rev=0
n=int(input("Enter a number to be checked : "))
num=n
while num!=0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
pal=rev
if(pal==n):
    print("The given number is a palindrome number")
else:
    print("The given number is not a palindrome number")

print("Press enter to exit")

    
