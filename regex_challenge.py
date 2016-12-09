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

# my_expression = r"\w*(\w{2})\w*\1"
my_expression = r"(.)\1.*(.)\1"
# my_expression = r"b.?b"



print get_matching_words(my_expression)
