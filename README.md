# realmstatus
A very basic realm status check using the Blizzard API. This script requires that your client (app) is already authorized on the `wow.profile` scope.

## Using the script
Update the `myCreds.json` file with your client_id and client_secret.

Run then `realmstatus.py` script.

The script now support two flags (`-r` and `-t`) that can be appended at runtime.

`-r` allows you to pass the realm, using the Blizzard Realm Slug. More info [here](https://develop.battle.net/documentation/world-of-warcraft/game-data-apis?target=_blank). Realm slugs are normally the realm name that has been stripped of non-alphabet characters and spaces. An example would be `Ner'Zhul`. It's slug would be `nerzhul`.

`-t` will display your current token alongside the realm status.

Example command with output: `realmstatus.py -r frostmane -t`

![realmstatus.py Screenshot](/realmstatus.png?raw=true "realmstatus.py screenshot")

# wownews
This is just a webscaper sample to grab patch notes. It completely standalone, but I didn't have anywhere else to put it.
