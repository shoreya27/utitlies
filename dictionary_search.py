'''
Beautiful Dictionary Module,
Gives meaning of a word asked by the user.
'''
import requests



class DictionaryLord():
    '''
    I am a Dictionary lord
    I will bring meaning for a given 
    word from the magic url 
    Please demand meaning of any word
    '''

    URL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

    def __init__(self, word):
        self.word = word
        self.meaning = ""

    def _search_meaning(self):
        url      = self.URL + self.word

        response = requests.get(url=url)


        return response.json()
    
    def _get_meaning(self):
        data           = self._search_meaning()[0]["meanings"]
        part_of_speach = data[0]["partOfSpeech"]
        definition     = data[0]["definitions"][0]["definition"]
        
        self.meaning   = f"{self.word.capitalize()}.{part_of_speach.capitalize()}.{definition}"
    
    @property
    def word_meaning(self):
        self._get_meaning()
        return self.meaning

def main():

    word = input("Word? ")

    dict_lord = DictionaryLord(word = word)
    print(dict_lord.word_meaning)

main()