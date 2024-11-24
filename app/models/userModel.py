from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base
#from  models.dispositionsModel import CompletedDisposition
from sqlalchemy.orm import relationship


class User(Base) :
    __tablename__ = 'completedclient'
    client_id = Column(String(20),primary_key=True)
    first = Column(String(50))
    email = Column(String(120), unique=True)
 
    def __init__(self,client_id:String=None, first:String=None, email:String=None):
        self.first = first
        self.email = email
        self.client_id=client_id
     
    def __repr__(self):
        return [f'{self.first}',f'{self.email}',f'{self.client_id}']


class ShowUsers(object):
    def __init__(self,user):
        self.user=user
    