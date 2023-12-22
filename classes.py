from dependancies import vpy


class object:

    OBJECTS = []

    def __init__(self, radius:int, color:vpy.color, mass:int, static:bool, canCollide:bool):

        #init
        self.object = vpy.sphere(radius=radius, color=color)

        #props
        self.coords = self.object.pos 
        self.mass = mass
        self.radius = radius
        self.color = color

        #special props
        self.canCollide = canCollide
        self.static = static

        #motion stuff
        self.velocity = vpy.vector(0,0,0)
        self.netForceOn = vpy.vector(0,0,0)

        self.gravCalcDone = []

        object.OBJECTS.append(self)

    def moveTo(self, newPos:vpy.vector):
        oldPos = self.object.pos
        self.object.pos = newPos
        return oldPos

    def distanceFrom(self, object:object):
        return (object.coords - self.coords).mag
    
    def isColliding(self, object:object):
        return True if self.distanceFrom(object) <= self.radius + object.radius else False
    
    def applyForce(self, force:vpy.vector):
        self.netForceOn += force