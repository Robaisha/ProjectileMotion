GlowScript 3.0 VPython

scene=canvas(background_color=color.white)
#Create objects
ground=box(pos=vector(0,-0.2,0), size=vector(10,0.4,2) , color=color.blue)
ball=sphere(pos=vector(-5,1.1,0), radius=0.5, color=color.orange, make_trail=True)
origin = sphere(color=color.white, opacity=0.4)
#========================================
#initial values
#axes
x_ax = curve(pos=[vector(-10,0,0),vector(10,0,0)],color=color.green)
y_ax = curve(pos=[vector(0,-10,0),vector(0,10,0)],color=color.yellow)
z_ax = curve(pos=[vector(0,0,-10),vector(0,0,10)],color=color.blue)
#================================================
r0=ball.pos
g=vector(0,-9.81,0)   #Constant gravitational acceleration
ball.mass=0.2         #mass of ball
v0=10  
theta=50*pi/180
v0_y=v0*sin(theta)
v0_x=v0*cos(theta)
ball.mom=ball.mass*v0*vector(cos(theta),sin(theta),0)
#===============================================
print("Initial velocity= ",v0,"m/s")
print("initial position= ",r0,"m")
print("Angle at which projectile occured",theta,"radians");
t=0
dt=0.02
#animations
#==============================================
while t<ball.pos.y>=1.1: 
 rate(100)              #100calculations per second
 fnet=ball.mass*g       #calculate force
 ball.mom=ball.mom+fnet*dt     #update momentum              
 ball.pos=ball.pos+ball.mom*dt/ball.mass     #update position
 t=t+dt                                   
#finalresults
#=================================================
print("final position= ",ball.pos,"m")
print("Time= ",t,"s")


