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

print get_matching_words(r'ss') #any words with consecutive 'ss'
print get_matching_words(r'b.b') #one character between b's
print get_matching_words(r'b.+b') #one character one or more times between b's
print get_matching_words(r'b.*b') #one character 0 or more times between b's
print get_matching_words(r'b.?b') #one character 0 or 1 times between b's
print get_matching_words(r'a.*e.*i.*o.*u') #catches words that has all 5 vowels in order
print get_matching_words(r'[a.*e.*i.*o.*u]{2}$') #catches words that end in two vowels
print get_matching_words(r'^[regularexpression]+$') #catches words with one or more letters from "regular expresion"
print get_matching_words(r'^[^regex]+$') #catches words that do not contain any letters from "regex"
print get_matching_words(r'(\w)\1.*(\w)\1') #catches any double characters twice ex: ll bb
print get_matching_words(r'^.*(\w{2}).*\1$') #catches any double characters twice of the same character ex: ll ll


