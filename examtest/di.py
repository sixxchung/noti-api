import json

# read : 파일 전체
# readline: 한라인데이터
# readlines: 전체데이터를 라인단위로 

# data = '{"1":"one", "2":"둘", "삼":"셋"}'    # str
with open('../app/data/mobi-ex1.json', 'r') as line:
    data = line.read()

s2d = json.loads(data)
# {'1': 'one', '2': '둘', '삼': '셋'}          # dict

d2s = json.dumps(s2d)
# '{"1": "one", "2": "\\ub458", "\\uc0bc": "\\uc14b"}'  # str
d2s_ko = json.dumps(s2d, ensure_ascii=False)
# '{"1": "one", "2": "둘", "삼": "셋"}'


# data = "{'1':'one', '2':'둘', '삼':'셋'}"    # str
with open('../app/data/mobi-ex1-single_quote.txt', 'r') as line:
    data = line.read()

s2d = json.loads(data)
# JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
s2d = json.loads(data.replace("'", "\""))

