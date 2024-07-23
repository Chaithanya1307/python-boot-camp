#str=input()
#print(str.title())
#print(str.upper())
#print(str.lower())
#print(str.swapcase())
#print(str.strip())
#print(str.split("a"))
#print(str.isnumeric())
#print(str.isnumeric())
#print(str.isdigit())

#char=input()
#print(ord(char))

'''check how may vowels are there in a given string'''

#str=input()
#Print(vowels)
#vowels=['a','e','i','o','u']
#count=0
#for i in str:
   #if(i in vowels):
      #count+=1
#print(count)



#str=input()
#vowels=('a','e','i','o','u')
#consonants="bcdfghjklmnpqrstvwxyz"
#count=0
#c=0
#l="hello world"
#inp= l.lower()
#for i in str:
    #if(i in vowels):
        #count+=1
#print(count)   
#for i in inp:
    #if(i in consonants):
        #c+=1
#print(count)
#print(c)             

str=input()
str1=""
str2=""
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
for i in str:
    if(i in vowels):
       str1+=i
for i in str:
    if(i in consonants):
       str2+=i
print(str1+str2)           

