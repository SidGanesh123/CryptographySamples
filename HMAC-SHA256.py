import hashlib, hmac, binascii
def hmac_sha256(key, msg):
  return hmac.new(key, msg, hashlib.sha256).digest()
key = b"00000"
msg = b"Siddharth Ganesh"
output = binascii.hexlify(hmac_sha256(key, msg))
print (output)
print(key)
keyfi = ""
while (keyfi != "123"):
 hmac.new(key, msg, hashlib.sha256).digest()
 output = binascii.hexlify(hmac_sha256(key, msg))
 keyfi = (str(output))[2:5]
 print (output) 
 print (key)
 key =  key.decode('ASCII')
 key = int(key)
 key += 1
 key = str(key)
 key = key.encode('ASCII')
