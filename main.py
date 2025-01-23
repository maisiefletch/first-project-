with open("students.txt", "w") as file:
 
 
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
        print(line[1])
 
new_line = input("Enter a new name:")
 
with open("students.txt", "a") as file:
    file.write(new_line + "\n")
 
with open("students.txt", "r") as file:
    for line in file:
        print(line.split(",",1)[0].strip())
 
with open("students.txt", "r") as file:
    for line in file:
        if len(line)>6:
            print(line)
