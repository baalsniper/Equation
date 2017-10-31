import random
import numpy as np 
from math import sqrt  



print """1. Linear equation with one variable \n2. Quadratic equation\n3. System of linear equations"""
number = raw_input('Chon dang bai tap: ')

if number == '1':

	ex = int(raw_input('Exercise: '))
	for i in range(0, ex):
		mark = random.choice('+-')
		a = random.randint(-100,100)
		b = random.randint(-100,100)
		c = random.randint(-100,100)
		print '{:3d}x {:+3d} = {:3d}'.format(a,b,c)
		
		while True:
			answer = float(raw_input('x = '))
			x = (c-b)/float(a)
			if answer == round(x,2):
				print 'Answer: {:.2f}'.format(round(x,2))
				print
				break
			else:
				print 'Wrong answer'
				continue

elif number == '2':

	ex = int(raw_input('Exercise: '))		
	for i in range(0, ex):
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
			answer = int(raw_input('How many roots: '))
			if (d > 0) and (answer == 2):
				x1 = float(raw_input('x1 = '))
				x2 = float(raw_input('x2 = '))
				if ((x1 == round(z1,2)) and (x2 == round(z2,2))) or ((x1 == round(z2,2)) and (x2 == round(z1,2))): break
				else: 
					print 'Wrong answer'
					print 'Answer: x1 = {}, x2 = {}'.format(round(z1,2),round(z2,2))
					break

			elif (d == 0) and (answer == 1):
				x = float(raw_input('x = '))
				if x == round(z1,2): break
				else: 
					print 'Wrong answer'
					print 'Answer: x1 = x2 ={}'.format(z1)
					
			elif (d < 0) and (answer == 0): break

			else:
				print 'Wrong answer'
			
			continue
		print

elif number == '3':

	ex = int(raw_input('Exercise: '))
	a = 0		
	for i in range(0, ex+a):
		a = random.randint(-100,100)
		b = random.randint(-100,100)
		c = random.randint(-100,100)
		a1 = random.randint(-100,100)
		b1 = random.randint(-100,100)
		c1 = random.randint(-100,100)
		# solve system of linear equations by matrix
		while True:
			d = np.matrix([[a,b],[a1,b1]])
			try:
				d1 = np.linalg.inv(d)
			except numpy.linalg.LinAlgError:
				a += 1 # add one system of linear equations 
				break
			else:
				e = np.matrix([c,c1]).reshape(2,1)
				eq = d1*e
			
			print
			print '{:3d}x {:+3d}y = {:3d}'.format(a,b,c)
			print '{:3d}x {:+3d}y = {:3d}'.format(a1,b1,c1)

			while True:
				x = float(raw_input('x: '))
				y = float(raw_input('y: '))
				if (x == round(eq[0],2)) and (y == round(eq[1],2)):
					print 'Dap an x = {}, y = {}'.format(round(eq[0],2), round(eq[1],2))
					break
				else:
					print 'Wrong answer'
					continue
			break
		print	
else: pass