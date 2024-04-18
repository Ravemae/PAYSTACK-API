import os
import requests
from dotenv import load_dotenv


class Payment:
    def __init__(self, key, email, amount):
        self.key = key
        self.email = email
        self.amount = amount * 100
        
    def pay(self):
        url = "https://api.paystack.co/transaction/initialize"
        data = {
            "email": self.email,
            "amount": self.amount 
        }
        
        headers = {
            "Authorization": "Bearer " + self.key,
            "Content+Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json() 
            ref = data['data']['reference']
            auth_link = data['data']['authorization_url']
            result = {
                'reference_id': ref,
                'auth_url': auth_link
                }
            return result
        return "404" 
    
