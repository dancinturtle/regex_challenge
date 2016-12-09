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

# Group : Joe and Daniel

ex_1= r"ss"
print get_matching_words(ex_1)

ex_2=r"b.b"
print get_matching_words(ex_2)

ex_3=r"b.+b"
print get_matching_words(ex_3)

ex_4=r"b.*b"
print get_matching_words(ex_4)

ex_5=r"b.?b"
print get_matching_words(ex_5)

ex_6=r"a.*e.*i.*o.*u"
print get_matching_words(ex_6)

ex_7=r"[aeiou]{2}$"
print get_matching_words(ex_7)

ex_8=r"^[regularexpression]+$"
print get_matching_words(ex_8)

ex_9=r"^[^\p{regex}]+$"
print get_matching_words(ex_9)

ex_10=r"([a-z])\1.+\1\1"
print get_matching_words(ex_10)
