import numpy as np
import random
import copy

class Enigma:  

    ALFABETO = "abcdefghijklmnopqrstuvwxyz "

    def __init__(self, seed=42):
        
        self._seed = seed
        np.random.seed(seed)

        self.P = np.eye(27)
        np.random.shuffle(self.P)

        self.E = copy.deepcopy(self.P)
        np.random.shuffle(self.E)


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
        return P @ message


    def decrypt(self, message, P):
        return np.linalg.inv(P) @ message


    def enigma(self, message):
        onehot = self.to_one_hot(message)

        encrypted_message = self.encrypt(onehot, self.P)

        for _ in range(len(message[0])):
            encrypted_message = self.encrypt(encrypted_message, self.E)
        
        print(encrypted_message)
        return self.to_string(encrypted_message)


    def de_enigma(self, message):
        onehot = self.to_one_hot(message)

        for _ in range(len(message[0])):
            onehot = self.decrypt(onehot, self.E)
        
        decrypted_message = self.decrypt(onehot, self.P)

        return self.to_string(decrypted_message)



e = Enigma()
m = "o tiago eh legal"

#print(e.P)

mc = e.enigma(m)
print(mc)

print(e.de_enigma(mc))