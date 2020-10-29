# realmstatus
A very basic realm status check using the Blizzard API. This script requires that your client (app) is already authorized on the `wow.profile` scope.

## Using the script
Update the `myCreds.json` file with your client_id and client_secret.

Run then `realmstatus.py` script.

The script now support two flags (`-r` and `-t`) that can be appended at runtime.

`-r` allows you to pass the realm, using the Blizzard Realm Slug. More info [here](https://)

`-t` will display your current token alongside the realm status.

Example command: `realmstatus.py -r frostmane -t`

Example output:
![Screenshot](/realmstatus.png?raw=true "Screenshot")

# wownews
This is just a webscaper sample to grab patch notes. It completely standalone, but I didn't have anywhere else to put it.
