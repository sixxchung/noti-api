status = 200

# if status == 200:
#     print("OK!")
# elif status == 300:
#     print("Err")
# else:
#     print("unknown")

# switch py=3.10
match status:
    case 200:
        print("OK!")
    case 300 | 400:
        print("Err")
    case _:
        print("unknown")
