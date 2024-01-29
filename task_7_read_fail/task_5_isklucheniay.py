try:
    num = float(input("Enter a number: "))
except ValueError as k:
    print("It looks like it's not a number!")
    print(k)
else:
    print("Yor enter number ", num)
# num = float(input("Enter a number: "))
