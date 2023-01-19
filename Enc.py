import base64
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Load the public key from the PEM file
with open("pu.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Read the input file
with open("inenc.txt", "rb") as input_file:
    data = input_file.read()

# Encrypt the data using the public key
encrypted_data = public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Encode the encrypted data in base64
encoded_data = base64.b64encode(encrypted_data)

# Write the encoded data to the output file
with open("outenc.txt", "wb") as output_file:
    output_file.write(encoded_data)