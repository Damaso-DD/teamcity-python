from main import get_greeting

def test_get_greeting():
    """Tests the get_greeting function for a standard name."""
    assert get_greeting('World') == 'Hi, World'
