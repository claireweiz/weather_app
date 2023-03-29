
import json

f = open('iconcode.json', 'r')
str= json.load(f)

print(str)
#if dict["code"] == "1261":
#	print(dict["icon"])

f.close()
