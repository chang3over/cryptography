import random


class Caesar:
    alfabet = ""

    def __init__(self, alfabet):
        self.alfabet = alfabet

    def modulo_value(self, number, modul):
        return number % modul

    def encrypt(self, text):
        pass

    def update_alfabet_random(self):
        random.shuffle(self.alfabet)
