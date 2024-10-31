class grid:
    def __init__(self):
        self.gridcharge = False;

    def process_grid(self, gridcharge: bool):
        self.gridcharge = gridcharge

    def getpower(self, key: str):
        return str(self.store.get(key))
