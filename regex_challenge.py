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

my_expression = r"a"
print get_matching_words(my_expression)

my_expression = r"ss"
print get_matching_words(my_expression)

my_expression = r"b.b."
print get_matching_words(my_expression)

my_expression = r"b.+b"
print get_matching_words(my_expression)

my_expression = r"b.*b"
print get_matching_words(my_expression)

my_expression = r"b.?b"
print get_matching_words(my_expression)

my_expression = r"a.*e.*i.*o.*u"
print get_matching_words(my_expression)

my_expression = r"[aeiou]{2}$"
print get_matching_words(my_expression)

my_expression = r"^[regular expression]*$"
print get_matching_words(my_expression)

my_expression = r"^[^regex]*$"
print get_matching_words(my_expression)

my_expression = r"\b\w*(\w{2})\w*\1"
print get_matching_words(my_expression)
