# If number inside of a range is divisible by 3 print Fizz
# If number inside of a range is divisible by 5 print Buzz
# If number inside of a range is divisible by 5 and 3 print FizzBuzz
# If number is not divisible return the number itself


# SOLUTION:


for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print ('Fizz')
    elif num % 5 == 0:
        print ('Buzz')

    else:
        print (num)