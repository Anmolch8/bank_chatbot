from chattools import tools
from features import user_account_balance,last_transctions,check_usercard
import json
def generate_response(conversation:list[object],client:object)->str:
    
    response:object = client.chat.completions.create(  
    model="gpt-4o-mini",
    messages=conversation,
    tools=tools(),
    )
    tool_call:list= response.choices
    tools_result:str = tool_call[0].message.content
    function_name:str=tool_call[0].message.tool_calls

    if tool_call[0].message.tool_calls!= None:
       function_name=function_name[0].function.name
      

    if function_name== None:
       conversation.append({"role": "assistant", "content":tools_result})
       return tools_result,conversation
    if function_name=='user_account_balance':
      tools_result=json.loads(tool_call[0].message.tool_calls[0].function.arguments)
      parameter:str=tools_result['lastdigits']
      #lastdigits:str=parameter.get('lastdigits')
      balance:str=str(user_account_balance(parameter))
    
      function_call_result:object = {
      "role": "tool",
      "content":json.dumps(
         {
      "last_digits": parameter,
      "balance": balance
      }
      ),
      "tool_call_id":tool_call[0].message.tool_calls[0].id
      }
      conversation.append(response.choices[0].message)
      conversation.append(function_call_result)

      payload_response:str = client.chat.completions.create(  
      model="gpt-4o-mini",
      messages=conversation,
      )

      return payload_response.choices[0].message.content,conversation

    if function_name=='last_transctions':
      tools_result=json.loads(tool_call[0].message.tool_calls[0].function.arguments)
      parameter:str=tools_result['lastdigits_trans']
      trans:str=last_transctions(parameter)

      function_call_result:object = {
      "role": "tool",
      "content": json.dumps({
      "last_trans": parameter,
      "transactions": trans
      }),
      "tool_call_id": tool_call[0].message.tool_calls[0].id
      }
      conversation.append(response.choices[0].message)
      conversation.append(function_call_result)

      payload_response:str = client.chat.completions.create(  
      model="gpt-4o-mini",
      messages=conversation,
      )

      return payload_response.choices[0].message.content,conversation
  
    if function_name=='check_usercard':
      tools_result=json.loads(tool_call[0].message.tool_calls[0].function.arguments) 
      parameter:str=tools_result['lastdigits_cards']
      card:dict[str,str]=check_usercard(parameter)
      balance:str=str(user_account_balance(parameter))
      function_call_result:object = {
      "role": "tool",
      "content": json.dumps({
      "last_cards": parameter,
      "card": card,
      "balance":balance
      }),
      "tool_call_id":  tool_call[0].message.tool_calls[0].id
      }
      conversation.append(response.choices[0].message)
      conversation.append(function_call_result)

      payload_response:str = client.chat.completions.create(  
      model="gpt-4o-mini",
      messages=conversation,
      )

      return payload_response.choices[0].message.content,conversation
    
    
    
      