from random import randint

class HashTable():
	def __init__(self):
		self.mydict = ['None']*50
		self.add_data = []

	def __str__(self):
		return str(self.__dict__)

	def set(self, key, value):
		addres = self._hash()
		self.mydict[addres] = [key,value]
		self.add_data.append(addres)

	def get(self, key):
		for i in self.add_data:
			if self.mydict[i][0] == key:
				return self.mydict[i][1]

	def keys(self):
		keys_arr = []
		for i in self.add_data:
			keys_arr.append(self.mydict[i][0])
		return keys_arr

	def _hash(self):
		while True:
			x = randint(0, 49)
			if x not in self.add_data:
				return x

myHashTable = HashTable()
myHashTable.set('hey', 5)
print(myHashTable.get('hey'))
print(myHashTable.keys())