import rsa
import base64
from Crypto.Util.Padding import pad

def encrypt(msg: str):
    publicKey, privatKey = rsa.newkeys(256)
    msg = msg.encode('utf-8')
    plaintext = rsa.encrypt(msg, publicKey)
    
    return plaintext.hex(), privatKey

def decrypt(msg: str, privateKey: rsa.PrivateKey):
    return rsa.decrypt(msg, privateKey).decode("utf-8")
