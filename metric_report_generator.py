from functions import*
import datetime
import csv

aht = cleaned_document("metrics/AHT.csv")
csat = cleaned_document("metrics/CSAT.csv")
frt = cleaned_document("metrics/MFRT.csv")
mrt = cleaned_document("metrics/MMRT.csv")
participated = cleaned_document("metrics/PARTICIPATIONS.csv")

# sorting lists

aht = sorted(aht)
csat = sorted(csat)
frt = sorted(frt)
mrt = sorted(mrt)
participated = sorted(participated)


# names = get_names([aht,csat,frt,mrt,participated])
#get all names
names = names_and_empty_metrics([aht,csat,frt,mrt,participated])


metrics = get_metrics_together(names,frt,1)
metrics = get_metrics_together(metrics,mrt,2)
metrics = get_metrics_together(metrics,aht,3)
metrics = get_metrics_together(metrics,participated,4)
metrics = get_metrics_together(metrics,csat,5)

metrics.insert(0,['AGENT', 'MFRT', 'MMRT', 'AHT','PARTICIPATIONS','CSAT'])

metrics = time_divider(metrics, 1)
metrics = time_divider(metrics, 2)
metrics = time_divider(metrics, 3)


with open('metrics_report.csv','w', newline='', encoding = "utf-8") as file:
	writer = csv.writer(file)
	writer.writerows(metrics)

# print(metrics)

# for l in metrics:
#  	print(l)

# for x in names:
# 	print(x)

# print(aht)