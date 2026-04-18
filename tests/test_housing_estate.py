from lib.house import House
from lib.housing_estate import HousingEstate

# When we build houses and a housing estate
# The houses can be added to the housing estate
def test_add_houses_to_housing_estate():
    house1 = House(137, "white")
    house2 = House(24, "red")
    housing_estate = HousingEstate()
    housing_estate.houses.append(house1)
    housing_estate.houses.append(house2)
    assert housing_estate.houses == [house1, house2]

# When we build houses and a housing estate
# And the houses are added to the housing estate
# We can get a list of the house numbers of those houses
def test_get_house_numbers():
    house1 = House(137, "white")
    house2 = House(24, "red")
    housing_estate = HousingEstate()
    housing_estate.houses.append(house1)
    housing_estate.houses.append(house2)
    assert housing_estate.get_house_numbers() == [137, 24], "Should return house numbers: [137, 24]" # => [137, 24]
