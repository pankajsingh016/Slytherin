# Program to see whether a Number is Prime or Not

n = int(input("Enter a Number"))   # Taking Input form the User
k=1
flag =0
while n>k:
    if n%k==0:                     # Condition to check for Prime
        flag+=1
    k+=1
if flag==1:
    print("Prime Number\n")        # Now Printing Output According to the User
else:
    print("Not a Prime Numeber\n")


