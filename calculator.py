#calculator
#arithmatic operation
def add(a,b):
    c=a+b
    print("addition of two no. ",a,"&",b,"is",c)
def sub(a,b):
    c=a-b
    print("substration of two no.",a,"&",b,"is",c)
def mul(a,b):
    c=a*b
    print("multiplication of two no.",a,"&",b,"is",c)
def div(a,b):
    c=a/b
    print("division of two no.",a,"&",b,"is",c)
def mod(a,b):
    c=a%b
    print("remainder of ",a,"divided by",b,"is",c)    
def flrval(a,b):
    c=a*b
    print("floorvalue of two no.",a,"&",b,"is",c)
def power(a,b):
    c=a**b
    print(a,"to the power ",b,"is",c)      
  #relational operation
def relation(a,b):
    if (a==b) :
        print(a,"is equal to",b)
    else:
        print(a,"is not equal to",b)    
        if(a>b) :
             print(a,"greater than",b)      
        else:
             print(a,"is less than",b)  
#logical operation
def logic(a,b):
     c=a>10 and b<100
     d=a>10 or b<100
     e= not(a>10 and b<100)
     if( c== True):
         print(a,"&",b,"lies in between 10 to 100 ")
     if(d== True):
         print(a,"&",b," may lies in between 10 to 100 ")
     if(e== True):
         print(a,"&",b," donot lie in between 10 to 100 ")
 #bitwise operation
def  bit_and(a,b):
     e=a&b
     print("a & b",e)
def bit_or(a,b):
     d=a|b 
     print("a | b",d)
def bit_xor(a,b):
     x=a^b
     print("a ^ b",x)
def bitshiftleft(a,c):
     y=a>>c
     print(a,"shifted left by ",c,"zeros",y)
def bitshiftright(b,c):
     z=b<<c
     print(b,"shifted right by",c," zeros",z)    
#wrong choice
def invalid():
    print("Invalid choice")
#menu part program
print("\r Menu driven Calculator")     
print("\n press 0 for arithmatic operation \n press 1 for logical operation\n press 2 for bitwise operation \n press 3 for relational operation")
ch=int(input(" enter your choice:"))
#value for arithmatic part
if (ch==0):
     print("arithmatic operation is allowed")
     a=float(input("enter the first no."))
     b=float(input("enter the second no."))
     ch1=int(input("\npress 1 for addition\npress 2 for substraction\npress 3for multiplication\npress 4 for division\n press 5 for remainder\npress 6 for floorvalue\npress 7 for exponent\nenter ur choice:"))    
     if (ch1==1):
            add(a,b)
     elif(ch1==2):
            sub(a,b)
     elif(ch1==3):
            mul(a,b)
     elif(ch1==4):
            div(a,b)   
     elif(ch1==5):
            mod(a,b)
     elif(ch1==6):
            flrval(a,b)
     elif(ch1==7):
            power(a,b)
     else:invalid()
#value for logical part
elif(ch==1):
    print("logical operation is allowed")
    a=float(input("enter the 1st no. to check the range within 10 to 100"))
    b=float(input("enter the 2nd no. to check the range within 10 to 100"))
    logic(a,b)
#value for bitwise part    
elif(ch==2)    :
       print("bitwise operation is allowed")
       ch2=int(input("\npress 1 for bit and\npress 2 for bit or\npress 3 for bit xor\npress 4 for leftshift\npress 5 for right shift\nenter the choice:"))
       if(ch2==1):
             a=int(input("enter the first no."))
             b=int(input("enter the second no."))
             bit_and(a,b)
       elif(ch2==2):
             a=int(input("enter the first no."))
             b=int(input("enter the second no."))
             bit_or(a,b)
       elif(ch2==3):
             a=int(input("enter the first no."))
             b=int(input("enter the second no."))
             bit_xor(a,b)
       elif(ch2==4 or ch2==5):
             if(ch2==4):
                   a=int(input("enter the no."))
                   c=int(input("enter the shifting position "))
                   bitshiftleft(a,c)
             else:
                    b=int(input("enter the no."))
                    c=int(input("enter the shifting position "))
                    bitshiftright(b,c)
       else:invalid()
#value for relational part
elif(ch==3):
     print("relational operation is allowed")
     a=float(input("enter the first no."))
     b=float(input("enter the second no."))
     relation(a,b)
else:invalid()
#end of program

    

         
         
     
     
