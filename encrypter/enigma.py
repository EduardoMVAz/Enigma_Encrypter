import numpy as np
import copy

class Enigma:  
    '''
    Class that implements the Enigma encryption algorithm.

    '''

    # This is the only accepted alphabet and must not be altered.
    ALFABETO = "abcdefghijklmnopqrstuvwxyz "

    def __init__(self, seed=42):
        
        # Sets the seed
        self._seed = seed
        np.random.seed(seed)

        # Creates the permutation matrix P
        self.P = np.eye(27)
        np.random.shuffle(self.P)

        # Creates the encryption matrix E from P
        self.E = copy.deepcopy(self.P)
        np.random.shuffle(self.E)


    def to_one_hot(self, message):
        '''
        Converts a string to a one-hot matrix.

        @param message: string to be converted.
        @return: one-hot matrix (shape = len(message) columns by 27 rows).

        '''

        # Creates empty matrix where the one-hot message will be stored.
        one_hot_message = np.empty((27, 0))

        # For each letter in the message, finds its index in the alphabet and sets the corresponding row to 1.
        for letter in message.lower():
            matriz = [[0] for i in range(27)]

            i = self.ALFABETO.find(letter)

            matriz[i] = [1]

            one_hot_message = np.concatenate((one_hot_message, matriz), axis=1)

        one_hot_message = np.array(one_hot_message)

        return one_hot_message


    def to_string(self, one_hot_message):
        '''
        Converts a one-hot matrix to a string.
        
        @param one_hot_message: one-hot matrix to be converted.
        @return: string

        '''
        message = ""

        # For each column in the one-hot matrix, finds the index of the 1 and adds the corresponding letter to the message.
        for col in one_hot_message.T:
            i = np.where(col == 1)[0][0]
            
            message += self.ALFABETO[i]
        
        return message


    def encrypt(self, message, idx):
        '''
        Encrypts a one-hot letter.

        @param message: one-hot letter to be encrypted.
        @param idx: index of the letter in the message (determines the number of times the matrix P will be shuffled by E).
        @return: encrypted one-hot letter.

        '''
        message = np.array([message]).T

        # Shuffles the first time
        message = self.P @ message

        # Shuffles the number of times indicated by idx
        for _ in range(idx):
            message = self.E @ message

        return message


    def decrypt(self, message, idx):
        '''
        Decrypts a one-hot letter.

        @param message: one-hot letter to be decrypted.
        @param idx: index of the letter in the message (determines the number of times the matrix P was shuffled by E).
        @return: decrypted one-hot letter.

        '''
        message = np.array([message]).T

        # Unshuffles the number of times indicated by idx
        for _ in range(idx):
            message = np.linalg.inv(self.E) @ message

        # Unshuffles lastly the P matrix
        message = np.linalg.inv(self.P) @ message

        return message


    def enigma(self, message):
        '''
        Encrypts a string message.

        @param message: string to be encrypted.
        @return: encrypted string.

        '''

        # Validation
        if len(message) == 0:
            return "Encryption error: message cannot be empty. Reference alphabet: 'abcdefghijklmnopqrstuvwxyz '"

        for letter in message.lower():
            if letter not in self.ALFABETO:
                return f"Encryption error: '{letter}' not accepted. Message must contain only letters and spaces. No symbols or accents are allowed. Reference alphabet: 'abcdefghijklmnopqrstuvwxyz '"

        onehot = self.to_one_hot(message)

        encrypted_message = np.empty((27, 0))
        
        # Encrypts each letter in the message and concatenates the result to the encrypted message matrix.
        for i in range(onehot.shape[1]):
           encrypted_message = np.concatenate((encrypted_message, self.encrypt(onehot[:,i].T, i)), axis=1)
        
        # Returns the encrypted message as a string.
        return self.to_string(encrypted_message)


    def de_enigma(self, message):
        '''
        Decrypts a string message.

        @param message: string to be decrypted.
        @return: decrypted string.

        '''
        # Validation
        if len(message) == 0:
            return "Encryption error: message cannot be empty. Reference alphabet: 'abcdefghijklmnopqrstuvwxyz '"

        for letter in message.lower():
            if letter not in self.ALFABETO:
                return f"Encryption error: '{letter}' not accepted. Message must contain only letters and spaces. No symbols or accents are allowed. Reference alphabet: 'abcdefghijklmnopqrstuvwxyz '"
            
        onehot = self.to_one_hot(message)

        decrypted_message = np.empty((27, 0))

        # Decrypts each letter in the message and concatenates the result to the decrypted message matrix.
        for i in range(onehot.shape[1]):
           decrypted_message = np.concatenate((decrypted_message, self.decrypt(onehot[:,i].T, i)), axis=1)
        
        # Returns the decrypted message as a string.
        return self.to_string(decrypted_message)
