#i = 0
numbers = []

def loop(num_times, increment):
    i = 0

    while i < num_times:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers is now: ", numbers)
        print(f"At the bottom i is {i}")

loop(7, 2)
print("The numbers: ")

for num in numbers:
    print(num)
