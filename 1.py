n=int(input("enter a four digit number : "))

if n<1000 or n>9999:
    print("invalid number only four digit number is acceptable")
    exit()

n1=n//1000
n2=(n//100)%10
n3=(n//10)%10
n4=n%10    

sum = n1+n2+n3+n4

rev = (n4 *1000) + (n3*100) + (n2*10) + n1

diff = (n1*n3) - (n2*n4)

print("the sum of each digit is : ",sum)
print('the reverse of the number is : ',rev)
print("thee difference between multiple of odd position and even position is : ",diff)

