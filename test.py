#!/usr/bin/python3
def hello(name="user"):
	print("Hello {}".format(name))
def goodbye(name="user"):
	print("Goodbye {}".format(name))
def nameLength(name="user"):
	print("Your name is {} characters long".format(len(name)))
def backwards(name="user"):
	print("{} is how you spell your name backwards".format(name[::-1]))
if __name__ =="__main__":
	hello()
