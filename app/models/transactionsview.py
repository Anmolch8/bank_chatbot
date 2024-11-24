
from pydantic import BaseModel

class TransactionModel(BaseModel):
    trans_id:str
    account_id:str
    type:str
    amount:str
    balance:str
    fulldate:str