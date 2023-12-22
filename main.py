#this is a comment

from classes import object
from dependancies import vpy, sleep
from utils import mulScalarVector


T_INT = 0.01
G_CONST = 6.67*(10**(-11))


xAxes = vpy.box(color=vpy.color.green, size=vpy.vector(200,0.2,0.2))
yAxes = vpy.box(color=vpy.color.red, size=vpy.vector(0.2,200,0.2))
zAxes = vpy.box(color=vpy.color.purple, size=vpy.vector(0.2,0.2,200))


def motion():

    global T_INT

    for i in object.OBJECTS:
        netForce = i.netForceOn

        #if netForce.mag != 0: print(netForce)

        acc = netForce/i.mass
        initialVel = i.velocity
        finalVel = initialVel + (acc * T_INT)
        displacement = initialVel*T_INT + vpy.vector(acc.x/2, acc.y/2, acc.z/2)*(T_INT**2)

        i.velocity = finalVel
        i.moveTo(i.coords+displacement)      


top = object(radius=1, color=vpy.color.blue, mass=1, static=False, canCollide=True)
bottom = object(2, vpy.color.cyan, mass=1, static=False, canCollide=True)

top.moveTo(vpy.vector(0,10,0))
bottom.moveTo(vpy.vector(0,2,0))

#top.applyForce(vpy.vector(0,-5,0))
#bottom.applyForce(vpy.vector(0,5,0))

top.velocity = vpy.vector(0,-1,0)
bottom.velocity = vpy.vector(0,1,0)

while True:
    vpy.sleep(T_INT)
    motion()
    collideCheck()