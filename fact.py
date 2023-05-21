num=int(input("Enter value for factorial:"))
if num>=0:
   print("Number enter by user is positive")
else:
   print("Number enter by user is negative")
i=1
fact=1
while i<=num:
    fact=fact*i
    i+=1
print("Factorial:",fact)

