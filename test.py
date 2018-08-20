import json

with open('settings.json', 'r+') as f:
    data = json.load(f)
    print(data['recording'])
    data['id'] = 134 # <--- add `id` value.
    data['recording'] = "True"
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()     # remove remaining part
