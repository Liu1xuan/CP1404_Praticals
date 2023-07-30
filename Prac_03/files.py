# program 1
OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, "w")
name = str(input("What is your name? "))
print(name, file=out_file)
out_file.close()

# program 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# program 3

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())

in_file.close()
print(number1+number2)

# program 4
IN_FILE = "numbers.txt"

in_file = open("numbers.txt", "r")
total = 0
for line in IN_FILE:
    number = int(line)
    total += number

in_file.close()
print(total)



