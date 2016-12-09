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

<<<<<<< HEAD
my_expression = r"\w*(\w)\1\w*\1\w*"
=======
my_expression = r"a"
>>>>>>> 25790ef9f8a5bbe8b555c613243e91cdeb4147a8
print get_matching_words(my_expression)