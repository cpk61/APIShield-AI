from core import APIShield

def test_burst_error_detection():
    shield = APIShield(window_s=60)
    out = None
    for i in range(130):
        out = shield.inspect('client-x', 404, 100, f'/path/{i}')
    assert out['risk'] > .7
    assert 'high_request_burst' in out['reasons']
    assert 'high_error_ratio' in out['reasons']
