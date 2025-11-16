number = int(input("Enter a number to see it's multiplication table: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")