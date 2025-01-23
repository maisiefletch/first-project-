with open("students.txt", "w") as file:
 
    file.write("Lida\n","101\n")
    file.write("Tara,5\n")
    file.write("Allessandro,12\n")
    file.write("Rafael,46\n")
    file.write("Oli,34\n")
    file.write("Aaron,21\n")
    file.write("Jolie,76\n")
    file.write("Maisie,90\n")
    file.write("Ollie,65\n")
    file.write("Harry,46\n")
    file.write("Ken,83\n")
    file.write("Bayne,99\n")
    file.write("Leila,96\n")
    file.write("Amelia,67\n")
    file.write("Selma,75\n")
    file.write("Sofi\n")
    file.write("Tao\n")
    file.write("Marlee\n")
    file.write("Layla\n")
    file.write("Ben\n")
    file.write("Letlotlo\n")
    file.write("Bram\n")
    file.write("Joseph\n")
    file.write("Bella\n")
    file.write("Axel\n")
 
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
