userInput = input("please enter a character: ")
sentence  = "the quick brown fox jumps over the lazy dog"

count = 0
for i in sentence:
    if userInput == i:
        count += 1

print("Your input was in the sentence ", count, "times")
