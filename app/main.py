
from flask import Flask,render_template,request,jsonify
import os,json
from database import db_session
from repository import GetAllUsers
from features import last_transctions
from initialize_conversation import initialize_conversation
from gptmodel import generate_response
from moderation_check import moderation_check
from openai import OpenAI

app = Flask(__name__)
app.app_context().push()
client = OpenAI()
client.api_key=os.environ.get('OPENAI_API_KEY')
chat_length:int=0
conversation:list[object]=[]
@app.route("/",methods=['GET'])
def Chatbot_initialization() ->object :
    system:str=initialize_conversation()
    conversation.append(
    {"role": "system", "content":system}
    )
    response=client.chat.completions.create(  
      model="gpt-4o-mini",
      messages=conversation,
    )
    
    return render_template('index.html',response=response.choices[0].message.content)
   # return render_template('index.html',response='test assistant')
@app.route("/send",methods=['POST'])
def chatbot_conversation() ->str:
    global chat_length
    if chat_length>9:
        return "conversation reached limit"
       
    customer_reply=json.loads(request.data)
    
    
    moderation_flag:str=moderation_check(customer_reply,client)
    if moderation_flag=="Flagged":
        return "Sorry! I cannot help you with that"
    
    message={"role": "user", "content":customer_reply["user"]}
    #del conversation[0]
    conversation.append(message)
    get_response=generate_response(conversation,client)
    response=get_response[0]
   # conversation.append(get_response[1][-1])
    chat_length+=1
    return jsonify({"reply":response})
    


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__=='__main__':
    Chatbot_initialization()
   #last_transctions('0112')
   # GetAllUsers()
    #shutdown_session()