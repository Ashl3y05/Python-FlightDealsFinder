import requests


class DestinationData:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/76ca9e17df4224ea156829a794c915ee/flightDeals/sheet1"


    def get_excel_data(self) -> dict:
        """Returns all data from the Excel file"""
        response = requests.get(url=self.sheety_endpoint)
        return response.json()

    def get_all_destinations(self) -> list:
        """Returns a list of all destinations from excel file"""
        data = self.get_excel_data()
        all_destinations = [data["sheet1"][num]["city"] for num in range(0, len(data["sheet1"]))]
        return all_destinations

    def put_excel_data(self, city: str, iata_code: str, lowest_price: float,row_id: int):
        """Updates the Excel file"""
        edit_excel = {
            "sheet1": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": lowest_price
            }

        }
        response = requests.put(url=f"{self.sheety_endpoint}/{row_id}", json=edit_excel)
        print(f"Updated {city} - {iata_code} - {lowest_price}")

    def get_last_price(self,row_id):
        data = self.get_excel_data()
        return data["sheet1"][row_id - 1]["lowestPrice"]

