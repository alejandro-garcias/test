from turtle import * 

def cuadro(cuadros):
	x = 1
	for k in range(cuadros):
		for i in range(4): 
			fd(100 * x) 
			rt(90) 
		x = x + 1 
up()
setpos(-300,300)
down()
cuadro(4) 
done() 