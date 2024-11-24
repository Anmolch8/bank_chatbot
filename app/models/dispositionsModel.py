from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship
#from models.userModel import User

class CompletedDisposition(Base):
    __tablename__ = 'completeddisposition'
    client_id = Column(String(20), ForeignKey("completedclient.client_id"))
    disp_id=Column(String(15),ForeignKey("completedcard.disp_id"))
    account_id=Column(String(10),primary_key=True)
    def __init__(self,client_id:String=None, account_id:String=None):
        self.account_id = account_id
        self.client_id=client_id
    def __repr__(self):
        return [f'{self.client_id}',f'{self.account_id}']