import re

def get_matching_words(regex):
    results = []
    words = [
        "baby",
        "baseball",
        "denver",
        "facetious",
        "issue",
        "mattress",
        "obsessive",
        "paranoia",
        "rabble",
        "union",
        "volleyball",
    ]
    for word in words:
        if re.search(regex, word):
            results.append(word)

    return results

my_expression = r'ss'
#Matches the literal "ss"

my_expression = r'b.b'
#"." matches any character except for the new line, so this looks for a word with a "b", any character, then another "b"

my_expression = r'b.+b'
#"+" is a wildcard character meaning "one or more times", so this looks for a "b", one or more characters, then another "b".

my_expression = r'b.*b'
# "*" is like "+", but it means "zero or more times". This looks for a "b", any number of characters (including none), then another "b"

my_expression = r'b.?b'
# "?" means that the preceeding character is matched 0 to 1 times, for example "."

my_expression = r'a.*e.*i.*o.*u.*'
#This pattern matches a word that has all five vowels in order, regardless of how many letters are or are not between them

# my_expression = r'[aeiou]{2}$'
# print get_matching_words(my_expression)

my_expression = r'^[regularexpression]+$'
#This pattern includes both "^" and "$", so it will only match full words. It looks for words consisting of one or more letters from "regular expression"

my_expression = r'^[^regex]+$'
#Annoyingly, "^" means two different things; inside a character class, it stands for "not", so this will match words that don't have any of the letters from "regex"

my_expression = r'^.*(\w{2}).*\1$'
#This matches any word where the double-letter appears twice
print get_matching_words(my_expression)
