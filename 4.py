def is_happy_number(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return n == 1

def check_happy_number(number):
    
    if is_happy_number(number):
        print(f"{number} is a happy number!")
    else:
        print(f"{number} is not a happy number.")

def print_happy_numbers_in_range():
    print(f"Happy numbers  under {100}:")
    for num in range(0, 100 + 1):
        if is_happy_number(num):
            print(num)

def print_first_n_happy_numbers(N):
    count = 0
    num = 1
    print(f"First {N} happy numbers:")
    
    while count < N:
        if is_happy_number(num):
            print(num)
            count += 1
        num += 1

number = int(input("Enter a number to check if it is a happy number: "))
x = int(input("Enter how many happy numbers should be printed: "))
check_happy_number(number)
print_first_n_happy_numbers(x)
print_happy_numbers_in_range()
