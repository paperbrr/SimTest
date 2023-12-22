'''def gravity():

    global G_CONST

    for i in object.OBJECTS:
        for j in object.OBJECTS:
            if i != j and i.canCollide and j.canCollide and i not in j.gravCalcDone:
                i.gravCalcDone.append(j)
                riToj = j.coords - i.coords
                #rjToi = -1*(riToj)
                rMag = riToj.mag

                gForceiOnj = vpy.vector((G_CONST*i.mass*j.mass*riToj.x)/(rMag**3), (G_CONST*i.mass*j.mass*riToj.y)/(rMag**3), (G_CONST*i.mass*j.mass*riToj.z)/(rMag**3))
                gForcejOnI = vpy.vector(-1*gForceiOnj.x, -1*gForceiOnj.y, -1*gForceiOnj.z)

                i.applyForce(gForcejOnI)
                j.applyForce(gForceiOnj)'''