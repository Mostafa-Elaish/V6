class Movement:
    def __init__(self, settings):
        self.settings = settings
    def drive(self, vx, vy):
        print(f'Drive: vx={vx}, vy={vy}')
