# discord-jeeves

## Installation
- Clone this repository to a directory you want the bot to run from
- `pip3 install -r requirements.txt`
- Copy `jeevesbot/env.py.dist` to `jeevesbot/env.py` and change the variables.
- Copy `jeevesbot/secret.json.dist` to `jeevesbot/secret.json` and add your Google Drive API secret.json
- `cp scripts/jeeves.service /etc/systemd/system/jeeves.service` and change the variables to suit your environment.
- `systemctl daemon-reload`
- `systemctl start jeeves.service`