import asyncio
import os
import sys
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


env_vars = {}
if os.path.isfile('.device'):
    with open('.device') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value.replace("\"", "")
else:
  print("error, are you sure you have put the ids correctly in the file .device ?")
  sys.exit()

os.system('python3 -m pip install --upgrade XBXBOT')
os.system('clear')

import XBXBOT

client = XBXBOT.XBXBOT(
  device_id=env_vars['DEVICE_ID'],
  account_id=env_vars['ACCOUNT_ID'],
  secret=env_vars['SECRET']
)

try:
  client.run()
except Exception as e:
  print(e)
  print("Can't login because your device auths is probably wrong.")
  print("are you sure you have put your IDs in secrets env or in .device  file ?")
