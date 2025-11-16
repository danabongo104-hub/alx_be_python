pattern_size = int(input("Enter the size of the pattern: "))
size = 0
while size < pattern_size:
    for i in range(pattern_size):
        print("*", end=" ")
    print()
    size += 1
