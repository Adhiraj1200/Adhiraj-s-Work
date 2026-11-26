def function(empty_string):
    empty_string = ("")     
    for x in word:
        if x != letter:
            empty_string = empty_string + x
    return (empty_string)
empty_string = ("")    
word = input("Enter a word:")
letter = input("Enter a letter you want to take out of the word:")
value = function(empty_string)
print("Removed",letter,":",value)