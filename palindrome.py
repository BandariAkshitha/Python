n=int(input("Enter a number: "))
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n//=10
if rev==temp:
    print("Palindrome")
else:
    print("Not palindrome")
