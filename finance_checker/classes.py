
class Document(object):

	def __init__(self, name, extension):
		name = self.name
		extension = self.extension
		doc_name = name + extension
		clean_doc = []

	def __str__(self):
		return self.name

	def document_reader(self): 

		with open('..file/' + doc_name, 'r', encoding = 'utf-8') as file:
			return file

	def cleaner(self, file):

		for line in file:
			word_list = line.split(",")
			clean_doc.append(word_list)

		return clean_doc

	
