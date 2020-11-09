aimport requests

print("""

╋╋┏┳━━┓╋╋╋╋╋┏━━━━┓╋╋╋╋╋┏━━━┳┓╋╋╋╋╋╋╋┏┓
╋╋┃┃┏┓┃╋╋╋╋╋┃┏┓┏┓┃╋╋╋╋╋┃┏━┓┃┃╋╋╋╋╋╋╋┃┃
┏━┛┃┗┛┗┳┳━━┓┗┛┃┃┣┻━┳━━┓┃┃╋┗┫┗━┳━━┳━━┫┃┏┳━━┳━┓
┃┏┓┃┏━┓┣┫┏┓┃╋╋┃┃┃┏┓┃┏┓┃┃┃╋┏┫┏┓┃┃━┫┏━┫┗┛┫┃━┫┏┛
┃┗┛┃┗━┛┃┃┗┛┃╋╋┃┃┃┏┓┃┗┛┃┃┗━┛┃┃┃┃┃━┫┗━┫┏┓┫┃━┫┃
┗━━┻━━━┻┻━━┛╋╋┗┛┗┛┗┻━┓┃┗━━━┻┛┗┻━━┻━━┻┛┗┻━━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛

This tool was NOT made by Discord.bio staff and this is unofficial.

By: Raz AKA razberries
Bugs: add raz#7092 on discord or make an issue on github.
Link: https://github.com/razberries/DBioTagChecker
Official Discord Server: https://discord.gg/xQVfD85GN9

Modes:
	[1] ID Checker
	[2] Slug checker
	[3] Exit the app
""")
inp = int(input("Which mode?: "))

url = "https://api.discord.bio/user/details/" 

while inp != 3:
	if inp == 1:
		id = input("What is the ID you would like to check?: ")
		rea = requests.get(url + id)
		if rea.status_code == 200:
			print(inpa + " has a Dbio account!")
		else:
			print(inpa + " does NOT have a dbio account!")
	if inp == 2:
		slug = input("What is the slug you would like to check?")
		resp = requests.get(url + slug)
		if resp.status_code == 200:
			print(inp + " is taken! try again.")
		else:	
			print(inp + " is not taken OR there is a outage")
print("Thanks for using Dbio Tag Checker.")
