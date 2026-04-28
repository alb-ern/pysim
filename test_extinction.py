import pygame as pg
import os
import threading
import time
from unittest.mock import patch, MagicMock

os.environ['SDL_VIDEODRIVER'] = 'dummy'

# Mock input to quickly trigger extinction and spacebar/escape
def run_test():
    import main

    def simulate_events():
        # Wait a bit
        time.sleep(1)
        # Kill all agents to trigger extinction
        print("Test: Triggering extinction via agents mock")
        # Simulate spacebar press (should be ignored since extinct)
        time.sleep(0.5)
        print("Test: Sending Space")
        pg.event.post(pg.event.Event(pg.KEYDOWN, key=pg.K_SPACE))

        # Simulate escape to close
        time.sleep(0.5)
        print("Test: Sending Escape")
        pg.event.post(pg.event.Event(pg.KEYDOWN, key=pg.K_ESCAPE))

    t = threading.Thread(target=simulate_events)
    t.daemon = True
    t.start()

    # Run main, overriding the initial population to 0 so we trigger extinction immediately
    with patch('main.load_config') as mock_load_config:
        import json
        with open("config.json", "r") as f:
            config = json.load(f)
        config["agent"]["initial_population"] = 0
        mock_load_config.return_value = config

        main.main()

if __name__ == '__main__':
    run_test()
