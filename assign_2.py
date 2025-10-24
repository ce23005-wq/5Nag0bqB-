text ="welcome to python programming"
print(text)


# if statement section
if "c++" in text:
    print("The word 'c++' is found in the text.")
else:
    print("The word 'c++' is not found in the text.")

print("Length of the text:", len(text))

# for loop section
print("\n")
for i in range(len(text)):
    print(f"Character at index {i}: {text[i]}")

print("\n\n")


# while loop section
secret_word = "python"
attempts = 0    
while attempts < 5:
    user_input = input("Guess the secret word: ")
    attempts += 1
    if user_input == secret_word:
        print("Congratulations! You've guessed the secret word.")
        break
    else:
        print("Incorrect guess. Try again.")

