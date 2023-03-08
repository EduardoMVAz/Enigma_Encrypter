# Enigma_Encrypter
## Enigma-like Encrypting Library Utilizing Linear Algebra

Developers:

* João Lucas de Moraes Barros Cadorniga [JoaoLucasMBC](https://github.com/JoaoLucasMBC)  
* Eduardo Mendes Vaz [EduardoMVaz](https://github.com/EduardoMVAz)

The Enigma library is a tool for encrypting messages, using the same system that the Enigma machine, developed by the nazis on the Second World War and cracked by Alan Turing, utilizes, but with matrix multiplication.

---

## How to install

To utilize this python library, simply install it using pip as such:

* pip install https://github.com/EduardoMVAz/Enigma_Encrypter.git

---

## How to Use

There is a jupyter nootebook named demo in this repository, with a brief demonstration of how u can utilize the functions of the library which are:

* Encrypting a message, with the Enigma class.

* Utilizing a seed to determine your encryption. As shown in the mathematical model, our program utilizes a seed, that can be either chosen by the user or not (if not, the seed is always 42), to determine how the the matrixes are shuffled. That means that two instances of Enigma with the same seed will encrypt a message the same way, and are able to decrypt messages encrypted by the other instance.

* Decrypting a message, also with the Enigma class. To decrypt correctly, the engima instance used to decrypt must have the same seed as the one used to encrypt.

---

## Mathematical Model

The mathematical model for the Enigma library consists in utilizing matrix multiplications to shuffle the message, in the following manner: 

#### Encryption

* First, letters are transformed into one hot, so each letter is a vector $V\subscript{27,1}$, with zeros in all lines but the one representing its position in the order "abcdefghijklmnopqrstuvwxyz ", with a space at the end. So a complete message is a matrix with the concatanated vectors of each letter.

* Then, for each letter represented by the $V\subscript{27,1}$ vector, the encrypt function is called, which is used by the enigma function to shuffle the message.

* Each letter in the message, including spaces, is multiplied by a matrix P, which is a permutated identity matrix, generated utilizing the seed given by the user or pre-selected. 

* After this, the letter is multiplied by another version of the P matrix, but shuffled once more, called E matrix. This is repeated a the number of times equal to the index (0 - size of the message) of the letter in the message. So, for example, the first letter V1 is multiplied only by P, P @ V1, for its index in the message is 0, and the seventh letter V7 is multiplied by P and 6 times by E, E @ E @ E @ E @ E @ E @ P @ V7, for its index in the message is 6.

#### Decryption

* The basis for decryption is utilizing the inverse of the permutation matrixes P and E, for when a matriz is multiplied by its inverse, it becomes an indentity matrix, which when multiplied by another matrix, results in this other matrix (same as multiplying a number by 1).

* So the process is basically the same as encryption, but the letters are multiplied by the inverse of P, and then by the inverse of E, as many times as their index, returning to their original one hot configuration, and then translated back into text before being returned to user.