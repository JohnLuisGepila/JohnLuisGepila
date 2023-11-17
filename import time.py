from doctest import OutputChecker
import time




# Function to print text with a smile emoji
def print_with_smile(text):
    print("\U0001F600 " + text)

# Animated output using a loop with a time delay
def animate_output(text):
    for character in text:
        print_with_smile("\033[95m"(character))
        time.sleep(0.1)  # Adjust the time delay as needed

# Text to animate
text_to_animate = [
    "Please Enter Your Name:",
    "Please Enter Your Age:",
    "Please Enter Your Address:",
    "Good Day Mr/Ms -",
    "Your Age is -{age} years old",
    "You live at -{address}",
    OutputChecker
]

# Animating each line
for line in text_to_animate:
    animate_output(line)