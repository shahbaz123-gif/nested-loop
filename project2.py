n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * i)