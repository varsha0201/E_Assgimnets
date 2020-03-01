# problem 1
n = int(input("Enter the no:"))
factorial = 1

if n < 0:
    print("Their is no factorial calculate for negative no")
elif n == 0:
    print("factorial of zero is 1")
else:
    for i in range(1, n+1):
        factorial = factorial * i
    print("factorial of",n,"is",factorial,".")
    if factorial%2 ==0:
        print("factorial no is even.")
    else:
        print("factorial no is odd.")
        
 
# Problem 2       
int_str = input("Eneter the words:")

words = int_str.split()
words.sort()
print("sorted words are:")
for word in words:
    print(word)
  
    
#Problem 3
for i in range(1000,3000):
    if i %2 ==0:
        print('{:,}'.format(i))
    
    
#Problem 4
string = input("Enter the string:")
digit=letter=0

for count in string:
    if count.isdigit():
        digit = digit+1
    elif count.isalpha():
        letter = letter+1
    else:
        pass
print("LETTERS:",letter)
print("DIGITS:",digit)

#Problem 5
no = int(input("Entre the no:"))
temp = no
rev = 0
while(no>0):
    dig=no%10
    rev = rev*10+dig
    no = no//10
if(temp==rev):
    print("This is the Palindrome no.")
else:
    print("This is not Palindrome no.")



