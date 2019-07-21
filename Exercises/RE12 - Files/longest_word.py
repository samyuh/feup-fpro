import urllib.request

def longest_word(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    words = html.split()

    lista = []
    length = 0
    longest = ""
    with open("words", "r") as f:
        doc = f.readlines()
        for line in doc:
            lista += line.split()
        wordset = set(lista)
        print(wordset)
        for word in words:
            if word in wordset:
                if len(word) > length:
                    length = len(word)
                    longest = word
    return longest