from Dice import Die
import matplotlib.pyplot as plt
import numpy as np

# Gets user inputs for number of dice to roll & how many sides they have
# Throws out non-integer responses
while True:
    try:
        num_die = int(input("How many die do you want to roll? "))
        break
    except ValueError:
        print("Please enter a number.")

while True:
    try:
        num_sides = int(input("How many sides should each die have (max 20)? "))
        if num_sides > 20:
            print("Pick a number less than 20.")
            continue
        break
    except ValueError:
        print("Please enter a number.")

# Creates die object, rolls it, and adds the value to a list
rolls = []
for num in range(num_die):
    die = Die(num_sides)
    roll = die.roll()
    rolls.append(roll)


# Counts each value in rolls & adds to list
frequencies = []
for value in range(1, num_sides+1):
    frequency = rolls.count(value)
    frequencies.append(frequency)

print(frequencies)

# Creates a formatted bar chart
x_values = list(range(1, num_sides+1))
plt.ylim(0, max(frequencies)+(max(frequencies)*0.1))
plt.xticks(np.arange(1, num_sides+1, step=1))
plt.bar(x_values, frequencies, color='blue')
for i, v in enumerate(frequencies):
    plt.text(i + .8, v + .25, str(v), color='blue')
plt.show()
