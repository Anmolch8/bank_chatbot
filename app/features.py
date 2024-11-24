
from database import db_session
from models.userModel import User,ShowUsers
from models.dispositionsModel import CompletedDisposition
from models.completedtrans import CompletedTrans
from models.completedcard import CompletedCard
from decimal import Decimal
from models.transactionsview import TransactionModel
import json



def user_account_balance(lastdigits:str)-> int:
    acc_num=search = "%{}".format(lastdigits)
    user_acc:str=db_session.query(User,CompletedDisposition).join(CompletedDisposition).filter(CompletedDisposition.account_id.like(acc_num)).all()[0]._data[1].account_id
    user_balance:int=db_session.query(CompletedTrans).filter(CompletedTrans.account_id==user_acc).order_by(CompletedTrans.fulldate.desc()).first()
    return Decimal(user_balance.balance)

def last_transctions(lastdigits_trans:str)->str:
      values:list=[]
      acc_num=search = "%{}".format(lastdigits_trans)
      user_acc:str=db_session.query(User,CompletedDisposition).join(CompletedDisposition).filter(CompletedDisposition.account_id.like(acc_num)).all()[0]._data[1].account_id
      for trans in db_session.query(CompletedTrans).filter(CompletedTrans.account_id==user_acc).limit(5).all():
           #values.append(trans.__dict__)
           values.append(TransactionModel(
                 trans_id=trans.trans_id,
                 account_id=trans.account_id,
                 type=trans.type,
                 amount=trans.amount,
                 balance=trans.balance,
                 fulldate=trans.fulldate
           ).model_dump())
      
      return json.dumps(values)

def check_usercard(lastdigits_cards:str) ->dict[str:str]:
    card:dict[str,str]=dict()
    acc_num=search = "%{}".format(lastdigits_cards)
    try:
     check_type:str=db_session.query(CompletedCard,CompletedDisposition).join(CompletedDisposition).filter(CompletedDisposition.account_id.like(acc_num)).all()[0]._data[0].type
     card["1"]=check_type
    except:
       card["0"]='no card'

    return json.dumps(card)