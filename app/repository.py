from database import db_session
from models.userModel import User,ShowUsers
from models.dispositionsModel import CompletedDisposition

def GetAllUsers() ->list:
 users=[]
 for user,completeddisposition in  db_session.query(User,CompletedDisposition).join(CompletedDisposition).all():
    ho=user.account_1[0].account_id
    print(ho)

 return users