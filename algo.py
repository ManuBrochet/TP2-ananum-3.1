import numpy as np
import copy
    


####################################################
# Méthode du gradient conjugué
def CG(produitAx, x0, bb, ddata, iteMax, eps):  
    # Initialisation :
    r = produitAx(x0,ddata) - bb
    w = np.copy(r)
    residus = [np.dot(r,r)]
    ite = 1
    x = np.copy(x0)
    w = r
    # Debut des iterations :
    while(residus[-1] >= eps*eps*residus[0] and iteMax > ite):
        print("Ite : ",ite," / ",iteMax,", residu : ",residus[-1]/residus[0])
        
        z = np.dot(r,w) / np.dot(produitAx(w,ddata),w)
        x = x - z*w
        r = r - z*produitAx(w,ddata)
        L = np.dot(produitAx(r,ddata),w) / np.dot(produitAx(w,ddata),w)
        w = r - L*w
        print("z = ", z, "L = ", L)

        residus.append(np.dot(r,r))
        #c'est bon jusque là
        ite += 1
    return [x,np.sqrt(residus)]    
####################################################    

####################################################
# Méthode de descente de gradient :
def DescenteGrad(produitAx, x0, bb, ddata, iteMax, eps):
    # Initialisation :
    r = produitAx(x0,ddata) - bb 
    residus = [np.dot(r,r)]
    ite = 1
    x = np.copy(x0)
    #comment trouver le pas optimale ?
    # Debut itérations :
    while(residus[-1] >= eps*eps*residus[0] and iteMax > ite):
        print("Ite : ",ite," / ",iteMax,", residu : ",residus[-1]/residus[0])
        
        alpha = np.dot(r,r)/np.dot(produitAx(r, ddata),r)

        x -= alpha*r

        r = produitAx(x, ddata) - bb
        
        residus.append(np.dot(r,r))
        ite += 1
    return [x,np.sqrt(residus)] 
####################################################


    
####################################################
# Méthode de Jacobi :    
def Jacobi(produitAx, produitMm1, x0, bb, ddata, iteMax, eps):  
    # Initialisation :
    r = produitAx(x0,ddata) - bb
    residus = [np.dot(r,r)]
    ite = 1
    x = np.copy(x0)
    while(residus[-1] >= eps*eps*residus[0] and iteMax > ite):
        print("Ite : ",ite," / ",iteMax,", residu : ",residus[-1]/residus[0])
        
        y = produitMm1(r, ddata)
        x -=y
        r = produitAx(x,ddata) - bb
        
        residus.append(np.dot(r,r)) 
        ite += 1
    return [x,np.sqrt(residus)]       



