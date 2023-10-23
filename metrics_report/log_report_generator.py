from functions import*
import csv

team = ['Alejandra Ramirez Andrade', 'Carolina', 'Aura Rojas',
		'Ivonne Sierra', 'Alejandra Cordoba', 'Luis Martinez', 'Durley Tatiana Nuñez Quiroga',
		 'Soranyi Rodriguez Casallas', 'Valentina Torres', 'Maria Fernanda Soler',
		'Viviana Castro', 'Alejandra Villan', 'Carolina Pinzón', 'Viviana Cordoba Beltran']

logs = log_cleaner("log_report/logs.csv")

team_logs = []

for x in logs:
	x[-1] = x[-1].strip()

for name in team:
	for log in logs:
		team_name_splited = name.split()
		log_name_splited = log[0].split()
		if  team_name_splited[0:2] == log_name_splited[0:2]:
		 	team_logs.append([log[0],f'{log[1]} {log[2]} {log[3]}'])
team_logs.reverse()

with open('clean_logs.csv','w', newline='') as file:
	writer = csv.writer(file)
	writer.writerows(team_logs)