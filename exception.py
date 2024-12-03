try:
    num1 = input("enter divisor:")
    num2 = input("enter divident:")
    result = num1/ num2
    print("The result of {num1} divided by {num2} is {result}")
except Exception as e:
    print("error occured",e)
else:
    print("no error")
finally:
    print("the program executed successfully")