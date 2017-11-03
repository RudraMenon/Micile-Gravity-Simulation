from ez_graphics_09 import*
from ez_touchscreen_09 import*
from ez_ui_09 import *
import time,math,copy

GRAVITY_CONSTANT = 6.67384 * math.pow(10,-11)
CONSTANT_RATIO = 1000
speed = .01
class Planet:
    def __init__(self, mass,locX,locY,vel,force):
        self.mass, self.locX, self.locY,self.vel,self.force = int(mass),locX,locY,vel,force
        pass
#    get distance between planet and other object
    def calcRadius(self,other):
        deltaX = abs(self.locX-other.locX)*1000
        deltaY = abs(self.locY-other.locY)*1000
        radius = math.pow(math.pow(deltaX,2) + math.pow(deltaY,2),.5)
        return radius
#    use formula to calculate
    def calcGravForce(self,other):
        force = (GRAVITY_CONSTANT*self.mass*other.mass)/math.pow((self.calcRadius(other)),2)
        return force
        
    def forceVectors(self,other):
        radius = self.calcRadius(other)
        force = self.calcGravForce(other)
        forceX = (force * (other.locX - self.locX))/radius
        forceY = (force * (other.locY - self.locY))/radius
        return [forceX,forceY]
    def addForce(self,other):
        self.force[0] += self.forceVectors(other)[0]
        self.force[1] += self.forceVectors(other)[1]
#   return x and y acceleration vectors
    def accelCalc(self,force):
        accel = (force/self.mass)
        return accel
    def calcVel(self,accelX,accelY):
#        xDelta = (self.vel[0]*speed) + ((accelX*(speed**2))/2)
#        yDelta = (self.vel[1]*speed) + ((accelY*(speed**2))/2)
        xDelta = self.vel[0] + (accelX*speed)
        yDelta = self.vel[1] + (accelY*speed)
        return [xDelta,yDelta]
#    change position of planet and velocity vector
    def move(self):
        accelX = self.accelCalc(self.force[0])
        accelY = self.accelCalc(self.force[1])
        vel = self.calcVel(accelX,accelY)
        self.vel[0] = vel[0]
        self.vel[1] = vel[1]
        self.locX += self.vel[0]
        self.locY += self.vel[1]
    
    def drift(self):
        self.locX += self.vel[0]
        self.locY += self.vel[1]
        prin
        
moonMass = math.pow(10,22)
#               mass    x coord, y coord, [x velocity, y velocity]

objs = [Planet(5.972 * 10**24,400,240,[0,0],[0,0]),Planet(1000000000000000000000000,600,240,[0,-4.4],[0,0]),Planet(1000000000000000000000000,200,240,[0,4.4],[0,0])]
#objs = [Planet(5.972 * 10**24,200,240,[0,0],[0,0]),Planet(7* 10**23,600,240,[0,0],[0,0])]
clear_screen('black')
set_color('white')
fill_rect(700,430,100,50)
bg = capture_image(0,0,800,480)
bg2 = capture_image(0,0,800,480)
def getSize(mass):
        Density = 10000000000 #kg/m^3
        volume = mass/Density
        rad = ((3*volume)/(4*math.pi))
        rad = int(math.pow(rad,1/3.0)/CONSTANT_RATIO)
        return rad
def crash(planet1,planet2):
    print "CRASH!!!!"
    if planet1.mass != planet2.mass:
        if planet1.mass > planet2.mass:
            obj1 = planet1
            obj2 = planet2
        else:
            obj1 = planet2
            obj2 = planet1
    else:
        obj1 = planet1
        obj2 = planet2
    totalVel = [obj1.vel[0]+obj2.vel[0],obj1.vel[1]+obj2.vel[1]]
    obj1.vel[0] = ((obj1.mass*obj1.vel[0])+(obj2.mass*obj2.vel[0]))/(obj1.mass+obj2.mass)
    obj1.vel[1] = ((obj1.mass*obj1.vel[1])+(obj2.mass*obj2.vel[1]))/(obj1.mass+obj2.mass)
    index = objs.index(obj2)
    del objs[index]
    obj1.mass += obj2.mass
    run()

Saved = False
values = []
def on_btn_clicked(btn, release_point):
    global panel, counter,Saved,values
    mass1 =    float(panel.get_control('Mass1').text)
    mass1Exp = float(panel.get_control('Mass1Exp').text)
    mass = mass1 * (10**mass1Exp)
    values = [mass]
    Saved = True
panel = None
def add():
    global Saved,values,panel,objs
    set_color('white')
    fill_rect(700,430,100,50)
    curr_pic = capture_image(0,0,800,480)
    panel = create_panel(400,300,400,180)
    panel.add_textbox('Mass1',        100, 50, 100,  40, text='7')
    panel.add_textbox('Mass1Exp',     250, 50, 100,  40, text='22')
    panel.add_button( 'Save',          100, 100, 275,  40, text='SAVE', text_size=20, text_alignment='CENTER_CENTER',on_click_handler=on_btn_clicked)

    Saved = False
    
    while not Saved:
        if panel!= None:
            point = touchscreen_finger_point()
            panel.process_touch(point)
            time.sleep(0.05)
            
    mass = values[0]
    draw_image(curr_pic,0,0)

    loc = pickLoc(mass)
    xLoc = loc[0]
    yLoc = loc[1]
    vel = pickVel(xLoc,yLoc)
    objs.append(Planet(mass,xLoc,yLoc,vel,[0,0]))
    while touchscreen_finger_point() != None:
        pass
def pickLoc(mass):
    
    set_color('white')
    fill_rect(700,430,100,50)
    curr_pic = capture_image(0,0,800,480)
    bg = capture_image(0,0,800,480)
    locPicked = False
    xLoc = 0
    yLoc = 0
    while touchscreen_finger_point() != None:
        pass
    while not locPicked:
        set_drawing_image(curr_pic)
        touch_point = touchscreen_finger_point()
        set_color('black')
        set_text_size(30)
        set_text_alignment(LEFT_TOP)
        draw_text("PLACE",700,440)
        if touch_point != None:
            x = touch_point['x']
            y = touch_point['y']
            if x > 700 and y > 430:
                locPicked = True
            else:
                xLoc = x
                yLoc = y-15
                draw_image(bg,0,0)
                set_color('red')
                fill_circle(x,y-15,int(getSize(mass)))
        set_drawing_image(None)
        draw_image(curr_pic,0,0)
    return [xLoc,yLoc]
def pickVel(xLoc,yLoc):
    set_color('white')
    fill_rect(700,430,100,50)
    curr_pic = capture_image(0,0,800,480)
    bg = capture_image(0,0,800,480)
    xDelta = 0
    yDelta = 0
    while touchscreen_finger_point() != None:
        pass
    velPicked = False
    while not velPicked:
        set_drawing_image(curr_pic)
        
        set_color('black')
        set_text_size(50)
        set_text_alignment(LEFT_TOP)
        draw_text("AIM",700,440)
        touch_point = touchscreen_finger_point()
        if touch_point != None:
            x = touch_point['x']
            y = touch_point['y']
            if x > 700 and y > 430:
                velPicked = True
            else:
                xDelta = x-xLoc
                yDelta = y-yLoc
                draw_image(bg,0,0)
                set_color('red')
                draw_line(xLoc,yLoc,x,y)
        set_drawing_image(None)
        draw_image(curr_pic,0,0)
    return [xDelta/100,yDelta/100]
def run():
    global speed
    while True:
        touch_point = touchscreen_finger_point()
        if touch_point != None:
            # get the x and y coordinates of the touch

            x = touch_point['x']
            y = touch_point['y']
            if x > 710 and y > 430:
                add()
        else:
            set_drawing_image(bg)
            draw_image(bg2,0,0)
            set_color('black')
            set_text_size(50)
            set_text_alignment(LEFT_TOP)
            draw_text("ADD",700,440)
            if len(objs) == 1:
                size = getSize(objs[0].mass)
                objs[0].drift()
                if objs[0].vel == [0,0]:
                    set_color('white')
                else:
                    set_color('yellow')
                fill_circle(int(objs[0].locX),int(objs[0].locY),int(size))
            else:
                for obj1 in objs:
                    obj1.force = [0,0]
                    for obj2 in objs:
                        if obj2 != obj1:
                            obj1.addForce(obj2)
                            if obj1.calcRadius(obj2) < (getSize(obj1.mass)+getSize(obj2.mass)*1000):
                                crash(obj1,obj2)
                                return
                for obj1 in objs:
                    obj1.move()
                    size = getSize(obj1.mass)
                    set_color('yellow')
                    fill_circle(int(obj1.locX),int(obj1.locY),size)
                    
#                    TO TRACE MOVEMENT, UNCOMMENT THIS:
#                    set_drawing_image(bg2)
#                    set_color('white')
#                    fill_circle(int(obj1.locX),int(obj1.locY),1)
#                    set_drawing_image(bg)
    
    #***************************************************
            set_drawing_image(None)
            draw_image(bg,0,0)
            time.sleep(.001)
run()
        