name = 'William K. Carlson'
age = 38 # not a lie
height = 73 # inches
metric_height = height * 2.54
weight = 165 # lbs
metric_weight = weight * .453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches, or {metric_height} centimeters tall.")
print(f"He's {weight} pounds, or {metric_weight} kilograms heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
