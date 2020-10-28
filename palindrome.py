#alotting a variable value so as to avoid default value.
rev=0
#storing the input as int datatype given by user in a variable.
n=int(input("Enter a number to be checked : "))
#now store the value of n in another variable.
num=n
#now using while loop check the condition if true then pursue further.
while num!=0:
 #following sequences of 3 lines are the logic of checking the digits.
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
#finally storing the outcome in a variable.
pal=rev
#here below we are checking is the outcome from while loop and the given input is equal or not.
if(pal==n):
    print("The given number is a palindrome number")
else:
    print("The given number is not a palindrome number")
#end of code.
