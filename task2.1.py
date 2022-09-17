# find the number divisible by which number

x = int(input())
if(x%2==0):
    a=x/2
    if(a%3==0):
        print('number is divisible by 2,3,6')
    else:
        print('number is divisible by 2')
