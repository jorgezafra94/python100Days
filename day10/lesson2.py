"""
we can return more than one value in a function
"""


def handle_connection(url):
    if "http" in url and "https" not in url:
        return "sorry the url is not secure!!"
    else:
        create_connection = url + "/home"
        final_url = create_connection + ".html"
        return final_url


test1 = handle_connection("http://www.google.com")
print(test1)

test2 = handle_connection("https://wwww.facebook.com")
print(test2)

print()
def returning_two_values(phrase):
    list_words = phrase.split(" ")
    first = list_words[0]
    last = list_words[-1]
    return first, last


one, two = returning_two_values("Hello there how are you?")
print(one)
print(two)
