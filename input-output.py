#!/usr/bin/python3
def hello_funktion():
    msg = "Hello, %s. How are you?"
    name = input('What is your name, human?:  --> ')
    print(msg % name)
hello_funktion()
