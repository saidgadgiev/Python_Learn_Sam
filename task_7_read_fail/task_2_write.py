# Запишем
print("Creating a text file using the method write().")
text_file = open("write_it.txt", "w", encoding="utf-8")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("This line got the number 3\n")
text_file.close()

print("\nI am reading a newly created file")
text_file = open("write_it.txt", "r", encoding="utf-8")
print(text_file.read())
text_file.close()

print("\nCreating a text file using the method writlines()")
text_file = open("write_it.txt", "w", encoding="utf-8")
lines = ["Line1\n",
         "This is line 2\n",
         "This line got the number 3\n"]
text_file.writelines(lines)
text_file.close()

print("\nI am reading a newly created file")
text_file = open("write_it.txt", "r", encoding="utf-8")
print(text_file.read())
text_file.close()
