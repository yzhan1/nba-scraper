
import pprint, json

file = open('data.json', 'r')
js = json.load(file)

for item in js:
    print(item)
