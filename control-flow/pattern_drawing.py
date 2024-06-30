size = int(input("Enter the size of the pattern: "))
i = 1
while i <= size :
    for num in range(size):
        print("*", end="")
    i += 1
    print()
