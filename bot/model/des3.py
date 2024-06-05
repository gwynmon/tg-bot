from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

while True:
    try:    
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

def encrypt(msg):
    msg = msg.encode()
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(msg, 8))
    return ciphertext.hex(), key.hex()

def decrypt(msg: bytes, key: bytes):
    key = DES3.adjust_key_parity(key)
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = cipher.decrypt(msg)
    return unpad(plaintext, 8).decode('utf-8')