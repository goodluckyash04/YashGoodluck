x = int(input())
a = 1
while a==1:
    a+=1
    if (x == 0 or x == 1):
        print('x is exception')
    elif(x==2 or x==3 or x==5 or x==7):
        print('x is prime number')
    elif(x%2==0 or x%3==0 or x%5==0 or x%7 == 0):
        print("x is non-prime number")
    else:
        print('x is prime number')

