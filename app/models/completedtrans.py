from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base

class CompletedTrans(Base):
    __tablename__ = 'completedtrans'
    trans_id:str=Column(String(10),primary_key=True)
    account_id:str=Column(String(10))
    type:str=Column(String(10))
    amount:str=Column(String(10))
    balance:str=Column(String(10))
    fulldate:str=Column(String(15))
    
   
    
    def __init__(self,trans_id, balance:str,amount:str, type:str=None,account_id:str=None,fulldate:str=None):
        self.account_id = account_id
        self.balance=balance
        self.type=type
        self.fulldate=fulldate
        self.amount=amount
        self.trans_id=trans_id
    
    def __repr__(self) -> list:
        return [f'{self.balance}',f'{self.account_id}',f'{self.fulldate}',f'{self.amount}',f'{self.type}']