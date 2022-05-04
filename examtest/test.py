import pandas as pd
import json

data = '''
{"$oid":"61","rental":{"a":"대여중","b":"a"},"class":"coml"}
'''
data = '{ "name":"John", "age":"30", "car":"None" }'

ldict = json.loads(data)
[ (k, v) for k, v in ldict.items()]

data = [{"name": "John", "age": "30", "car": "None"}]



pd.read_json(*data)

pd.DataFrame(ldict)
pd.DataFrame(data)


ddl = json.loads(data)
pd.DataFrame.from_dict(ldict)


print(a_json)

df.info()



data = '''
[
  {
    "id": "A001",
    "name": "Tom",
    "math": 60,
    "physics": 66,
    "chemistry": 61
  },
  {
    "id": "A002",
    "name": "James",
    "math": 89,
    "physics": 76,
    "chemistry": 51
  },
  {
    "id": "A003",
    "name": "Jenny",
    "math": 79,
    "physics": 90,
    "chemistry": 78
  }
]
'''