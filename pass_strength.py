#This is my trial code

mystr = input("Enter the password : ")
strength = 0
        
alp = False
num = False
cu = cl = False

for x in range(len(mystr)):
    if mystr[x].isalpha() == True:
        if(mystr[x].isupper()):
            cu = True
        else:
            cl = True
        alp = True
    elif mystr[x].isdigit() == True:
        num = True
        
if(len(mystr) >= 8):
    strength += 1
if mystr.isalnum()!= True and mystr.isspace()!= True:
        strength += 1      
if(cu == True and cl == True):
    strength += 1
if(num == True and alp == True):
    strength += 1
    
print("Your password strength : ", strength)
    
    
