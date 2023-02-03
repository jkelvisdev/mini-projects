
class Document(object):

	def __init__(self, name):
		self.name = name
		self.extension = '.csv'
		self.doc_name = self.name + self.extension
		self.clean_doc = None

	def __str__(self):
		return self.doc_name

	def reader(self): 

		with open('file/'+self.doc_name, 'r', encoding = 'utf-8') as file:
			file = file.read()
			return file

	def cleaner(self, file):

		self.clean_doc = file.split(",")
