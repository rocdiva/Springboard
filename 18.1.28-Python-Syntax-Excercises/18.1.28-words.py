
"""
1. For a list of words, print out each word on a separate line, 
but in all uppercase. How can you change a word to uppercase? 
Ask Python for help on what you can do with strings!

2. Turn that into a function, ***print_upper_words***. Test it out. 
(Don’t forget to add a docstring to your function!)

3. Change that function so that it only prints words that start with 
the letter ‘e’ (either upper or lowercase).

4. Make your function more general: you should be able to pass in a 
set of letters, and it only prints words that start with one of those letters.

Breakdown


"""

# v1
# list_of_words = ["hey", "hello", "you", "yemen", "hawaii"]
# print(list_of_words)
# upper(list_of_words)

"""
I see there is an .upper method that will make a string uppercase
However, this is not a list
"""
# s = "hey hello you yemen hawaii"
# x = s.upper()
# print(x)

"""
Next iteration, iterate over the list:
Here I am iterating over the list
    im taking each word stored in the iterator and attaching the method .upper
    BUT, I am doing anything with it

for word in list_of_words: 
    print(word)
    word.upper()
"""

#1.
list_of_words= ["hey", "hello", "you", "yemen", "hawaii"]

for word in list_of_words: 
    #print(word)
    result = word.upper() # attach .upper method to each word
    print(result)


#2.

"""
Here, I had an extra elif block, not needed

def print_upper_words(word_list):
    -Print a list of words to uppercase-
    for word in word_list:
        if word.startswith("e"):
            result = word.upper() # attach .upper method to each word
            print(result)
        elif word.startswith("e") != "e":
           print("No more words that start with e")
print_upper_words(["echo", "hello", "either", "hey", "goodbye", "yo", "yes"])
"""

def print_upper_words(word_list):
    """Print a list of words to uppercase"""
    for word in word_list: 
        result = word.upper() # attach .upper method to each word
        print(result)
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

#3.
# Use In [5]: dir(str) to find a list of Attributes

def print_upper_words(word_list):
    """Print a list of words to uppercase"""
    for word in word_list:
        if word.startswith("e") or word.startswith("E"):
            result = word.upper() # attach .upper method to each word
            print(result)

print_upper_words(["echo", "Evelyn", "hello", "either", "hey", "goodbye", "your ", "yes"])

#4.
"""
I need to able to pass in a set of letters to the function at will
Dont have the letters baked in like:
    if word.startswith("e") or word.startswith("E"):

"""
def print_upper_words(word_list, must_have_letter):
    """Print a list of words to uppercase"""
    for word in word_list:
        if word[0].lower() in must_have_letter:
            result = word.upper()
            print(result)

print_upper_words(word_list = ["echo", "Evelyn", "hello", "either", "hey", "goodbye", "yo", "yes"], must_have_letter={'e', 'h', 'y'})
