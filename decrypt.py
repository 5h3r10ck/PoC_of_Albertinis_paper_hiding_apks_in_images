from Crypto.Cipher import AES

algo = AES.new('mykey_0123456789', AES.MODE_CBC, '\xd8~\xecB\x0f\x11\xafS\xa0N\x94G\xa7\x97I\x9f')

with open('dec-projet.png', "rb") as f:
	d = f.read()

d = algo.decrypt(d)

with open('decrypted.apk', "wb") as f:
	f.write(d)
