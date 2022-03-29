import enum
import json, requests
import pydantic
from typing import Optional, List


class ISBNMissingError(Exception):
    '''custom error '''

    def __init__(self, title:str, message:str)-> None:
        self.title = title
        self.message= message
        super().__init__(message)

class ISBN10FormatError(Exception):
    ''' custom error Not right format '''
    def __init__(self, value:str, message:str)-> None:
        self.value = value
        self.message = message
        super().__init__(message)

class MyBook(pydantic.BaseModel):
    title:str
    author:str
    publisher:str
    price:float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        '''make sure there is either an isbn10 or isbn13 value defined.'''
        if ("isbn_10" not in values) and ("isbn_13" not in values):
            raise ISBNMissingError(value =values['title'], message="show be ...")
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value):
        '''Validator to check whether ISBM10 is valid'''
        chars = [ c for c in value if c in "0123456789Xx"]
        if len(chars) !=10:
            print("ERRRRRRR")
            raise ISBN10FormatError(value= value, message="should be 10digit")
        
        def char_to_int(char:str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        
        weighted_sum = sum((10-i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum %11 !=0:
            raise ISBN10FormatError(value= value, message="should be 10digit")
        
        
        return value
    
    class Config:
        ''' Pydantic config class'''
        allow_mutation = False



def main() -> None:
    with open("examtest/data.json") as file:
        data = json.load(file)
    books: List[MyBook] = [MyBook(**item) for item in data]
    books[0].title = "alkdfja;dslfk book"
    print(books[0])  

if __name__ == "__main__":
    main()