import asyncio
from tabulate import tabulate
from googletrans import Translator

class TranslateClass:
    def __init__(self, word, lang):
        self.word = word
        self.lang = lang
        self.translator = Translator()

    async def translate(self):
        result = await self.translator.translate(self.word, dest=self.lang)
        data = [
            ['Language:', "Word/Sentence"],
            ['English', self.word],
            ['Spanish', result.text]
        ]
        return tabulate(data, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    word = input("Enter Word/Sentence: ")
    language = "es"
    translator = TranslateClass(word, language)
    translated_table = asyncio.run(translator.translate())
    print(translated_table)
