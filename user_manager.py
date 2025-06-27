import requests
import smtplib

class UserManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/76ca9e17df4224ea156829a794c915ee/flightDeals/users"
        self.sender_email = "youremail@gmail.com"
        self.receiver_email = "recipient@example.com"
        self.password = "your_app_password"

    def get_user_data(self):
        response = requests.get(url=self.sheety_endpoint)
        return response.json()

    def get_user_email(self):
        data = self.get_user_data()
        all_emails = [data["users"][num]["whatIsYourEmail?"] for num in range(0, len(data["users"]))]
        return all_emails


    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message()
        pass