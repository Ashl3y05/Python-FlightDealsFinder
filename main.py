from flight_deals import FlightDeals
from destination_data import DestinationData
from datetime import datetime,timedelta

flight_offers = FlightDeals()
destinations = DestinationData()


def get_next_day_date() -> str:
    date_tomorrow = datetime.now() + timedelta(days=1)
    return date_tomorrow.strftime("%Y-%m-%d")


ORIGIN_CITY = "MNL"

city_iata = {}

all_destinations = destinations.get_all_destinations()

for city in all_destinations:
    city_info = flight_offers.search_city(city, 1)
    iata_code = city_info["data"][0]["iataCode"]
    city_iata[city] = iata_code



#


# TODO: Get the cheapest flight offer using key and values from city_iata dictionary
#
#
# cheapest_flight = result["data"][0]["price"]["total"]
row = 1
for item in city_iata:
    result = flight_offers.get_cheapest_offer(ORIGIN_CITY, city_iata[item], get_next_day_date())
    lowest_price = float(result["data"][0]["price"]["total"])
    last_price = destinations.get_last_price(row)
    if lowest_price < last_price:
        print(f"LOWEST!! - last{last_price} - now{lowest_price}")
    row += 1
    destinations.put_excel_data(city=item, iata_code=city_iata[item], lowest_price=lowest_price,row_id=row)


# TODO: Send a text using twilio if the offer is cheaper than the price from the excel file

# TODO: Record to excel if it is the lowest offer
