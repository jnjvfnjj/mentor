text = input('введите текст: ')

def count_text(text):
    words = text.split()
    count_words = set(words)
    print(len(count_words))

count_text(text)

