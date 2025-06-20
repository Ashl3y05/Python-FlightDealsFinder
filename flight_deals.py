import requests
import os


class FlightDeals:
    def __init__(self):
        self.amadeus_api_key = os.environ["AMADEUS_API_KEY"]
        self.amadeus_secret_key = os.environ["AMADEUS_SECRET"]
        self.amadeus_base_endpoint = "https://test.api.amadeus.com/v2"
        self.amadeus_access_token = self.get_access_token()
        self.flight_offers_endpoint = "/shopping/flight-offers"
        self.city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    def get_access_token(self):
        api_key = self.amadeus_api_key
        secret_key = self.amadeus_secret_key
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        data = {
            "grant_type":"client_credentials",
            "client_id": api_key,
            "client_secret": secret_key
        }
        response = requests.post(url=url,data=data,headers=header)
        result = response.json()
        return f"{result["token_type"]} {result["access_token"]}"

    def search_city(self, city: str, max_result: int):

        data = {
            "keyword": city,
            "max":str(max_result)
        }

        header = {
            "Authorization": self.amadeus_access_token
        }
        response = requests.get(url=self.city_search_endpoint,params=data,headers=header)
        return response.json()

    def get_cheapest_offer(self, origin_city_code, destination_city_code,departure_date):
        header = {
            "Authorization": self.amadeus_access_token
        }

        data = {
            "originLocationCode":origin_city_code,
            "destinationLocationCode":destination_city_code,
            "departureDate":departure_date,
            "adults": 1,
            "currencyCode": "PHP",
            "max": 5
        }

        response = requests.get(url=f"{self.amadeus_base_endpoint}{self.flight_offers_endpoint}", params=data,headers=header)
        return response.json()