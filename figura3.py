from turtle import * 

def cuadro(cuadros):
	s = 600
	r = 0.05
	x = 1.0 - r
	for k in range(cuadros):
		for i in range(2): 
			fd(s * x) 
			rt(90) 
		x = x - r 
up()
setpos(-300,300)
down()
cuadro(19) 
done() 