#!/usr/bin/env py
# write your code here
def main():
    interactive_greet()

def greet(name):
    return f"Hello, {name}!"

def interactive_greet():
    name = input("What is your name?")
    print(greet(name))

if __name__ == '__main__':
    main()