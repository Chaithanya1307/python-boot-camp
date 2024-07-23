#str=input()
#sum=0
#str1="hello world"
#num=i
#for i in str:
    #if(i in str):
       # str=str1-i# changes 
        #sum+=i
#print(sum)

#str=input()
#list="0123456789"
#sum=0
#for i in str:
    #if(i in list):
            #sum+=int(i)
#print(sum)

str=input()
sum=0
for i in str:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)        