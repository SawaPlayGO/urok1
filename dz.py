polindrom = "abcdefgh"
ne_polindrom = "Google"

def test_on_polindrom(word : str) -> bool:

    """
    Проверка на полиндром слитных слов
    """
    
    iteration = 0
    symbols = []

    for symbol in word:

        symbols.append(symbol)
        iteration += 1
    
    symbols = set(symbols)

    if len(symbols) == iteration:
        return True
    else:
        return False