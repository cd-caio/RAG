from unidecode import unidecode

class TextNormalizer():
    def __init__(self) -> None:
        pass

    def normalize(self, text:str):
        text = text.lower()
        text = unidecode(text)
        text = text.strip()
        text = ' '.join(text.split())
        text = text.replace("ç", "c")
        text = text.replace("-", "")
        text = text.replace("...", "")
        return text
    
if __name__ == "__main__":
    obj = TextNormalizer()
    result = obj.normalize("Olá     Gostaria de um pão doçe")
    print(result)