from AesEverywhere import aes256
from random import randint

key = randint(0, 2147483647).__str__()

def encrypt(msg: str):
    return aes256.encrypt(msg, key).hex(), key

def decrypt(msg: bytes, key: int):
    return aes256.decrypt(msg, key).decode()