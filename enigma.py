import numpy as np
import random
import copy

class Enigma:  

    def __init__(self, seed=42):
        
        self._seed = seed
        random.seed(seed)

        self.P = np.eye(27)
        random.shuffle(self.P)

        self.C = copy.deepcopy(self.P)
        random.shuffle(self.C)

    def to_one_hot(self, message):
        pass

    def to_string(self, one_hot_message):
        message = ""

        for col in one_hot_message.T:
            pass


    def encrypt(self, message, P):
        pass

    def decrypt(self, message, P):
        pass

    def enigma(self, message, P, E):
        pass

    def de_enigma(self, message, P, E):
        pass