import random
import numpy as np 
from math import sqrt  



print """1. phuong trinh bac nhat\n2. phuong trinh bac 2\n3. He phuong trinh 2 an"""
number = raw_input('Chon dang bai tap: ')

if number == '1':

	bt = int(raw_input('So bai tap: '))
	for i in range(0, bt):
		mark = random.choice('+-')
		a = random.randint(-100,100)
		b = random.randint(-100,100)
		c = random.randint(-100,100)
		print '{:3d}x {:+3d} = {:3d}'.format(a,b,c)
		
		while True:
			answer = float(raw_input('x = '))
			x = (c-b)/float(a)
			if answer == round(x,2):
				print 'Dap an: {:.2f}'.format(round(x,2))
				print
				break
			else:
				print 'Dap an khong chinh xac'
				continue

elif number == '2':

	bt = int(raw_input('So bai tap: '))		
	for i in range(0, bt):
		mark = random.choice('+-')
		a = random.randint(-100,100)
		b = random.randint(-100,100)
		c = random.randint(-100,100)

		d = b**2 - 4*a*c
		z1 = (-b - sqrt(abs(d)))/(2*a)
		z2 = (-b + sqrt(abs(d)))/(2*a)

		print 
		print '{}x**2 {:+3d}x {:+3d} = 0'.format(a,b,c)
				
		while True:
			answer = int(raw_input('phuong trinh co may nghiem: '))
			if (d > 0) and (answer == 2):
				x1 = float(raw_input('x1 = '))
				x2 = float(raw_input('x2 = '))
				if ((x1 == round(z1,2)) and (x2 == round(z2,2))) or ((x1 == round(z2,2)) and (x2 == round(z1,2))): break
				else: 
					print 'Dap an khong chinh xac'
					print 'Dap an dung x1 = {}, x2 = {}'.format(round(z1,2),round(z2,2))
					break

			elif (d == 0) and (answer == 1):
				x = float(raw_input('x = '))
				if x == round(z1,2): break
				else: 
					print 'Dap an khong chinh xac'
					print 'dap an dung x1 = x2 ={}'.format(z1)
					
			elif (d < 0) and (answer == 0): break

			else:
				print 'Dap an khong chinh xac'
			
			continue
		print

elif number == '3':

	bt = int(raw_input('So bai tap: '))
	a = 0		
	for i in range(0, bt+a):
		a = random.randint(-100,100)
		b = random.randint(-100,100)
		c = random.randint(-100,100)
		a1 = random.randint(-100,100)
		b1 = random.randint(-100,100)
		c1 = random.randint(-100,100)

		while True:
			d = np.matrix([[a,b],[a1,b1]])
			try:
				d1 = np.linalg.inv(d)
			except numpy.linalg.LinAlgError:
				a += 1
				break
			else:
				e = np.matrix([c,c1]).reshape(2,1)
				eq = d1*e
			
			print
			print '{:3d}x {:+3d}y = {:3d}'.format(a,b,c)
			print '{:3d}x {:+3d}y = {:3d}'.format(a1,b1,c1)

			while True:
				x = float(raw_input('nghiem x: '))
				y = float(raw_input('nghiem y: '))
				if (x == round(eq[0],2)) and (y == round(eq[1],2)):
					print 'Dap an x = {}, y = {}'.format(round(eq[0],2), round(eq[1],2))
					break
				else:
					print 'Dap an khong chinh xac'
					continue
			break
		print	
else: pass