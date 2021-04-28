import cv2
import string
import os

d={}
c={}

for i in range (255):
    d[chr(i)]=i
    c[i]=chr(i)

x=cv2.imread("image.jpg")    

#i=x.shape[0]
#j=x.shape[1]
#print(i,j)

key=input("SECURITY KEY FOR ENCRYPTION :")
text=input("ENTER TEXT FOR ENCRYPTION :")

kl=0
tln=len(text)
z=0
n=0
m=0

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]
    n=n+1
    m=m+1
    m=(m+1)%3
    kl=(kl+1)%len(key)

cv2.imwrite("encrypted.jpg",x)

print(" ")
print("DATA IS HIDDEN IN IMAGE")
print(" ")

kl=0
tln=0
z=0
n=0
m=0

ch= int(input("PRESS 1 TO DECRYPT :"))
if ch==1:
    key1=input("SECURITY KEY FOR DECRYPTION :")
    decrypt=""


    if key==key1:
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[kl]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            kl=(kl+1)%len(key)
    
        print("THE TEXT WAS :",decrypt)
    else:
        print("KEY DOES NOT MATCH") 
else:
    print("EXITING")              

            
            
            
            
