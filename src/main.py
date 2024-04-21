import os
from fastapi import FastAPI
from pydantic import BaseModel
from Paystack import Payment
from dotenv import load_dotenv

load_dotenv()
sk = os.environ.get("secret")


class Data(BaseModel):
    email : str
    cash : float
    
app = FastAPI()

@app.post("/pay")
async def pay(data_input: Data):
    Email = data_input.email
    Cash = data_input.cash
    data_instance = Payment(sk, Email, Cash )
    response = data_instance.pay()
    return response