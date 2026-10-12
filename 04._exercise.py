#Exercise

##The Fizz Buzz challenge. 
# Write a program that prints the numbers from 1 to 100 
# for multiples of 3 print Fizz instead of the number and for the multiples of 5 print Buzz. 
# If it is divisible by both, print FizzBuzz. So the output should be something like below

### 1, 2, Fizz, 4, Buzz, Fizz ... 13, 14, FizzBuzz, ...

### Breaking down the problem further, we need to create for-loop with following conditions



'''If the number is a multiple of both 3 and 5 (i.e. 15), print FizzBuzz
If the number is multiple of 3, print Fizz
If the number is multiple of 5, print Buzz
Otherwise print the number
'''

for num in range(1,100):

    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz', num)
    elif num % 3 == 0:
        print('Fizz', num)
    elif num % 5 == 0:
        print('Buzz', num)
    else:
        print(num)