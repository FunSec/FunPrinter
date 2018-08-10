# -*- coding: utf-8 -*-

import sys, os

LINE_BREAKS = 79

print 'By FunSec with love ;)'

def compatibility(file):
	with open(file, 'r') as worker:
		data_file = worker.readlines()

		raw_data = ''
		for line in data_file:
			raw_data += line


		if len(data_file) > LINE_BREAKS:
			print '[ERROR] Your file have more than one page'
			sys.exit()
		elif len(data_file) == 80:
			print '[DONE] Your file have exactly one page'
			sys.exit()
		
		lines_need = LINE_BREAKS-len(data_file)

		while lines_need > 0:
			raw_data+='\n'
			lines_need-=1

		with open('temp', 'w') as temp:
			temp.write(raw_data)

			temp.close()

		with open('temp', 'r') as temp:

			if not len(temp.readlines()) == LINE_BREAKS:
				print '[ERROR] Its was at this moment Fun knew... He fucked up!'
			
			temp.close()
		
		worker.close()
	
	with open(file, 'w') as worker:
		worker.write(raw_data)
		



if len(sys.argv) < 2:
	print '[ERROR] File name needed in args\nExample: python '+sys.argv[0]+' myfile.txt'
	sys.exit()

if not os.path.exists(sys.argv[1]):
	print "[ERROR] '+sys.argv[1]+' don't exists in your computer. Bruh!"
	sys.exit()

compatibility(sys.argv[1])
