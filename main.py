from flight_deals import FlightDeals
from destination_data import DestinationData

flight_offers = FlightDeals()
destinations = DestinationData()

ORIGIN_CITY = "MNL"

city_iata = {}

all_destinations = destinations.get_all_destinations()

for city in all_destinations:
    city_info = flight_offers.search_city(city, 1)
    iata_code = city_info["data"][0]["iataCode"]
    city_iata[city] = iata_code


# destinations.put_excel_data(city="Paris",iata_code="CDG",lowest_price=53)


# TODO: Get the cheapest flight offer using key and values from city_iata dictionary

# TODO: Send a text using twilio if the offer is cheaper than the price from the excel file

# TODO: Record to excel if it is the lowest offer
