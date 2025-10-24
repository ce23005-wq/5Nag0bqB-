import numpy as np
np.random.seed(42)

#numpy array section
grade_array = np.random.randint(0, 101, size=15)
print("Generated grades array:\n", grade_array)
print("\n") 
reshaped_array = grade_array.reshape(3, 5)
print("Reshaped grades array (3x5):\n", reshaped_array) 
print("\n")
print("Letter grades for each grade:")
for grade in grade_array:   
    if grade >= 90:
        print(f"{grade} is A")
    elif grade >= 80:
        print(f"{grade} is B")
    elif grade >= 70:
        print(f"{grade} is C")
    elif grade >= 60:
        print(f"{grade} is D")
    else:
        print(f"{grade} is F")

print("\n")

#function to add two numbers
def add_numbers(a, b):
    result = a + b
    print("The sum is:", result)

# Call the function
add_numbers(5, 10)


