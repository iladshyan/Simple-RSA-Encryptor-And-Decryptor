import base64
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

passwordin = input("Password :")

try:

    # Load the private key from the PEM file
    with open("pr.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password = bytes(passwordin, 'utf-8'),
            backend = default_backend()
        )

    # Read the encoded data from the input file
    with open("indec.txt", "rb") as input_file:
        encoded_data = input_file.read()

    # Decode the data from base64
    encrypted_data = base64.b64decode(encoded_data)

    # Decrypt the data using the private key
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Write the decrypted data to the output file
    with open("outdec.txt", "wb") as output_file:
        output_file.write(decrypted_data)


except ValueError as e:
    if 'Bad decrypt' in str(e):
        print("The password entered is incorrect. Please try again.")
    else:
        raise