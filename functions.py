import datetime

def cleaner(document):
	#will split the document

	with open(document, 'r',encoding = "utf-8") as file:
		clean_file = []
		count = 0
		for line in file:
			count += 1
			if count > 5:
				word = line.split(',')
				clean_file.append(word[1:])
	return clean_file

def log_cleaner(document):
	#will split the document

	with open(document, 'r',encoding = "utf-8") as file:
		clean_file = []
		for line in file:
			word = line.split(',')
			clean_file.append(word)
	return clean_file

def organized(elements):
	#will assign the metrics to the names
	metrics_names = []
	for name in range(len(elements[0])): 
		metrics_names.append([elements[0][name].strip('"').strip('"\n'), elements[1][name].strip('"').strip('"\n')])
	return metrics_names

#clean document
def cleaned_document(document):
	doc = cleaner(document)
	doc = organized(doc)

	return doc

#get names
def get_names(lists):
	names = []
	for element in lists:
		for name in element:
			if name[0] not in names:
				names.append(name[0])
	return sorted(names)

#assign empty metrics
def metrics_by_name(names):
	metrics = []
	for name in names:
		metrics.append([name, 0,0,0,0,0])

	return metrics

# get names and assign metrics
def names_and_empty_metrics(name_list):
	names = get_names(name_list)
	metrics = metrics_by_name(names)

	return sorted(metrics)

#assign metrics
def get_metrics_together(names, metric_to_add,index):
	for name in names:
		for metric in metric_to_add:
			if name[0] == metric[0]:
				name[index] = metric[1].strip('"').strip("'")

	return names			

def time_divider(metrics_list, i):
	for agent in metrics_list[1:]:
		if len(agent) < i+1:
			continue
		# ahm = f'{float(agent[i]) / 60:.2f}'
		ahm = str(datetime.timedelta(seconds=int(agent[i])))
		agent[i] = ahm

	return metrics_list

def att_format(document):
	with open(document, 'r',encoding = "utf-8") as file:
		clean_file = []
		count = 0
		for line in file:
			count += 1
			if count > 5:
				word = line.split(',')
				clean_file.append(word)
	return clean_file

def att_organized(listas):
	#will assign the metrics to the names
	for lista in listas:
		for i in range(len(lista)):
			lista[i] = lista[i].strip('"').strip('"\n')
	return listas

def att_cleaner(doc):
	document = att_format(doc)
	document = att_organized(document)

	return document

def att_names_organizer(lista):
	names = []
	for name in lista[0][1:]:
		if name not in names:
			names.append([name])
	return names

def att_time_assigment(doc1,doc2,names):
	attendance = []
	#getting index from each list
	for name in names:
		indx1 = doc1[0].index(name[0])
		indx2 = doc2[0].index(name[0])

		for time in range(len(doc1)):
			if time > 0:
				attendance.append([name[0], doc1[time][indx1], doc2[time][indx2], 0, doc2[time][0]])
	return attendance

def att_format_transformation(att):
	for time in att:
		if time[1] == '-' or time[1] == "":
			time[1] = 0
		if time[2] == '-' or time[2] == "":
			time[2] = 0
		if int(time[1]) > 0:
			time[1] = int(time[1])
	return att

def att_missing_time(att):
	for time in att:
		time[3] = int(time[1]) - int(time[2])
	return att

def att_time_divider(attendance, i):
	for time in attendance:
		ahm = str(datetime.timedelta(seconds=int(time[i])))
		time[i] = ahm

	return attendance

def att_creation(doc1,doc2):
	names = att_names_organizer(doc1)
	attendance = att_time_assigment(doc1,doc2, names)
	attendance = att_format_transformation(attendance)
	attendance = att_missing_time(attendance)

	return attendance
