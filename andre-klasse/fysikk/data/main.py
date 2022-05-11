import json

data = {}

with open("./data.json") as f:
    str_data = f.read()

    data = json.loads(str_data)

for i in list(data.keys()):
    data[i] = float(data[i])

# def solve()

print(f'$$H-1 = {data["H-1"]}$$')