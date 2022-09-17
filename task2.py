# find the number divisible by which number

x = int(input())
if(x%10==0):
    if(x%4==0):
        if (x % 8 == 0):
            print("number is divisible by 2,4,8,5,10")
        if(x%8==0):
            print("number is divisible by 2,4,8,5,10")
        else:
            print('number is divisible by 2,4,5,10')
    elif(x%3==0):
        if (x % 6 == 0):
            if (x % 9 == 0):
                print("number is divisible by 2,3,5,6,9,10")
            else:
                print("number is divisible by 2,3,5,6,10")
        else:
            print('number is divisible by 2,3,5,10')
    elif(x%7==0):
        print("number is divisible by 2,5,7,10")
    else:
        print("number is divisible by 2,5,10")
# elif(x%3==0):
#
# elif(x%5==0):
# elif(x%7==0):
#     # if(x%4==0):
#     #     if (x % 6 == 0):
#     #         if (x % 8 == 0):
#     #             print("x is divisible by 2,4,6,8")
#     #         else:
#     #             print("x is divisible by 2,4,6")
#     #     else:
#     #         print("x is divisible by 2,4")
#     # else:
#     #     print("x is divisible by 2")
else:
    print("please try another number")