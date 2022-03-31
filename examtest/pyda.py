from typing import Optional, List
import enum
import uvicorn, fastapi

import json, requests
import pydantic

class ISBNMissingError(Exception):
    '''custom error '''
    def __init__(self, title:str, message:str)-> None:
        self.title = title
        self.message= message
        super().__init__(message)

class Error_ISBN10Format(Exception):
    ''' custom error Not right format '''
    def __init__(self, value:str, message:str)-> None:
        self.value = value
        self.message = message
        super().__init__(message)  # 부모의 메소드 또는 속성을 자동으로 불러와 사용

class MyBook(pydantic.BaseModel):
    title:str
    author:str
    publisher:str
    price:float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
# https://youtu.be/Vj-iU-8_xLs?t=682
    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, value):
    #     '''make sure there is either an isbn10 or isbn13 value defined.'''
        if ("isbn_10" not in values) and ("isbn_13" not in values):
            raise Error_ISBNMissing(value =values['title'], message="show be ...")
        return value

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None :
        '''Validator to check whether ISBM10 is valid
        모든 ISBN 10은 978로 시작되었습니다. ISBN의 마지막 번호는 <확인번호>. 
        예를 들어 ISBN 10에서 처음 9 자리에 10부터 2까지의 숫자를 곱한 다음 모든 결과를 더합니다. 
        이 결과를 11로 나눕니다. 나머지가 없으면 ISBN 번호만 유효합니다.
         0  6  1  8  2  6  9  4  1  <>
        10  9  8  7  6  5  4  3  2
         0+54+ 8+56+12+30+36+12+ 2 =210
        210 // 11 = 19 + 1      1+<> =11   <>=10 =X
        '''
        chars = [ c for c in value if c in "0123456789Xx"]
        if len(chars) !=10:
            raise Error_ISBN10Format(value=value, message="should be 10digit")
        
        def char_to_int(char:str) -> int :
            if char in "Xx":
                return 10
            return int(char)
        
        weighted_sum = sum((10-i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum %11 !=0:
            raise Error_ISBN10Format(value= value, message="should be divisible by 11")
        
        return value
    
    class Config:
        ''' Pydantic config class'''
        allow_mutation = False

def main() -> None:
    with open("examtest/data.json") as file:
        data = json.load(file)
    #print([MyBook(**item) for item in data])
    books: List[MyBook] = [MyBook(**item) for item in data]
    #books[0].title = "k"
    print(books[0])  

if __name__ == "__main__":
    main()
    #uvicorn.run("pyda:app", host="0.0.0.0", port=8886, reload=True)