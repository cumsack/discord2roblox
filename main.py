import requests

target = input("Target: ")
bloxlinkapikey = ""

r=requests.get(f"https://v3.blox.link/developer/discord/{target}", headers={"api-key": bloxlinkapikey}).json())
if r["success"] == True and str(r) != "{'success': True, 'user': {}}" and r["user"]["robloxId"] != None:
  print(r["user"]["robloxId"])
else:
  print("couldnt find shit")
