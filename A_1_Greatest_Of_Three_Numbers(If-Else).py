#Greatest_of_three_numbers (IF..ELSE)

a = int(input('Enter any number : '))

b = int(input('Enter any number : '))

c = int(input('Enter any number : '))

if   a > b and a > c : 
    print('the greatest value is ',a)
elif b > a and b > c : 
    print('the greatest value is ',b)    
elif c > a and c > b : 
    print('the greatest value is ',c)    
else :
    print('NOn of the value is greater')

