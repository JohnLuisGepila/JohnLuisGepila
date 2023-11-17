from pyfiglet import Figlet

design = Figlet(font='slant', width=100)

name = input("What's your name?: ")
age = int(input("How old are you? "))
address = input("What's your address?: ")

output = f"Name: {name}, Age: {age}, Address: {address}"

print("\033[95m" + design.renderText("Good Day Mr/Ms -" + name))
print("\033[95m" + design.renderText("Your Age is -" + str(age) + " years old"))
print("\033[95m" + design.renderText("You live at -" + address))
print("\033[95m" + design.renderText (output))