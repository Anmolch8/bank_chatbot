
def moderation_check(user_input:str,client:object)-> str:
  response = client.moderations.create(input=user_input)
  moderation_output = response.results[0].flagged
  if moderation_output == True:
    return "Flagged"
  else:
    return "Not Flagged"