import os
import json

def setVariables()-> None:
 with open("appsettings.json") as data:
    data = json.load(data)


 os.environ['DBDriver']=data['DBDriver']
 os.environ['SERVER']=data['SERVER']
 os.environ['DATABASE']=data['DATABASE']
 os.environ['UID']=data['UID']
 os.environ['PWD']=data['PWD']
 os.environ['OPENAI_API_KEY']=data['OPENAI_API_KEY']

