from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base

class CompletedCard(Base):
    __tablename__ = 'completedcard'
    disp_id:str=Column(String(10),primary_key=True)
    type:str=Column(String(15))
    
   
    
    def __init__(self,disp_id:str, type:str):
        self.type=type
        self.disp_id=disp_id
    
    def __repr__(self) -> list:
        return [f'{self.disp_id}',f'{self.type}']