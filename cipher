from Crypto.Cipher import AES
import os
#Name and key 
name = b'Siddharth Ganesh'
key = os.urandom(32)
#Cipher to use for encrypting name with key
aesInstance = AES.new(key, AES.MODE_GCM)
#Name gets encrypted with cipher resulting in two outputs
cipher_name, name_tag = aesInstance.encrypt_and_digest(name)
#Printing the two outputs
print(cipher_name)
print(name_tag)
#New cipher to use for decrypting using the previous cipher
decryptingCipher = AES.new(key, AES.MODE_GCM, aesInstance.nonce)
#New cipher uses the cipher_name and name_tag to decrypt the name
decryptedName = decryptingCipher.decrypt_and_verify(cipher_name, name_tag)
print(decryptedName)
