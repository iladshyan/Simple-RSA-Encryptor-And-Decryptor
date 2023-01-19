from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

print('Enter A password to protect private key. WARNING IF YOU LOSE THIS PASSWORD YOU CANNOT DECRYPT ANY FILES ENCRYPTED WITH PUBLIC KEY CORRESPONDING TO THIS PRIVATE KEY')
password = input("Password :")

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(bytes(password, 'utf-8'))
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


# Save the key pair to a secure location
with open('pr.pem', 'wb') as f:
    f.write(private_pem)

with open('pu.pem', 'wb') as f:
    f.write(public_pem)
