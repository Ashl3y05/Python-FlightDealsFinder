import requests
import os
from datetime import datetime

class FlightDeals:
    def __init__(self):
        self.amadeus_api_key = os.environ["AMADEUS_API_KEY"]
        self.amadeus_secret_key = os.environ["AMADEUS_SECRET"]
        self.amadeus_base_endpoint = "http:/test.api.amadeus.com/v2"
        self.amadeus_access_token = os.environ["AMADEUS_ACCESS_TOKEN"]
        self.flight_offers_endpoint = "/shopping/flight_offers"
