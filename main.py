meme_dict = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "ЛОЛ": "Что-то очень смешное",
    "РОФЛ": "шутка",
    "ЩИЩ": "одобрение или восторг",
    "КРИПОВЫЙ": "страшный, пугающий",
    "АГРИТЬСЯ": "злиться"
}

while True:
    word = input("Введите непонятное слово:")
    if word.lower() == 'стоп':
        break
    elif word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Извините мы не знаем такого слова")
