import random
k=['rock','paper','scissor']
a=random.choice(k)
b=input("rock/paper/scissor:")
print(a)
if (a=='rock' and b=='paper') or (a=='paper' and b=='scissor') or (a=='scissor' and b=='rock'):
    print('b won')
elif(a==b):
    print('draw')
else:
    print('a won')