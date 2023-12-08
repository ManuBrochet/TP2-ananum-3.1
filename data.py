import numpy as np   



####################################################
# Produit A x pour la matrice de la partie 1
def produit1(x,ddata):
    alpha,h = ddata
    prodx = x * 0.0

        
    prodx[1:len(x)-1] = x[1:len(x)-1] * (2+alpha*(h**2)) - x[0:len(x)-2] - x[2:len(x)]

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
    N = Nx*Ny
    
    newImg = np.zeros(np.shape(xxImg))

    # l'intérieur de la matrice 
    newImg[1:Nx-1, 1:Ny-1] = mask[1:Nx-1, 1:Ny-1]*xxImg[1:Nx-1, 1:Ny-1] + regu*(4*xxImg[1:Nx-1, 1:Ny-1]\
        - xxImg[:Nx-2, 1:Ny-1] - xxImg[1:Nx-1, :Ny-2] - xxImg[2:Nx, 1:Ny-1] - xxImg[1:Nx-1, 2:Ny])

    # la ligne l=0 (sans les coins)
    newImg[0,1:Ny-1] = mask[0,1:Ny-1]*xxImg[0,1:Ny-1] + regu*(4*xxImg[0,1:Ny-1]\
        - xxImg[0, 2:Ny] - xxImg[1, 1:Ny-1] - xxImg[0, 0:Ny-2])

    # la ligne l=Nx (sans les coins)
    newImg[Nx-1,1:Ny-1] = mask[Nx-1,1:Ny-1]*xxImg[Nx-1,1:Ny-1] + regu*(4*xxImg[Nx-1,1:Ny-1]\
        - xxImg[Nx-1, 2:Ny] - xxImg[Nx-2, 1:Ny-1] - xxImg[Nx-1, 0:Ny-2])

    # la colonne c=0 (sans les coins)
    newImg[1:Nx-1,0] = mask[1:Nx-1,0]*xxImg[1:Nx-1,0] + regu*(4*xxImg[1:Nx-1,0] \
        - xxImg[1:Nx-1,1]  - xxImg[0:Nx-2,0]  - xxImg[2:Nx, 0])

    #la colonne c=Ny (sans les coins)
    newImg[1:Nx-1,Ny-1] = mask[1:Nx-1,Ny-1]*xxImg[1:Nx-1,Ny-1] + regu*(4*xxImg[1:Nx-1,Ny-1] \
        - xxImg[1:Nx-1,Ny-2]  - xxImg[0:Nx-2,Ny-1]  - xxImg[2:Nx, Ny-1])

    # Les coins
    newImg[0,0] = mask[0,0]*xxImg[0,0] + regu*(4*xxImg[0,0] \
        - xxImg[0,1]  - xxImg[1,0])

    newImg[Nx-1 , Ny-1] = mask[Nx-1 , Ny-1]*xxImg[Nx-1 , Ny-1] + regu*(4*xxImg[Nx-1 , Ny-1] \
        - xxImg[Nx -2 , Ny-1]  - xxImg[Nx-1 , Ny-2])

    newImg[0 , Ny-1] = mask[0 , Ny-1]*xxImg[0 , Ny-1] + regu*(4*xxImg[0 , Ny-1] \
        - xxImg[1 , Ny-1]  - xxImg[0 , Ny-2])

    newImg[Nx-1 , 0] = mask[Nx-1 , 0]*xxImg[Nx-1 , 0] + regu*(4*xxImg[Nx-1 , 0] \
        - xxImg[Nx -2 , 0]  - xxImg[Nx-1 , 1])

    
    


    
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