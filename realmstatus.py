# Imports and their uses
import requests # Used to get webpage HTML
import json # Used for reading json data
import time # Used for sleep in loop
import os # Used to get file paths
import sys # Used to read arguments from execution
import getopt # Used to read arguments from execution

slug = ''
showtoken = False

opts, args = getopt.getopt(sys.argv[1:],"hr:t")
for opt, arg in opts:
	if opt == '-h':
		print('realmstatus.py -r <realmslug> -t')
		sys.exit()
	elif opt in ("-r"):
		slug = arg
	elif opt in ("-t"):
		showtoken = True

# Set local current working directory
cwd = os.path.dirname(__file__)

# Read myCreds.json for client_id and client_secret
myCreds = os.path.join(cwd, "myCreds.json")
with open(myCreds, 'r') as f:
	myCreds = f.read()
	creds = json.loads(myCreds)
client_id = creds['client_id']
client_secret = creds['client_secret']

# API stuff
token_url = 'https://us.battle.net/oauth/token'

# Not used anymore, but keeping around
# These are used for authorizing you client with the wow.profile scope
# See more here:https://develop.battle.net/documentation/guides/using-oauth
#scope = "wow.profile"
#authorization_base_url = 'https://us.battle.net/oauth/authorize'
#redirect_uri="https://localhost"

# Colors for highlighting text (not all are used)
class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Function to get current/refresh token
def generateToken():
	global myToken
	data = {'grant_type': 'client_credentials'}
	# Fetch token response
	response = requests.post(token_url, data=data, auth=(client_id, client_secret))
	# Read response as json
	token = response.json()
	# Set variable from json response
	myToken = token['access_token']
	return myToken

# Execute function
generateToken()

# Request input of realm slug
if slug == '':
	slug = input("Please enter your realm slug (ex. frostmane): ")

# Search for realm by slug
realmAPI = "https://us.api.blizzard.com/data/wow/realm/" + slug + "?namespace=dynamic-us&locale=en_US&access_token=" + myToken
realmReq = requests.get(realmAPI)
realmJ = realmReq.json()

# Lookup the selected realm connected-realm ID
url = realmJ['connected_realm']['href'] + "&locale=en_US&access_token=" + myToken

# Get connected-realm group status
i = 0
# Try/Except for clean exit
try:
	while True:
		i += 1
		# Fetch info from Blizzard
		req = requests.get(url)
		# Read req as json
		jsonreq = req.json()
		# Clear screen
		os.system('cls' if os.name == 'nt' else 'clear')
		# Set variables from the json results
		status = jsonreq['status']['name']
		realms = jsonreq['realms']
		print([realm['name'] for realm in realms])
		if status == 'Down':
			print(f"The above realms are {bcolors.BOLD}{bcolors.RED}" + status + f"{bcolors.ENDC}.")
		else:
			print(f"The above realms are {bcolors.BOLD}{bcolors.GREEN}" + status + f"{bcolors.ENDC}.")
		print("This updates every 20 seconds. Number of updates: " + str(i))
		# Show current token if flag was used
		if showtoken == True:
			print('Current token: ', myToken)
		print('Press CTRL+C to exit.')
		time.sleep(20)
# Catch CTRL+C to exit loop
except KeyboardInterrupt:
	print("Exiting...")
	time.sleep(2)
