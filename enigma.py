import numpy as np

class EnigmaEncrypter:  

    ALFABETO = "abcdefghijklmnopqrstuvwxyz "

    def __init__(self):
        pass

    def to_one_hot(self, message):
        one_hot_message = np.empty((27, 0))
        for letter in message.lower():
            matriz = [[0] for i in range(27)]

            i = self.ALFABETO.find(letter)

            matriz[i] = [1]

            one_hot_message = np.concatenate((one_hot_message, matriz), axis=1)

        one_hot_message = np.array(one_hot_message)
        return one_hot_message

    def to_string(self, one_hot_message):
        pass

    def encrypt(self, message, P):
        pass

    def decrypt(self, message, P):
        pass

    def enigma(self, message, P, E):
        pass

    def de_enigma(self, message, P, E):
        pass