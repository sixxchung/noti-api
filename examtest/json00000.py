import json

dict_a = {
    "C": 1.1,
    "O": True,
    "M": "HelloWorld",
    "P": {
        "X": 1,
        "Y": 2,
        "Z": 3
    },
    "U": 25,
    "T": None,
    "E": ["Python", "Is", "Beautiful"],
    "R": [1, 2, 100, 200]
}
targetKey = ["C", "P", "U"]
result = {k: dict_a[k] for k in targetKey}
result = {k: dict_a[k] for k in dict_a.keys() if k in targetKey}
result = {k:v for k,v in dict_a.items() if k in targetKey}
# {'C': 1.1, 'P': {'X': 1, 'Y': 2, 'Z': 3}, 'U': 25}
print(json.dumps(result, indent = 4))

result={}
for k,v in dict_a.items(): 
    if k in targetKey:
        result[k] = v

import itertools
dict( itertools.islice( dict_a.items(), 2))
# {'C': 1.1, 'O': True}


