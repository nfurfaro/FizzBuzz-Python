# fizzbuzz.py
def fizzle():
    num = int(input("Enter a number between 0 - 1000: "))
    while num <= 0 or num >= 1000:
        print("Sorry, try again.")
        num = int(input("Enter a number between 0 - 1000: "))
    if num % 3 == 0 and num % 2 == 0:
        print("Fizz Buzz")
    elif num % 2 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

fizzle()