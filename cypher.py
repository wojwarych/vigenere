import os
import re
import string
import sys



class Vigenere(object):


	def __init__(self, txt=None):

		self.ltrs_tbl = [[chr(j) for j in range(97, 123)] for i in range(26)]
		self.ltrs_tbl = self.reverse_order(self.ltrs_tbl)
		self.order_dict = {let: val for val, let in enumerate(string.ascii_lowercase)}

		self.msg_2_encrypt = self.get_text(txt)
		self.capital_ltrs = self.count_upper_ltrs(self.msg_2_encrypt)
		self.msg_2_encrypt = self.lower_txt()

	def reverse_order(self, ltrs):

		n = 1
		for l in ltrs[1:]:

			if l is ltrs[-1]:
				l.reverse()
				break

			for i in range(n):
				replacer = l.pop(0)
				l.append(replacer)

			n += 1

		return self.ltrs_tbl


	def get_text(self, txt=None):

		encrypt_txt = str()

		if txt is not None:

			path_to_txt = os.getcwd() + "\\" + txt

		if txt is None:

			txt = input("Please, enter the name of txt file to encrypt: ")
			path_to_txt = os.getcwd() + "\\" + txt

		with open(path_to_txt, 'r+') as  f:

				encrypt_txt = f.read()

		return encrypt_txt


	def lower_txt(self):

		return self.msg_2_encrypt.lower()


	def count_upper_ltrs(self, in_txt):
		
		capitals = set()
		for index, char in enumerate(in_txt):

			if re.match(r'\w', char) and char == char.upper():
				capitals.add(index)

		return capitals


	def get_key(self, key=None):

		if key is not None:

			encryptor = list(key)

		else:

			encryptor = list(input("Please, enter the key to encrypt message: "))

		return encryptor


	def inplace_msg(self, encryptor):
		
		self.inplace_str = self.msg_2_encrypt
		length_msg = len(self.msg_2_encrypt)
		n = 0
		while n < length_msg:

			for enc in encryptor:

				while n != length_msg and re.match(r'\W', self.msg_2_encrypt[n]):
					n += 1

				if n == length_msg:
						break

				self.inplace_str = self.inplace_str[:n] + self.inplace_str[n:].replace(self.inplace_str[n], enc, 1)
				n += 1


	def encrypt_msg(self):

		m = 0
		self.crypted_msg = str()
		length_msg = len(self.msg_2_encrypt)
		while m < length_msg:

			while m != length_msg and re.match(r'\W', self.msg_2_encrypt[m]):
				self.crypted_msg += self.msg_2_encrypt[m]
				m += 1

			if m == length_msg:
				break

			self.crypted_msg += self.ltrs_tbl[self.order_dict[self.msg_2_encrypt[m]]][self.order_dict[self.inplace_str[m]]]
			m += 1


	def restore_uppercase(self):

		for index, char in enumerate(self.crypted_msg):

			if index in self.capital_ltrs:

				self.crypted_msg = self.crypted_msg[:index] + self.crypted_msg[index:].replace(char, char.upper(), 1)

	def decrypt_key(self, encryptor):

		self.decryptor = "".join(encryptor)

		for i, j in enumerate(self.decryptor):

			replacer = list(self.order_dict.keys())[list(self.order_dict.values()).index((26 - self.order_dict[j]) % 26)]
			self.decryptor = self.decryptor[:i] + self.decryptor[i:].replace(self.decryptor[i], replacer, 1)

		return self.decryptor



if __name__ == "__main__":


	msg = Vigenere(sys.argv[1])
	encrypt = msg.get_key(sys.argv[2])
	msg.inplace_msg(encrypt)
	msg.encrypt_msg()
	msg.restore_uppercase()

	print(msg.crypted_msg)