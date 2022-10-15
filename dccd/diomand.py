#    *
#   * *
#  * A *
# * B C *
#  * D *
#   * *
#    *
num=int(input())
i = 0
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for uh in range((num//2)+1):
    s = ''
    for j in range(uh+1):
        if j==0 or j==uh:
            s += '* '
        else:
            s = s+alp[i]+' '
            if i == 25:
                i = 0
            else:
                i+=1
    s = s.center(num)
    print(s)

for lh in range(num//2,0,-1):
    s = ''
    for k in range(lh):
        if k==0 or k==lh-1:
            s += '* '
        else:
            s = s+alp[i]+' '
            if i == 25:
                i = 0
            else:
                i+=1
    s = s.center(num)
    print(s)

