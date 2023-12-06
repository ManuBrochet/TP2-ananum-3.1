import numpy as np   



####################################################
# Produit A x pour la matrice de la partie 1
def produit1(x,ddata):
    alpha,h = ddata
    prodx = x * 0.0

    for i in range(1,len(x)-1):
        prodx[i] = x[i] * (2+alpha*(h**2)) - x[i-1] - x[i+1]

    prodx[0] = x[0] * (2+alpha*(h**2)) - x[1]
    prodx[len(x)-1] = x[len(x)-1] * (2+alpha*(h**2)) - x[len(x)-2]
    
    return prodx
####################################################


####################################################
# Produit M^{-1} x pour la matrice de la partie 1
def diag1(x,ddata):    
    alpha,h = ddata
    res = x* 0.
    
    res = x / (2+alpha*(h**2))
    
    return res
####################################################



    
####################################################
# Produit M^{-1} x pour la partie 2 (image)        
def diagImg(x,ddata):    
    mask,regu,Nx,Ny = ddata
    diagg = x*0.
    diagg += mask.reshape(-1)
    diagg += regu * 4.0 
    return x/diagg
####################################################



####################################################
# Produit A x pour la matrice de la partie 2 (image)    
def produitImg(x,ddata):
    mask,regu,Nx,Ny = ddata
    xxImg = x.reshape(Nx,Ny)
    # Completer ICI :
    # ...
    
    return newImg.reshape(-1)  
####################################################      
    
####################################################      
# Calcul du Laplacien discret partie 2 (image)    
def laplace(img):
    imgres = img*4.0 # Ici img est une matrice de taille Nx x Ny
    # Completer ICI :
    # ... 
    return imgres
####################################################          