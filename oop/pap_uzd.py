# Sukurti klasę, kurioje atributas butu "text".
#
# Sukurti metodus, kurie:
#   1. Suskaičiuotų kiek yra žodžių tekste;
#   2. Metoda, kuris gražintų visus žodžius, kurie būtų nurodyti metodo kintamajame.
#   Pvz nurodytos raidės 'ams', turi išrinkti visus žodžius, kurie turis šias raides.
#   3. Išrinktų visus žožius, kurių ilgis didesnis arba lygus nurodytam metode;
#

class Text:

    def __init__(self, text: str):
        self.text = text

    def counting(self):
        return len(self.text.split())

    def search_letters(self, letters):
        words_with_letters = []
        for word in self.text.split():
            for letter in letters:
                if letter in word:
                    words_with_letters.append(word)
                    break
        return words_with_letters

    def found_counting_results(self, length):
        words_with_length = []
        for word in self.text.split():
            if len(word) >= length:
                words_with_length.append(word)
        return words_with_length


text = Text("""Kauno „Žalgirio“ komanda yra arti susitarimo
 su Andrea Trinchieri dėl kontrakto pratęsimo,
  skelbia basketnews.lt žurnalistas Donatas Urbonas.""")

letters = 'amc'
length = 5

print(text.counting(), 'žodžių skaičiavimas')
print(text.search_letters(letters), 'raidžių ieškojimas')
print(text.found_counting_results(length), 'bent penkių raidžių žodžiai')


# Vik.Versija

class Text:
    def __init__(self, text: str):
        self.text = text

    def split_text(self):
        return self.text.split()

    def count_words(self) -> int:
        return len(self.split_text())

    def return_words_with_letters(self, letters: str ='ams') -> list:
        result = []
        for word in self.split_text():
            if all(letter in word for letter in letters):
                result.append(word)
        return result

    def return_longer_than_number(self, number: int = 5) -> list:
        return [word for word in self.split_text() if len(word) > number]