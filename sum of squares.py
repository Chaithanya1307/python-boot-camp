n=int(input())
sum=0
while(n>0):
   a=n%10
   sum=sum+a**2
   n=n//10
print(sum)

