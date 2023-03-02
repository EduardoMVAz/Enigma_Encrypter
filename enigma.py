import numpy as np
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


    def encrypt(self, message, idx):
        message = np.array([message]).T
        message = self.P @ message

        for _ in range(idx):
            message = self.E @ message

        return message


    def decrypt(self, message, idx):
        message = np.array([message]).T

        for _ in range(idx):
            message = np.linalg.inv(self.E) @ message

        message = np.linalg.inv(self.P) @ message

        return message


    def enigma(self, message):
        onehot = self.to_one_hot(message)

        encrypted_message = np.empty((27, 0))

        for i in range(onehot.shape[1]):
           encrypted_message = np.concatenate((encrypted_message, self.encrypt(onehot[:,i].T, i)), axis=1)
        
        return self.to_string(encrypted_message)


    def de_enigma(self, message):
        onehot = self.to_one_hot(message)

        decrypted_message = np.empty((27, 0))

        for i in range(onehot.shape[1]):
           decrypted_message = np.concatenate((decrypted_message, self.decrypt(onehot[:,i].T, i)), axis=1)
        
        return self.to_string(decrypted_message)



e = Enigma(22)
m = "o tiago eh legal"

mc = e.enigma(m)
print(mc)
print(e.de_enigma(mc))