class pvpanel:
    def __init__(self, storesystem):
        self.storesystem = storesystem

    def setProduction(self, key: str, value):
        self.storesystem[key] = value
        return True

    def getProduction(self, key: str):
        return str(self.storesystem.get(key))
