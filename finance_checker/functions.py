def cleaner(document):
	clean_file = []
	for line in filename:
		filename_list = line.split(",")
		clean_file.append(filename_list[1:5])
	return clean_file