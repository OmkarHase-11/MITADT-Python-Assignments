# 1. Basic open() syntax
file = open("filename.txt", "r")
file.close()


# 2. Opening a file in read mode
f = open("geek.txt", "r")
print(f)
f.close()


# 3. Opening and closing a file
file = open("geek.txt", "r")

# Perform file operations

file.close()


# 4. Checking file properties
f = open("geek.txt", "r")

print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()

print("Is Closed?", f.closed)


# 5. Reading a file using read()
file = open("geek.txt", "r")

content = file.read()

print(content)

file.close()


# 6. Writing to a file using write()
with open("geek.txt", "w") as file:
    file.write("Hello, Omkar Hase!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")


# 7. Reading a file using with statement
with open("geek.txt", "r") as file:
    content = file.read()
    print(content)


# 8. Handling file closing using try and finally
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)

finally:
    file.close()
