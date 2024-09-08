import requests
import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# AES Encryption
def encrypt_aes(plaintext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_plaintext = plaintext + (16 - len(plaintext) % 16) * ' '  # Add padding
    encrypted = encryptor.update(padded_plaintext.encode('utf-8')) + encryptor.finalize()
    return encrypted

# RSA Encryption (Encrypt the AES key using RSA)
def encrypt_rsa(public_key_pem, data):
    public_key = serialization.load_pem_public_key(public_key_pem.encode(), backend=default_backend())
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

# Client function to fetch server's public key and send encrypted data
def client():
    try:
        # Step 1: Fetch the server's public key
        response = requests.get('http://localhost:5000/get_public_key')
        public_key_pem = response.json()['public_key']

        # Step 2: Generate AES key and IV
        aes_key = os.urandom(32)  # AES-256 key
        iv = os.urandom(16)       # Initialization vector (16 bytes)

        # Step 3: Encrypt the message with AES
        message = "This is a top-secret message!"
        encrypted_message = encrypt_aes(message, aes_key, iv)

        # Step 4: Encrypt the AES key using the server's public RSA key
        encrypted_aes_key = encrypt_rsa(public_key_pem, aes_key)

        # Step 5: Send the encrypted AES key, IV, and encrypted message to the server
        payload = {
            'encrypted_aes_key': encrypted_aes_key.hex(),
            'iv': iv.hex(),
            'encrypted_message': encrypted_message.hex()
        }

        result = requests.post('http://localhost:5005/decrypt_message', json=payload)
        print(f"Server's response: {result.json()}")
    except Exception as e:
        print(f"Error: {e}")

client()
