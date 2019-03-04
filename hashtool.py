# Script make by Lucas.C | Python 3.7
import hashlib
import os
import sys
import time

# Pour exécuter la commande 'cls' avant l'exécution du script en lui même.
def clsa():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])
clsa()


print("")
print("		###########################################")
print("				Hashing Tool : ")
print("		###########################################")
print("")
print("			[1] Secure Hash Algorithms MD5")
print("			[2] Secure Hash Algorithms SHA1")
print("			[3] Secure Hash Algorithms SHA224")
print("			[4] Secure Hash Algorithms SHA256")
print("			[5] Secure Hash Algorithms SHA384")
print("			[6] Secure Hash Algorithms SHA512")
print("			[7] All Secure Hash Algorithms")
print("")

choose = input("			> Type here the number of Hash Algorithm : ")
msg = input("			> Write the password/msg : ")

file = 'data.txt'
write = open(file,'w')

if choose == "1":
	port = hashlib.md5(msg.encode('utf-8')).hexdigest()
	print("")
	print("			Password/msg in MD5 > " + port)
	write.write("[#] > " + time.asctime() + " > " + "*" + msg + "*" + " = " + port)
	print("			> (Very obsolete) Password/msg save in data.txt")
elif choose == "2":
	port2 = hashlib.sha1(msg.encode('utf-8')).hexdigest()
	print("")
	print("			Password/msg in SHA1 > " + port2)
	write.write("[#] > " + time.asctime() + " > " + "*" + msg + "*" + " = " + port2)
	print("			> (Very obsolete) Password/msg save in data.txt")
elif choose == "3":
	port3 = hashlib.sha224(msg.encode('utf-8')).hexdigest()
	print("")
	print("			Password/msg in SHA224 > " + port3)
	write.write("[#] > " + time.asctime() + " > " + "*" + msg + "*" + " = " + port3)
	print("			> (Very obsolete) Password/msg save in data.txt")
elif choose == "4":
	port4 = hashlib.sha256(msg.encode('utf-8')).hexdigest()
	print("")
	print("			Password/msg in SHA256 > " + port4)
	write.write("[#] > " + time.asctime() + " > " + "*" + msg + "*" + " = " + port4)
	print("			> (Very obsolete) Password/msg save in data.txt")
elif choose == "5":
	port5 = hashlib.sha384(msg.encode('utf-8')).hexdigest()
	print("")
	print("			Password/msg in SHA384 > " + port5)
	write.write("[#] > " + time.asctime() + " > " + "*" + msg + "*" + " = " + port5)
	print("			> (Very obsolete) Password/msg save in data.txt")
elif choose == "6":
	port6 = hashlib.sha512(msg.encode('utf-8')).hexdigest()
	print("")
	print("			Password/msg in SHA512 > " + port6)
	write.write("[#] > " + time.asctime() + " > " + "*" + msg + "*" + " = " + port6)
	print("			> (Very obsolete) Password/msg save in data.txt")
elif choose == "7":
	hash1 = hashlib.md5(msg.encode('utf-8')).hexdigest()
	hash2 = hashlib.sha1(msg.encode('utf-8')).hexdigest()
	hash3 = hashlib.sha224(msg.encode('utf-8')).hexdigest()
	hash4 = hashlib.sha256(msg.encode('utf-8')).hexdigest()
	hash5 = hashlib.sha384(msg.encode('utf-8')).hexdigest()
	hash6 = hashlib.sha512(msg.encode('utf-8')).hexdigest()

	print("")
	print("			Password/msg in MD5 > " + hash1)
	print("			Password/msg in SHA1 > " + hash2)
	print("			Password/msg in SHA224 > " + hash3)
	print("			Password/msg in SHA256 > " + hash4)
	print("			Password/msg in SHA384 > " + hash5)
	print("			Password/msg in SHA512 > " + hash6)
else:
	print("") 
	print("			[#] Secure Hash Algorithm not found !")



