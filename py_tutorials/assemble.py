##import sys
##import os
##from os import environ
##sys.path.append(environ['NETGENDIR']+"/../lib")

##from libngspy import *

# being sloppy ....
# from libngspy.ngstd import *
# from libngspy.ngbla import *
# from libngspy.ngfem import *
# from libngspy.ngcomp import *
# from libngspy.ngsolve import *


from ngsolve import *

pde = comp.PDE("d1_square.pde")
# SetDefaultPDE (pde)
mesh = pde.Mesh()

v = pde.spaces["v"]
v.Update (heapsize=1000000)

lh = ngstd.LocalHeap (10000, "heap")

lam = fem.ConstantCF (4.8)
lap = fem.BFI (name="laplace", dim=2, coef=lam)



for i in v.Elements():
    fel = i.GetFE()    
    trafo = i.GetTrafo()
    mat = bla.Matrix(fel.ndof, fel.ndof)
    lap.CalcElementMatrix(fel, trafo, mat, i.GetLH())
    print ("Element matrix of element ", i, ":\n", mat)
    print ("dofs: ", i.dofs, "\n")


