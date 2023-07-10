#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    if length >= 1:
        fibonacci_list.append(0)
    if length >= 2:
        fibonacci_list.append(1)
    
    for i in range(2, length):
        next_fibonacci = fibonacci_list[i - 1] + fibonacci_list[i - 2]
        fibonacci_list.append(next_fibonacci)
    
    print(fibonacci_list)