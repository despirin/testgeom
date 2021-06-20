import json

f = open("c:/temp/py/config.json")
try:
    res = json.load(f)
except ValueError:

f.close()

print(res)s