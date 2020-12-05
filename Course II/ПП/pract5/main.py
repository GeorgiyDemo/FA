# program template for Spaceship
import simpleguitk as simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.thrust = False
        
    def draw(self,canvas):
        
        if self.thrust :
            
            t=90
            ship_thrust_sound.play()
            
            canvas.draw_image(self.image,(self.image_center[0]+t,self.image_center[1]),self.image_size,self.pos,self.image_size,self.angle)

        else :
            ship_thrust_sound.rewind()
            canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)

    def update(self):
        
        self.angle += self.angle_vel 
        
        self.pos[0]=(self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1]=(self.pos[1] + self.vel[1]) % HEIGHT	
        
        fv = angle_to_vector(self.angle)
        
        if self.thrust:
            self.vel[0] += fv[0]/10
            self.vel[1] += fv[1]/10
            
        self.vel[0] *= (1-.01)
        self.vel[1] *= (1-.01)
         
        
    def incAv(self):
        
        self.angle_vel -= .1
        
    def decAv(self):
        
        self.angle_vel += .1   
        
    def setAv(self):
        self.angle_vel = 0
        
    def setThrustOn(self,val):
        self.thrust = val
        
        if self.thrust :
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
        
    def getPosition(self):
        return self.pos
    
    def getRadius(self):
        return self.radius    
        
    def shoot(self):
        
        if not started:
            return 
        global missile_group
        vel=[0,0]
        fw = angle_to_vector(self.angle)
        vel[0] = self.vel[0] + fw[0]*5
        vel[1] = self.vel[0] + fw[1]*5
        missile_pos = [self.pos[0] + fw[0] *40 , self.pos[1] + fw[1] *40] 
        a_missile = Sprite(missile_pos,vel, 0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
        #a_missile.update()
        
        
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
            
    def getPosition(self):
        return self.pos
    
    def getRadius(self):
        return self.radius
   
    def draw(self, canvas):
        
        if self.animated :
            canvas.draw_image(self.image, [self.image_center[0] + self.age * self.image_size[0], self.image_center[1]], self.image_size,
                          self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)
    
    def update(self):
        self.angle += self.angle_vel 
            
        self.pos[0]=(self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1]=(self.pos[1] + self.vel[1]) % HEIGHT	
        
        self.age += 1
        
        if self.age > self.lifespan :
            return True
        else :
            return False
        
      
    def collide(self, other_object):
        dist = math.pow((self.getPosition()[0] - other_object.getPosition()[0]), 2) + math.pow((self.getPosition()[1] - other_object.getPosition()[1]), 2)
        dist = math.pow(dist, 0.5)
        if self.getRadius() + other_object.getRadius() > dist:
            return True
        return False
        
        
            
            
rock_group = set([])
missile_group = set([])
explosion_group = set([])
           
def draw(canvas):
    global time,score,rock_group,lives,my_ship,missile_group,started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    str1 = "Score: " + str(score)
    str2 = "Lives: " + str(lives)
    canvas.draw_text(str(str2),[30,20],20,'white')
    canvas.draw_text(str(str1),[700,20],20,'white')
    
    
    # draw ship and sprites
    my_ship.draw(canvas)
    #a_rock.draw(canvas)
    #a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    #a_rock.update()
    #a_missile.update()
    
    if lives <= 0:
        started = False
        soundtrack.pause()
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
        my_ship.setThrustOn(False)
        
        for sprite in set(rock_group):
            rock_group.remove(sprite)
        
        for sprite in set(missile_group):
            missile_group.remove(sprite)
            
        for element in set(explosion_group):
            explosion_group.remove(element)     
        
    if not started :
        canvas.draw_image(splash_image,splash_info.get_center(),splash_info.get_size(),[WIDTH/2,HEIGHT/2],splash_info.get_size()  )
    
    
    if started :
        soundtrack.play()
        process_sprite_group(rock_group,canvas)
        process_sprite_group(missile_group,canvas)
        process_sprite_group(explosion_group,canvas)
    
    if group_collide(rock_group,my_ship) :
        lives -= 1
        
    score += group_group_collide(rock_group,missile_group)    
            
# timer handler that spawns a rock  


def rock_spawner():
    global rock_group,my_ship
    
    
    
    a_rock = Sprite([random.choice(range(WIDTH)), random.choice(range(HEIGHT))], [1, 1],0.1,random.choice( [-0.1,0.1]), asteroid_image, asteroid_info)

    
    if len(rock_group) < 13 and dist(a_rock.getPosition(),my_ship.getPosition()) > 70 and started:
                rock_group.add(a_rock)
        


def click(pos):
    global started,lives,score
    
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.rewind()
        lives = 3
        score = 0
        
        
        
def process_sprite_group(s,canvas):
    
    for sprite in set(s) :
        sprite.draw(canvas)
        if sprite.update() :
            s.remove(sprite)
    
    
def group_collide(s,other_object):
     
    for sprite in set(s) :
        
        if sprite.collide(other_object) :
            s.remove(sprite)
            explosion_pos = sprite.getPosition()
            explosion_vel = [0, 0]
            explosion_avel = 0
            explosion = Sprite(explosion_pos, explosion_vel, 0, explosion_avel, explosion_image, explosion_info)
            explosion_group.add(explosion)
            explosion_sound.play()
            return True
        
    return False


def group_group_collide(group1,group2):

    count = 0	
    for sprite in group1:
        if group_collide(group2,sprite) :
            group1.discard(sprite)
            count += 1
            
    return count
        
def keydown(key):
    
    if not started :
        return
    
    if key == 37 :
        my_ship.incAv()
        
    if key == 39:
        my_ship.decAv()
        
    if key ==38  :
        my_ship.setThrustOn(True)
        
    if key == 32 :
        my_ship.shoot()
        
def keyup(key):
    
    if not started :
        return
    
    if key == 37 or key == 39 :
        my_ship.setAv()
    
    if key == 38 :
        my_ship.setThrustOn(False)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0.1, -0.1, asteroid_image, asteroid_info)
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
