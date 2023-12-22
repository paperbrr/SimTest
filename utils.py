from dependancies import vpy


def mulScalarVector(scalar:int or float, vector: vpy.vector):
    return vpy.vector(scalar*vector.x, scalar*vector.y, scalar*vector.z)