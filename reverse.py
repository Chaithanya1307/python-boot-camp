n=int(input())
rev=""
while(n>0):
   a=n%10
   rev=rev+str(a)
   n=n//10
print(int(rev))

