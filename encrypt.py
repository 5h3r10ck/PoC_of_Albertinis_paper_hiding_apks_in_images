from Crypto.Cipher import AES

algo = AES.new('mykey_0123456789', AES.MODE_CBC, '\xd8~\xecB\x0f\x11\xafS\xa0N\x94G\xa7\x97I\x9f')

with open('app-similar.apk', "rb") as f:
	d = f.read()

d = algo.encrypt(d)

with open("dec-" + 'projet.png', "wb") as f:
	f.write(d)
