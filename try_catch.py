try: 
    result = 10 // int(input())
except ZeroDivisionError: 
    print("զրոյին բաժանել չի կարելի") 
else:
    print("պատասխանն է`", result)
finally:
    print('էս էլ միիիիշտ կտպի')