import re

Reference_Id = str(input('Enter the referenceId:'))
validity = re.match(r'[A-Za-z0-9]{12,}',Reference_Id)
print(validity)

if(validity):
    print('Valid user')
else:
    print('Invalid user')