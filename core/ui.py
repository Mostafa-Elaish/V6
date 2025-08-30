class UI:
    def __init__(self, settings, movement, guard, telegram):
        self.settings = settings
        self.movement = movement
        self.guard = guard
        self.telegram = telegram
    def run(self):
        # placeholder UI loop - in real deploy this runs Flask + Touchscreen app
        print('UI running. Guard mode:', self.settings.get('security.guard_mode'))
        if self.settings.get('security.guard_mode'):
            self.guard.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.guard.stop()
