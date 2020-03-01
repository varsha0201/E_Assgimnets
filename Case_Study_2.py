# Problem 1
Output : 4

# Problem 2
Output : ['john','peter']

#Problem 3
import re

password = str(input('Enter the Password:'))
pattern = re.match(r'[A-Za-z0-9@#$%^&+=!]{6,12}$', password)
if(pattern):
    print("Valid password!")
else:
    print("Invalid Password!!","\n" "Password must contain atleast 1 letter from(A-Z, a-z, 0-9,'@#$%^&+=!').""\n""Password length between 6-12.")


#Pronlem 4
a = [4,7,3,2,5,9]
j =0
for i in a:
    print("Position Of",i,"is ",j)
    j+=1

