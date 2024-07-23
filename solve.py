

#k=int(input())
#my_list=list(map(int,input().split()))
#sum=(k*(k+1))//2
#sum1=0
#for i in range(1,k+1):
#print(sum)
#for i in range(0,len(my_list)):
    #sum1+=my_list[i]
#print(sum-sum1)
''' sum of digits'''

n=int(input())
sum=0
while(n>0):
   a=n%10
   sum+=a
   n=n//10
print(sum)
'''find the sum of squares in a given digit'''

n=int(input())
sum=0
while(n>0):
   a=n%10
   sum=sum+a**2
   n=n//10
print(sum)



        
        



    