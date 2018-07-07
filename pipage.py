#If you don't want to install screeninfo 
#you can set this variable to your screen's width
default_width = 480

#IMPORTS
import random, math, time, sys

#attempt to set screen size automatically
#also tkinter in python3, but Tkinter in python2. Why? 
if sys.version_info[0] < 3:
	from Tkinter import *
	if default_width == 480:
		try:
			import screeninfo
			screen = screeninfo.get_monitors()[0]
			cw = screen.width
		except ImportError:

			print("It seems you haven't installed <screeninfo> a python package required to get your monitor's width")
			print("You can install it with 'pip install screeninfo'")
			print("The program will use the default width, which you may change in the pillows.py file.")
			cw = default_width
	else:
		cw = default_width
else:
	from tkinter import *
	if default_width == 480:
		try:
			import screeninfo
			screen = screeninfo.get_monitors()[0]
			cw = screen.width
		except ImportError:
			print("It seems you haven't installed <screeninfo> a python package required to get your monitor's width")
			print("You can install it with 'pip3 install screeninfo'")
			print("The program will use the default width, which you may change in the pillows.py file.")
			cw = default_width
	else:
		cw = default_width
	
#VARIABLES, but they don't actually change that much

sqh = (cw/5-4)/math.sqrt(2) #height of a square
sqd = sqh*math.sqrt(2) #hypotenuse of square
b = sqh/2 #these are here to make things simpler
d = sqd/2
ch = sqd+100 #This is the height of canvas
oh = sqh/6 #overlay, how much will the pillow cover pillows beneath
od = sqd/5 

comb = 0 #combination counters
comb2 = 0



#FUNCTIONS

def trinar(x): #converts integer (0-8) base 10 to base 3, returns a list of two strings
	ans = []
	while x > 0:
		rest = int(x % 3)
		x -= rest
		x = x/3
		ans.insert(0, str(rest))
	while len(ans) < 2:
		ans.insert(0, "0")
	return(ans)

def next_comb(): #increases combination counters
	global comb
	global comb2
	comb += 1
	if comb == 16:
		comb = 0
		comb2 += 1
		if comb2 == 9:
			comb2 = 0
	show_a_pattern()

def back_comb(): #decreases combination counters
	global comb
	global comb2
	comb -= 1
	if comb ==  -1:
		comb = 15
		comb2 -= 1
		if comb2 == -1:
			comb2 = 8
	show_a_pattern()
def rand_comb(): #sets combination counters to random values
	global comb
	global comb2
	comb = random.randint(0, 15)
	comb2 = random.randint(0, 8)
	show_a_pattern()

def gen_from_code(): #reads the input and converts it into a combination pattern
	global comb
	global comb2
	try:	
		code = int(ent.get())
	except ValueError:
		print('Woah there, this was supposed to be an integer, silly!')
	else:
		if code > 143 or code < 0:
			print('This must be between 0 and 143, silly!')
		else:
			rest = code % 16
			code -= rest
			comb = int(rest)
			comb2 = int(code/16)
			show_a_pattern()

#not sure if this is the proper way to do this, but it works
#basically button events that lead to other fuctions		
def rand_but(event):
	rand_comb()
def next_but(event):
	next_comb()
def back_but(event):
	back_comb()
def ent_but(event):
	gen_from_code()

#this one shows the pattern
def show_a_pattern():
	w.delete(ALL)#clear canvas
	
	#display current combination number
	root.title(str(comb)+';'+str(comb2)+" ("+str(comb+(16*comb2))+")")

	props = bin(comb)[2:] #convert combination counters into properties lists
	while len(props) < 4: #4 binary signs for the first counter
		props = "0" + props
	print(props)

	props2 = trinar(comb2) #and 2 ternary for the second counter
	print(props2)

	#the color of outer pillows
	if props[0] == '1': #if 1 then red
		colin = "blue"
		colout = "red"

	else:#if 0 then blue
		colin = "red"
		colout = "blue"


	#creating pillows
	if props[1] == '0':#middle pillow
		pil3 = w.create_rectangle(cw/2-b, ch/2-b, cw/2+b, ch/2+b, fill="orange red", outline='pink')#normalsquare
		rmidx = w.coords(pil3)[2]
		lmidx = w.coords(pil3)[0]#this saves coordinates for other pillows
		upmidy = w.coords(pil3)[1]
		dwmidy = w.coords(pil3)[3]
	else:
		pil3 = w.create_polygon(cw/2, ch/2-d, cw/2+d, ch/2, cw/2, ch/2+d, cw/2-d, ch/2, fill="orange red", outline='pink')#rotated square
		upmidy = w.coords(pil3)[1] 
		dwmidy = w.coords(pil3)[5]
		rmidx = w.coords(pil3)[2]
		lmidx = w.coords(pil3)[6]
		

	if props[2] == '0':#inner pillows
		pil2 = w.create_rectangle(cw/2-b, ch/2-b, cw/2+b, ch/2+b, fill=colin, outline='white')
		pil4 = w.create_rectangle(cw/2-b, ch/2-b, cw/2+b, ch/2+b, fill=colin, outline='white')
		if props2[0] == '1':
			w.move(pil4, rmidx-cw/2+b, 0)
			w.move(pil2, -(cw/2-lmidx+b), 0)
		elif props2[0] == '2':
			w.move(pil4, rmidx-cw/2+b-oh, 0)
			w.move(pil2, -(cw/2-lmidx+b-oh), 0)
			w.tag_raise(pil2)
			w.tag_raise(pil4)

		elif props2[0] == '0':
			w.move(pil4, rmidx-cw/2+b-oh, 0)
			w.move(pil2, -(cw/2-lmidx+b-oh), 0)
			w.tag_lower(pil4)
			w.tag_lower(pil2)	 
		rinx = w.coords(pil4)[2]
		linx = w.coords(pil2)[0]

	else:
		pil2 = w.create_polygon(cw/2, ch/2-d, cw/2+d, ch/2, cw/2, ch/2+d, cw/2-d, ch/2, fill=colin, outline='white')
		pil4 = w.create_polygon(cw/2, ch/2-d, cw/2+d, ch/2, cw/2, ch/2+d, cw/2-d, ch/2, fill=colin, outline='white')
		if props2[0] == '1':
			w.move(pil2, -(cw/2-lmidx+d), 0)
			w.move(pil4, rmidx-cw/2+d, 0)
		elif props2[0] == '2':
			w.move(pil2, -(cw/2-lmidx+d-od), 0)
			w.move(pil4, rmidx-cw/2+d-od, 0)
			w.tag_raise(pil2)
			w.tag_raise(pil4)
		elif props2[0] == '0':

			w.move(pil2, -(cw/2-lmidx+d-od), 0)
			w.move(pil4, rmidx-cw/2+d-od, 0)
			w.tag_lower(pil4)
			w.tag_lower(pil2)

		rinx = w.coords(pil4)[2]
		linx = w.coords(pil2)[6]


	if props[3] == '0':#outer pillows
		pil1 = w.create_rectangle(cw/2-b, ch/2-b, cw/2+b, ch/2+b, fill=colout, outline='white')
		pil5 = w.create_rectangle(cw/2-b, ch/2-b, cw/2+b, ch/2+b, fill=colout, outline='white')
		if props2[1] == '1':
			w.move(pil1, -(cw/2-linx+b), 0)
			w.move(pil5, rinx-cw/2+b, 0)
		elif props2[1] == '2':
			w.move(pil1, -(cw/2-linx+b-oh), 0)
			w.move(pil5, rinx-cw/2+b-oh, 0)
			w.tag_raise(pil1)
			w.tag_raise(pil5)
		elif props2[1] == '0':
			w.move(pil1, -(cw/2-linx+b-oh), 0)
			w.move(pil5, rinx-cw/2+b-oh, 0)
			w.tag_lower(pil1)
			w.tag_lower(pil5)

	else:
		pil1 = w.create_polygon(cw/2, ch/2-d, cw/2+d, ch/2, cw/2, ch/2+d, cw/2-d, ch/2, fill=colout, outline='white')
		pil5 = w.create_polygon(cw/2, ch/2-d, cw/2+d, ch/2, cw/2, ch/2+d, cw/2-d, ch/2, fill=colout, outline='white')
		if props2[1] == '1':
			w.move(pil1, -(cw/2-linx+d), 0)
			w.move(pil5, rinx-cw/2+d, 0)

		if props2[1] == '2':
			w.move(pil1, -(cw/2-linx+d-od), 0)
			w.move(pil5, rinx-cw/2+d-od, 0)
			w.tag_raise(pil1)
			w.tag_raise(pil5)
		if props2[1] == '0':	
			w.move(pil1, -(cw/2-linx+d-od), 0)
			w.move(pil5, rinx-cw/2+d-od, 0)
			w.tag_lower(pil1)
			w.tag_lower(pil5)

#INTERFACE
root = Tk() #main window
w = Canvas(root, bg="black", height=ch, width=cw) #canvas on which we display pillows
w.pack(fill='both')

but = Button(root, text="NEXT", command = next_comb)#graphical input
but2 = Button(root, text="BACK", command = back_comb)
but3 = Button(text="RANDOM", command= rand_comb)
ent = Entry(root)
but4 = Button(root, text='GO', command = gen_from_code)
but2.pack(side='left', fill='both')
but3.pack(side='left', fill='both')
but.pack(side='left', fill='both')
ent.pack(side='left', fill='both')
but4.pack(side='left', fill='both')

root.bind('<Left>', back_but) #keyboard bindings
root.bind('<Right>', next_but)
root.bind('<space>', rand_but)
root.bind('<Return>', ent_but)

#START TKINTER
root.mainloop() 
