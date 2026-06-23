'''
Problem Description: You are given an integer n. 
Your task is to printa square pattern of size n x n made up of
the character '*', represented as a list of strings.
'''

def pattern(n):
    for i in range (n):
        print("* "*n, end ="\n")

n=int(input("Enter number: "))
pattern(n)