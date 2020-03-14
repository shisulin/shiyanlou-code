import csv
import json
import sys
files = sys.argv[1:]

def calculator(income):
	start_point = 5000
	social_security = 0.08 + 0.02 + 0.005 + 0.06
	tax_part = income * (1 - social_security) - start_point
	
	if tax_part <= 0:
		tax = 0 
	elif tax_part <= 3000:
		tax = tax_part * 0.03
	elif tax_part <= 12000:
		tax = tax_part * 0.1 - 210 
	elif tax_part <= 25000:
		tax = tax_part * 0.2 - 1410
	elif tax_part <= 35000:
		tax = tax_part * 0.25 - 2660
	elif tax_part <= 55000:
		tax = tax_part * 0.3 - 4410
	elif tax_part <= 80000:
		tax = tax_part * 0.35 - 7160
	else:
		tax = tax_part * 0.45 - 15160
	salary = income * (1 - social_security) - tax
	return '{:.2f}'.format(salary)
    

def output(data):
	json_str = json.dumps(data)
	
	with open(files[1],'w') as f:
		f.write(json_str)
        
    
def main():
	result = {}
	
	with open(files[0]) as f:
		usr_csv = csv.reader(f)
		data_list = list(usr_csv) 
	
	for item in data_list:
		ID,income = item[0],float(item[1])
		income = calculator(income)
		result[ID] = income
	
	output(result)
	
	
if __name__=='__main__':
	main()
