# Enigma_Encrypter Restful API

The encrypter can also be used as a local Restful API to encrypt and decrypt messages as `GET` requests.

Each request creates a new instance of the object Enigma with a given seed and utilizes it to encrypt or decrypt messages.

Also, the API treats exceptions in the body request and return the suitable error messages and codes.
<br/>

---

### How to Setup the API

1. Change to the API directory:

`cd .\api`

2. Install the requirements for the web service. Utilizing a **virtual python environment** is strongly recommended, avoiding any version conflicts.

`pip install -r requirements.txt`

3. Change to the source directory and start the application:

`cd .\src`

`python app.py`

4. If you see the following message on your terminal, you are ready to use the Enigma with requests through **Postman** or other program:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 854-186-789
```

---
<br/>

### How to Request from Enigma API

The Enigma API have only *2 paths*: `/enigma` and `/de_enigma`.

* `http://127.0.0.1:5000/enigma`  
* `http://127.0.0.1:5000/de_enigma`

Each one only accepts **GET** requests and requires the parameters to be sent in the following pattern:

```
{
  "message": <str>,
  "seed": <int>
}
```

*OBS: the seed is optional*

If done correctly, you will receive a JSON response with your encrypted or decrypted message as the example below:

**Request Body**:
```
{
    "message": "tiago eh legal",
    "seed": 29
}
```

**Response**:
```
{
    "encrypted message": "zgfpsfrmiofnvk"
}
```

---
<br/>

### Other request examples

##### DeEnigma

**Request Body**:
```
{
    "message": "zgfpsfrmiofnvk",
    "seed": 29
}
```

**Response**:
```
{
    "decrypted message": "tiago eh legal"
}
```

##### Enigma with no seed:

**Request Body**:
```
{
    "message": "matrizes sao incriveis"
}
```

**Response**:
```
{
    "encrypted message": "i vopygzuvevuxpynhd oh"
}
```

#### DeEnigma with no seed:

**Request Body**:
```
{
    "message": "i vopygzuvevuxpynhd oh"
}
```

**Response**:
```
{
    "decrypted message": "matrizes sao incriveis"
}
```

#### Enigma missing message

**Request Body**:
```
{
    "seed": 42
}
```

**Response**:
```
{
    "error": "Missing message"
}
```

#### Unsupported messages:

**Request Body**:
```
{
    "message": "Hello, world! áãç"
}
```

**Response**:
```
{
    "encrypted message": "Encryption error: message must contain only letters and spaces. No symbols or accents are allowed. Reference alphabet: 'abcdefghijklmnopqrstuvwxyz '"
}
```

**Request Body**:
```
{
    "message": ""
}
```

**Response**:
```
{
    "encrypted message": "Encryption error: message cannot be empty. \n Reference alphabet: 'abcdefghijklmnopqrstuvwxyz '"
}
```
