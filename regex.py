
# regex assignment
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

# my_expression = 
print get_matching_words(r"a")



# What would our output be for this example? Predict the following:
# r"v" => [denver, obsessive, volleyball]
print get_matching_words(r"v")
# r"^[aeiou]" => [issue, obsessive, union]
print get_matching_words(r"^[aeiou]")
# r"(\w)\1" => (matches any alphanumeric character and the underscore) and \1  matches the results of the first capture group - therefore this regex matches 2 consecutive characters. => [baseball, issue, mattress, obsessive, rabble, volleyball]
print get_matching_words(r"(\w)\1")


# Write regular expressions that will produce the following output, and use the above code to test your regex:
# ['issue', 'mattress', 'obsessive']
# Hint: Matches the literal "ss"
print get_matching_words(r"ss")

# ['baby']
# Hint: "." matches any character except for the new line, so this looks for a word with a "b", any character, then another "b"
print get_matching_words(r"b.b")

# ['baby', 'baseball']
# Hint: "+" is a wildcard character meaning "one or more times", so this looks for a "b", one or more characters, then another "b". All of the wildcard characters (and the next few problems cover more) apply to the one character immediately in front of them (so then is any number of "."s, not any number of "b."s)
print get_matching_words(r"b.+b")

# ['baby', 'baseball', 'rabble']
# Hint: "*" is like "+", but it means "zero or more times". This looks for a "b", any number of characters (including none), then another "b"
print get_matching_words(r"b.*b")

# ['baby', 'rabble']
# Hint: "?" means that the preceeding character is matched 0 to 1 times, for example "."
print get_matching_words(r"b.?b")

# ['facetious']
# Hint: This pattern matches a word that has all five vowels in order, regardless of how many letters are or are not between them
print get_matching_words(r"a.*e.*i.*o.*u")

# ['issue', 'paranoia']
# Hint: Curly braces mean the pattern repeats that many times, so this is words that end with two vowels
print get_matching_words(r"[aeiou]{2}$")

# ['issue', 'paranoia', 'union']
# Hint: This pattern includes both "^" and "$", so it will only match full words. It looks for words consisting of one or more letters from "regular expression"
# print get_matching_words(r"[aeiou]{2,}.*")
print get_matching_words(r"^[regulaexpsion]+$")

# ['baby', 'union']
# Hint: Annoyingly, "^" means two different things; inside a character class, it stands for "not", so this will match words that don't have any of the letters from "regex"
print get_matching_words(r"^[^regex]+$")

# ['volleyball']
# Hint: This matches any word where the double-letter appears twice
print get_matching_words(r"ll.+ll")
