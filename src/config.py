import json

_CONFIG_PATH = "/private/config.json"
with open(_CONFIG_PATH) as config_file:
    cfg = json.load(config_file)

DISCORD_KEY = cfg['discord']
SUBMIT_CHANNEL = cfg['channels']['submit']
MOD_ROLES = cfg['roles']['moderator']
AWARDED_ROLES = cfg['roles']['awards']

