import random

phone=['samsung','apple','nokia','sony','lg','htc','motorola','huawei','xaiomi']
print("***Word Guess - Mobile Brands***\nYOU have 5 Chance to find the missing letter")
ans=phone[random.randint(0,len(phone)-1)]

nan=ans
def rep(inp,nans):
    for a in inp:
        nans = nans.replace(a, '_')
    return nans
counter=0
a=[]
while counter<7:
    if counter==0:
        print('_'*len(ans))
    inp=input('Enter a letter ')[0]
    a.append(inp)
    nan=rep(set(ans)-set(a),ans)
    print(nan)
    counter+=1
    if nan==ans:
        break

if nan == ans:
    print("Answer is correct "+ans.title())
else:
    print(ans.title()+" is the answer.Better luck next time !!!\nBye!")