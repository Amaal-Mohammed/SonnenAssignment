class house:
    def __init__(self, storesystem):
        self.store = storesystem

    def setConsumption(self, key: str, value):
        self.store[key] = value
        return True

    def getConsumption(self, key: str):
        return str(self.store.get(key))
