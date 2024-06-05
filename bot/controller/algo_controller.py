from bot.model import des3, aes, rc4, rsa
# Новый алгоритм надо добавлять в .env, algo_keyboard.py и algo.controller.py.
# Автор говнокодер простите
def encrypt(algo: str, plaintext: str):
    if algo.lower() == "3des":
        return des3.encrypt(plaintext)
    elif algo.lower() == "aes":
        return aes.encrypt(plaintext)
    elif algo.lower() == "rsa":
        return rsa.encrypt(plaintext)
    elif algo.lower() == "rc4":
        return rc4.encrypt(plaintext)
    else:
        raise Exception("Argument Exception")
    
def decrypt(algo: str, plaintext: bytes, key: bytes):
    if algo.lower() == "3des":
        return des3.decrypt(plaintext, key)
    elif algo.lower() == "aes":
        return aes.decrypt(plaintext, key)
    elif algo.lower() == "rsa":
        return rsa.decrypt(plaintext, key)
    elif algo.lower() == "rc4":
        return rc4.decrypt(plaintext, key)
    else:
        raise Exception("Argument Exception")