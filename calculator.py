#calculator
#arithmatic operation
x=1
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
    c=a//b
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
     print(a,"shifted left by ",c,"zeros and val is ",y)
def bitshiftright(b,c):
     z=b<<c
     print(b,"shifted right by",c," zeros and val is ",z)    
def ext():
    x=0
    print("calculator is commanded to exit")
    exit()
#wrong choice
def invalid():
    print("Invalid choice\nplease put the choice as stated\n")
#menu part program
print("\t Menu driven Calculator\n")     
while (x==1):    
     ch=int(input(" press 1 for arithmatic operation \n press 2 for logical operation\n press 3 for bitwise operation \n press 4 for relational operation\n press 0 for exit\n\nenter your choice:"))
#value for arithmatic part
     if(ch==1):         
         ch1=int(input("\tarithmatic operation is allowed\n\npress 1 for addition\npress 2 for substraction\npress 3 for multiplication\npress 4 for division\npress 5 for remainder\npress 6 for floorvalue\npress 7 for exponent\n\nenter ur choice:"))    
         if (ch1==1):
                add(a=float(input("enter the first no.")),b=float(input("enter the second no.")) )
         elif(ch1==2):
                    sub(a=float(input("enter the first no.")) ,b=float(input("enter the second no. to be deducted")) )
         elif(ch1==3):
                    mul(a=float(input("enter the first no.")) ,b=float(input("enter the second no. to be multiplied")) )
         elif(ch1==4):
                    div(a=float(input("enter the dividend")) ,b=float(input("enter the divisor")) )   
         elif(ch1==5):
                    mod(a=float(input("enter the dividend")) ,b=float(input("enter the divisor")) )
         elif(ch1==6):
                    flrval(a=float(input("enter the dividend")) ,b=float(input("enter the divisor")) )
         elif(ch1==7):
                    power(a=float(input("enter the  no.")) ,b=float(input("enter the power")))
         else:invalid()
#value for logical part
     elif(ch==2):          
           print("\tlogical operation is allowed\n")
           logic(a=float(input("enter the 1st no. to check the range within 10 to 100 ")),b=float(input("enter the 2nd no. to check the range within 10 to 100 ")))
#value for bitwise part    
     elif(ch==3)    :
            ch2=int(input("\tbitwise operation is allowed\n\npress 1 for bit and\npress 2 for bit or\npress 3 for bit xor\npress 4 for leftshift\npress 5 for right shift\n\nenter the choice:"))
            if(ch2==1):
                 bit_and(a=float(input("enter the first no.")) ,b=float(input("enter the second no.")) )
            elif(ch2==2):
                 bit_or(a=float(input("enter the first no.")) ,b=float(input("enter the second no.")) )
            elif(ch2==3):
                 bit_xor(a=float(input("enter the first no.")) ,b=float(input("enter the second no.")) )
            elif(ch2==4):
                 bitshiftleft(a=int(input("enter the no.")) ,c=int(input("enter the left shifting position ")))
            elif(ch2==5):          
                 bitshiftright(b=int(input("enter the no.")) ,c=int(input("enter the right shifting position "))) 
            else:invalid()
#value for relational part
     elif(ch==4):        
         print("\trelational operation is allowed\n")
         relation(a=float(input("enter the first no.:")) ,b=float(input("enter the second no.:")) )
#exit condition
     elif(ch==0):
         ext()
#invalid condition
     else:invalid()
#end of program
