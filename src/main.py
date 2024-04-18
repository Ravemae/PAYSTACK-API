import os
from fastapi import FastAPI
from pydantic import BaseModel
from Paystack import Payment
from dotenv import load_dotenv

load_dotenv()
sk = os.environ.get("secret_key")


class Data(BaseModel):
    email : str
    cash : float
    
app = FastAPI()

@app.post("/pay/")
async def pay(data: Data):
    Email = data.email
    Cash = data.cash
    data = Payment(Email, Cash, sk)
    response = data.pay()
    return response