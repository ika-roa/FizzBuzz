# FizzBuzz Kata

> TDD implementation of the FizzBuzz Kata

## General requirements:
- Write a program that prints the numbers from 1 to n. 
- For multiples of three print “Fizz” instead of the number.
- For the multiples of five print “Buzz” instead of the number. 
- For numbers which are multiples of both three and five print “FizzBuzz”.

## Important:
- Follow TDD best practices:
    - Write production code only to pass a failing unit test.
    - Write no more of a unit test than sufficient to fail (compilation failures are failures).
    - Write no more production code than necessary to pass the one failing unit test.
- Make code easily extensible with further rules.

## New requirements:
- For multiples of seven print "Woof" instead of the number
- If 3, 5 or 7 occur in the number (e.g. 13, 52, 17), also print replacement instead of number.
- If number is a square number, print "Bam"