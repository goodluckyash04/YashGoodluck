#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

for a in range(1,10):
    if a<=5:
        print(' ' * (6-a), end='')
        print('*' * a)
    else:
        print(' ' * (a-4),end='')
        print('*' * (10-a))
        