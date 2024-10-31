import source.house as house
import source.pvpanel as panel


class StorageSystem:

    def __init__(self, storesystem):
        self.storesystem = storesystem
        self.pvpanel = panel.pvpanel({})
        self.house = house.house({})

    def setbattery(self, key: str, value):
        if int(value) > 2 or int(value) <= 0:
            print(f"Invalid value for basic system set up")
            self.storesystem[key] = 1
        else:
            self.storesystem[key] = value
        return True

    def getbattery(self, key: str):
        return str(self.storesystem.get(key))

    def controller(self, production, consume):
        if int(self.pvpanel.getProduction(production)) > int(self.house.getConsumption(consume)):
            storagecharge = True
            gridcharge = True
        else:
            storagecharge = False
            gridcharge = False

        return storagecharge, gridcharge
