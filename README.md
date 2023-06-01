# Simple-RSA-Encryptor-And-Decryptor
This repo name is self-explanatory. This software could encrypt and/or decrypt file(s). Look at below for more info on how to use this. DO NOT USE THIS FOR HIGH SECURITY APPS AND I AM NOT RESPONSIBLE FOR ANY HARM CAUSED TO ANYONE OR ANYTHING BY USING THIS CODE.  This is some beginner level code but you can still [post issues](https://github.com/iladshyan/Simple-RSA-Encryptor-And-Decryptor/issues) about this program.


## Generating A Key Pair

 1. First Run `KeyGen.py`
 2. It will ask you for a password. Enter a secure and memorable password. 
      **WARNING** - IF YOU LOSE THIS PASSWORD YOU CANNOT DECRYPT ANY FILES ENCRYPTED WITH PUBLIC KEY CORRESPONDING TO THIS PRIVATE KEY **(TL;DR Don't loose your Private key password)**
      
 3. The code will generate two key pair files called `pr.pem` and `pu.pem`
 4. `pu.pem` is unencrypted Public Key
 5. `pr.pem` is encrypted (using the password provided when running the script) Private Key

**NOTES** - 

1. Public key can be shared freely But Private key must be kept secret
2. `.pem` files are standert in security inustry you can edit the code to change the program to output `.txt` files too

## Encrypting

 1. In `inenc.txt` file type the content to be encrypted 
 2. Run `Enc.py` 
 3. Output will be in a file called `outenc.txt` encoded in Base64 for ease of sharing

## Decrypting

 1. In `indec.txt` file type the encrypted content (Copy -> Paste)
 2. Run `Dec.py`
 3. It will ask for a password. Provide the password you gave the program while generating key pair using `KeyGen.py` script
 4. Output will be in `outdec.txt` file 

## If you like this project ...

 - Just put this repo link if you review or use resonable amount of this code
 - Star the project (Only if you like this project)
 - Please ask for feature requests. I will try my best to add them
