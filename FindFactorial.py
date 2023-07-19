def FindFactorial(num):
    if num<=1:
        return 1
    return num*FindFactorial(num-1)
if __name__ == '__main__':
    num=int(input())
    print(FindFactorial(num))
"""
Write a program to find the factorial of the given number A using recursion.

Note: The factorial of a number N is defined as the product of the numbers from 1 to N.
"""