for i in range(1,101):
	if i%7!=0:
		a=i//10		
		while a<11:
			if a==0:
				print(i)
			elif a==7:
				break
			else: 
				if i%10 ==7:
					break
				print(i)
			break
