import hashlib, binascii
text = 'Siddharth Ganesh'
data = text.encode("utf8")
help = ""
while (help != "000"):
 sha256hash = hashlib.sha256(data).digest()
 output = binascii.hexlify(sha256hash)
 print("SHA-256:   ", output)
 data = output
 help = (str(output))[2:5]
 print (help)
exit
