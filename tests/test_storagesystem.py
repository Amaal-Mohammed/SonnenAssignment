import pytest

import source.storage_system as storage


@pytest.mark.parametrize('battery_setup', ("1", "3", "5"))
class TestStorageSystem:

    @pytest.fixture
    def basic_battery2(self):
        self.basic.pvpanel.setProduction("production", "1")
        self.basic.house.setConsumption("consumption", "2")

    @pytest.fixture
    def basic_battery(self, request):
        self.basic.pvpanel.setProduction("production", "2")
        self.basic.house.setConsumption("consumption", "1")

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.basic = storage.StorageSystem({})

    def test_storage_charge_when_prod_greater_than_consume(self, basic_battery, battery_setup):
        self.basic.setbattery("battery", battery_setup)
        actual, _ = self.basic.controller("production", "consumption")
        assert actual is True

    def test_gridcharge_when_prod_greater_than_consume(self, basic_battery, battery_setup):
        self.basic.setbattery("battery", battery_setup)
        _, actual = self.basic.controller("production", "consumption")
        assert actual is True

    def test_storage_charge_when_prod_less_than_consume(self, basic_battery2, battery_setup):
        self.basic.setbattery("battery", battery_setup)
        actual, _ = self.basic.controller("production", "consumption")
        print(self.basic.house.getConsumption)
        assert actual is False

    def test_gridcharge_when_prod_less_than_consume(self, basic_battery2, battery_setup):
        self.basic.setbattery("battery", battery_setup)
        _, actual = self.basic.controller("production", "consumption")
        assert actual is False

    def teardown_method(self, method):
        print(f"tear down {method}")
        del self.basic
