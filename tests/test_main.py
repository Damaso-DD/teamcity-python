import time
import random
from src.main import get_greeting

def test_get_greeting():
    """Tests the get_greeting function for a standard name."""
    assert get_greeting('World') == 'Hi, World'


#def test_slow_greeting_generation():
#    """Simulates a slow operation during a test."""
#    time.sleep(180)  # Sleep for 180 seconds
#    assert get_greeting("Slowpoke") == "Hi, Slowpoke"


#def test_flaky_greeting():
#    """
#    This is a flaky test. It will randomly fail about 33% of the time.
#    """
#    roll = random.randint(1, 3)
#    assert roll != 1  # Fails if the number is 1


