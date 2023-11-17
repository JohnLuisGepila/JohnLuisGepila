from pyfiglet import Figlet

design = Figlet(font='standard', width=105)

def print_with_smile(text):
    print("\U0001F600 " + text)

print_with_smile("\033[95m" + design.renderText("Please Enter Your Name:"))
name = input()

print_with_smile("\033[95m" + design.renderText("Please Enter Your Age:"))
age = (input())

print_with_smile("\033[95m" + design.renderText("Please Enter Your Address:"))
address = input()

output = f"Name: {name}, Age: {age}, Address: {address}"

print_with_smile("\033[95m" + design.renderText("Good Day Mr/Ms -" + name))
print_with_smile("\033[95m" + design.renderText("Your Age is -" + str(age) + " years old"))
print_with_smile("\033[95m" + design.renderText("You live at -" + address))
print_with_smile("\033[95m" + design.renderText(output))
