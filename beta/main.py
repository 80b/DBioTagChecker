# Beta releases are UNSTABLE.
import requests

print("""

╋╋┏┳━━┓╋╋╋╋╋┏━━━━┓╋╋╋╋╋┏━━━┳┓╋╋╋╋╋╋╋┏┓
╋╋┃┃┏┓┃╋╋╋╋╋┃┏┓┏┓┃╋╋╋╋╋┃┏━┓┃┃╋╋╋╋╋╋╋┃┃
┏━┛┃┗┛┗┳┳━━┓┗┛┃┃┣┻━┳━━┓┃┃╋┗┫┗━┳━━┳━━┫┃┏┳━━┳━┓
┃┏┓┃┏━┓┣┫┏┓┃╋╋┃┃┃┏┓┃┏┓┃┃┃╋┏┫┏┓┃┃━┫┏━┫┗┛┫┃━┫┏┛
┃┗┛┃┗━┛┃┃┗┛┃╋╋┃┃┃┏┓┃┗┛┃┃┗━┛┃┃┃┃┃━┫┗━┫┏┓┫┃━┫┃
┗━━┻━━━┻┻━━┛╋╋┗┛┗┛┗┻━┓┃┗━━━┻┛┗┻━━┻━━┻┛┗┻━━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛
           ╋Beta!╋
This tool was NOT made by Discord.bio staff and this is unofficial.

By: Raz AKA razb_erries
Bugs: add raz#7092 on discord or make an issue on github.
Link: https://github.com/razberries/DBioTagChecker

Modes:
	[1] ID Checker
	[2] Slug checker
	[3] Exit the app
	[4] Get raw JSON for Slug and UID
""")
inp = int(input("Which mode?: "))

url = "https://api.discord.bio/user/details/" 

while inp != 3:
	if inp == 1:
		id = input("What is the ID you would like to check?: ")
		rea = requests.get(url + id)
		dbioUserStr = requests.get(rea + "?username")
		if rea.status_code == 200:
			print(id + " has a Dbio account!")
		else:
			print(id + " does NOT have a dbio account!")
	if inp == 2:
		slug = input("What is the slug you would like to check?: ")
		resp = requests.get(url + slug)
		if resp.status_code == 200:
			print(slug + " is taken! try again.")
		else:	
			print(slug + " is not taken OR there is a outage")
	if inp == 4:
		print("""
Available modes:
	Slug
	ID
			""")
		# idUrl = requests.get(url + id)
		# slugUrl = requests.get(url + id)
		slugorid = input("Mode?: ")
		if slugorid == "Slug":
			slugInput = input("Slug?: ")
			slugUrl = requests.get(url + slugInput).json()
			print(slugUrl)
		if slugorid == "ID":
			
			idInput = input("ID?: ")
			idUrl = requests.get(url + idInput).json()
			print(idUrl)
print("Thanks for using Dbio Tag Checker.")
