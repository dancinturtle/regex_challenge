# Jenny and Kunal
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

problem1 = r"ss"
print get_matching_words(problem1)

problem2 = r"b.b"
print get_matching_words(problem2)

problem3 = r"b.+b"
# print get_matching_words(problem3)

problem4 = r"b.*b"
print get_matching_words(problem4)

problem5 = r"b.?b"
print get_matching_words(problem5)

problem6 = r"a.*e.*i.*o.*u"
print get_matching_words(problem6)

problem7 = r"\b.*[aeiou]{2}\b"
print get_matching_words(problem7)

problem8 = r"^[regular expression]+$"
print get_matching_words(problem8)

problem9 = r"^[^regex]+$"
print get_matching_words(problem9)

problem10 = r"\b\w*?(\w{2})\w*?\1\w?\b"
print get_matching_words(problem10)
