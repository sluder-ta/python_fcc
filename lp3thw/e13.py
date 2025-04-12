from sys import argv

script, first, second, third = argv

print("the script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

user_input = input("What's your favorite color? ")
print(f"Your favorite color is {user_input}.")