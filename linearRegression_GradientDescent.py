import pygame
from scipy.interpolate import interp1d  #python equivalent of arduino's map function


def drawline():
	x1=0
	y1=m*x1+b
	x2=1
	y2=m*x2+b

	#interpid is similar to map function in arduino
	xx=interp1d([0,1],[0,width],fill_value="extrapolate")#for x
	x1=int(xx(x1))
	x2=int(xx(x2))
	yy=interp1d([1,0],[0,height],fill_value="extrapolate")#for y # it is opposite since we want the origin to be at down left corner 
	y1=int(yy(y1))
	y2=int(yy(y2))
	return(x1,x2,y1,y2)

def gradientDescent(m,b):
	
	learningRate=0.05
	for i in range(len(data)):
		x=data[i][0]
		y=data[i][1]

		guess=m*x+b
		error=y-guess
		m=m+(error*x)*learningRate
		b=b+(error)*learningRate	
		

	return m,b


data=[] #to handle real data
data1=[] #to display all the points
running =1
LEFT = 1
x=y=0
width=400
height=400
screen=pygame.display.set_mode((width,height))

bgcolor = 0, 0, 0
screen.fill(bgcolor)

m=0
b=0
while running :
	event=pygame.event.poll()
	if event.type==pygame.QUIT:
		running =0
	elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
		x,y=event.pos
		

		point=[x,y]

		data1.append(point)
		xx=interp1d([0,width],[0,1])#for x
		x=float("{0:.2f}".format(xx(x)))
		yy=interp1d([0,height],[1,0])#for y # it is opposite since we want the origin to be at down left corner 
		y=float("{0:.2f}".format(yy(y)))

		point=[x,y]

		data.append(point)

		

	if len(data)>1:	
		m,b=gradientDescent(m,b)
		
	x1,x2,y1,y2=drawline() 
	
	pygame.draw.lines(screen,(255, 255, 255),True,((x1,y1),(x2,y2)), 5)

	for i in data1:
		pygame.draw.circle(screen, (255, 255, 255), i, 5)

	pygame.display.flip()
	screen.fill(bgcolor)


		