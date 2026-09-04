from collections import defaultdict, deque
import time

class APIShield:
    def __init__(self, window_s=60, max_events=500):
        self.window_s = window_s
        self.events = defaultdict(lambda: deque(maxlen=max_events))

    def inspect(self, client_id, status_code, latency_ms, path, ts=None):
        ts = ts or time.time()
        q = self.events[client_id]
        q.append((ts, status_code, latency_ms, path))
        while q and ts - q[0][0] > self.window_s:
            q.popleft()
        n = len(q)
        errors = sum(s >= 400 for _, s, _, _ in q)
        unique = len({p for *_, p in q})
        avg = sum(latency for _, _, latency, _ in q) / n
        burst = min(1, n / 120)
        error_ratio = errors / n
        scan = min(1, unique / 40)
        latency = min(1, avg / 2000)
        risk = round(min(1, .4 * burst + .35 * error_ratio + .2 * scan + .05 * latency), 3)
        reasons = []
        if burst > .5:
            reasons.append('high_request_burst')
        if error_ratio > .3:
            reasons.append('high_error_ratio')
        if scan > .5:
            reasons.append('wide_path_scanning')
        action = 'block' if risk >= .8 else 'challenge' if risk >= .55 else 'allow'
        return {
            'risk': risk,
            'action': action,
            'reasons': reasons,
            'window_events': n,
            'error_ratio': round(error_ratio, 3),
        }
