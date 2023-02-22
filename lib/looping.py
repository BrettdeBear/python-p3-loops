#!/usr/bin/env python3

def happy_new_year():
   counter = 10
   while counter > 0:
       print(counter)
       counter = counter - 1
   print("Happy New Year!")

def square_integers(int_list):
    square_list = [number * number for number in int_list]
    return square_list


def fizzbuzz():
    for i in range(100):
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
