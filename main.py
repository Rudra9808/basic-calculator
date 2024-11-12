a= input("What is your first number: ")
b= input("What is your second number:")
c= input("What do you want to do(+,-,*,/)")
if(c== "*"):
    print(int(a)*int(b))

elif(c== "+"):
    print(int(a)+int(b))
    
elif(c== "-"):
    print(int(a)-int(b))
else:
    print(int(a)/int(b))
