def deco1(func):
    def aa(*args):
        print(func.__name__, 'start')
        print(f'args: {args}, kwargs: {kwargs}')
        func(*args, **kwargs)
        print(func.__name__, 'end')

    return aa


@deco1
def cccc(n, val):
    print('cccc 함수')
    print(n, val)


cccc(10, val=False)
