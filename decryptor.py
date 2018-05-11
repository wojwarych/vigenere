import sys

from cypher import Vigenere



if __name__ == "__main__":

	msg = Vigenere(sys.argv[1])
	decryptor = msg.decrypt_key('tajne')
	encrypt = msg.get_key(decryptor)

	msg.inplace_msg(encrypt)
	msg.encrypt_msg()
	msg.restore_uppercase()

	print(msg.crypted_msg)