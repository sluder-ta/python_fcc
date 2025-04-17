# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i += 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#     print(num)

def count_by(start, increment):
    i = start
    numbers = []

    while i < 101:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
    print("The numbers: ")

    for num in numbers:
        print(num)

start = int(input("What number should we begin with? ")) or 1
increment = int(input("What should we count by? ")) or 1
count_by(start, increment)