import csv
def ReadCSV(fname):
	with open(fname, newline='',encoding='utf-8-sig') as csvfile:
		data = csv.DictReader(filter(lambda row: row[0]!='#', csvfile))
		# data = csv.DictReader(csvfile)
		listdata=list(data)
		# for row in data:
		# 	print(row)
#        print(', '.join(row))
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	return listdata

# import sys
# def join(f1,f2,fout):
def join(f2,f1=''):
	# if len(sys.argv) > 2:
	if f1:
		with open(f1) as fp:
			ff1 = fp.read()
	else :
		ff1= ''
	with open(f2) as fp:
		ff2 = fp.read()

	# with open (fout, 'w') as fp:
	with open (f2, 'w') as fp:
		fp.write(ff1+"\n"+ff2)

	return ff2
