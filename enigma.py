import numpy as np
import random
import copy

class Enigma:  

    ALFABETO = "abcdefghijklmnopqrstuvwxyz "

    def __init__(self, seed=42):
        
        self._seed = seed
        random.seed(seed)

        self.P = np.eye(27)
        random.shuffle(self.P)

        self.C = copy.deepcopy(self.P)
        random.shuffle(self.C)

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
        message = ""

        for col in one_hot_message.T:
            i = np.where(col == 1)[0][0]
            
            message += self.ALFABETO[i]
        
        return message


    def encrypt(self, message, P):
        pass

    def decrypt(self, message, P):
        pass

    def enigma(self, message, P, E):
        pass

    def de_enigma(self, message, P, E):
        pass


e = Enigma()
onehot = e.to_one_hot("piroca")
print(e.to_string(onehot))