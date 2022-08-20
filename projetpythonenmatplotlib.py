#PROJET PYTHON
#Importer les librairies
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from skimage import measure
from tkinter import *
a0=0.52 # = rayon de bohr
A=(1/a0)**(3/2) # Constante atomique
#On utilise les coordonnées sphériques et ses 3 composantes
def r(x,y,z): 
    return np.sqrt(x**2+y**2+z**2)
def theta(x,y,z):
    return np.arccos(z/r(x,y,z))
def phi(x,y,z):
    return np.arctan(y/x)
x,y,z = np.mgrid[-20:20:100j,-20:20:100j,-20:20:100j]#Matrice quadrillant toutes les valeurs spatiales

orbitale=input("Quel est le choix de l'orbitale ?")#On demande à l'utilisateur quelle OA il veut afficher

#1s
def rad1s(r):
    return A*2*np.exp(-r/a0)# Fonction radiale   
def FO1s(r,theta,phi):
    return rad1s(r)*(1/(2*np.sqrt(np.pi)))# Fonction d'onde
def Orb1s(r, theta, phi): # pour visualiser une OA, on s'interesse au carré de la probabilité de trouver un electron
    return FO1s(r,theta,phi)**2


#2s
def rad2s(r):
    return A/(2*np.sqrt(2))*(2-r/a0)*np.exp(-r/(2*a0))
def FO2s(r,theta,phi):
    return rad2s(r)*(1/2*np.sqrt(np.pi))
def Orb2s(r, theta, phi):
    return FO2s(r,theta,phi)**2

#2px
def rad2px(r):
    return A/(2*np.sqrt(6))*r/a0*np.exp(-(r/(2*a0)))
def FO2px(r,theta,phi):
    return rad2px(r)*np.sqrt(3)/(np.sqrt(8*np.pi))*np.sin(theta)*np.cos(phi)*np.sqrt(2)
def Orb2px(r, theta, phi):
    a=FO2px(r,theta,phi)**2
    return FO2px(r,theta,phi)**2
#2py
def FO2py(r,theta,phi):
    return rad2px(r)*np.sqrt(3)/(np.sqrt(8*np.pi))*np.sin(theta)*np.sin(phi)
def Orb2py(r, theta, phi):
    return FO2py(r,theta,phi)**2
#2pz
def FO2pz(r,theta,phi):
    return rad2px(r)*np.sqrt(3)/(2*np.sqrt(np.pi))*np.cos(theta)
def Orb2pz(r, theta, phi):
    return FO2pz(r,theta,phi)**2
#3s
def rad3s(r):
    return A*1/(9*np.sqrt(3))*(6-4*r/a0+4*r*r/(9*a0*a0))*np.exp(-r/(3*a0))
def FO3s(r,theta,phi):
    return rad3s(r)*1/(2*np.sqrt(np.pi))
def Orb3s(r, theta, phi):
    return FO3s(r,theta,phi)**2
#3pz
def rad3pz(r):
    return A*1/(9*np.sqrt(6))*2*r/(3*a0)*(4-2*r/(3*a0))*np.exp(-r/(3*a0))*r
def FO3pz(r,theta,phi):
    return rad3pz(r)*np.sqrt(3)/(2*np.sqrt(np.pi))*np.cos(theta)
def Orb3pz(r, theta, phi):    
    return FO3pz(r,theta,phi)**2
#3px
def FO3px(r,theta,phi):
    return rad3pz(r)*np.sqrt(3)/(2*np.sqrt(np.pi))*np.sin(theta)*np.cos(phi)
def Orb3px(r, theta, phi):    
    return FO3px(r,theta,phi)**2
#3py
def FO3py(r,theta,phi):
    return rad3pz(r)*np.sqrt(3)/(2*np.sqrt(np.pi))*np.sin(theta)*np.sin(phi)
def Orb3py(r, theta, phi):    
    return FO3py(r,theta,phi)**2
#3dz²
def rad3dz2(r):
    return A*1/(9*np.sqrt(30))*4*r*r/(9*a0*a0)*np.exp(-r/(3*a0))
def FO3dz2(r,theta,phi):
    return rad3dz2(r)*np.sqrt(5/16*np.pi)*(3*np.cos(theta)*np.cos(theta)-1)
def Orb3dz2(r, theta, phi):
    return FO3dz2(r,theta,phi)**2
#3dxz
def FO3dxz(r, theta, phi):
    return rad3dz2(r)*np.sqrt(15/16*np.pi)*np.sin(2*theta)*np.cos(phi)
def  Orb3dxz(r, theta, phi):
    return FO3dxz(r, theta, phi)**2
#3dxy
def FO3dxy(r, theta, phi):
    return rad3dz2(r)*np.sqrt(15/16*np.pi)*np.sin(theta)*np.sin(theta)*np.sin(2*phi)
def  Orb3dxy(r, theta, phi):
    return FO3dxy(r, theta, phi)**2
#3dyz
def FO3dyz(r, theta, phi):
    return rad3dz2(r)*np.sqrt(15/16*np.pi)*np.sin(2*theta)*np.sin(phi)
def  Orb3dyz(r, theta, phi):
    return FO3dyz(r, theta, phi)**2
#3dx²-y²
def FO3dx2y2(r, theta, phi):
    return rad3dz2(r)*np.sqrt(15/16*np.pi)*np.sin(theta)*np.sin(theta)*np.cos(2*phi)
def  Orb3dx2y2(r, theta, phi):
    return FO3dx2y2(r, theta, phi)**2

def plot(orbitale, nom, angle):
    o=orbitale(r(x,y,z),theta(x,y,z),phi(x,y,z))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    max_val = np.max(o)
    print(max_val)
    sommet,faces, normales, valeurs = measure.marching_cubes(o,max_val/100)
    ax.plot_trisurf(sommet[:,0], sommet[:,1],faces, sommet[:,2],cmap="inferno")
    plt.title("Visualisation de l'orbitale {0}".format(nom))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.view_init(*angle)    
    plt.show()
def visu(orbitale):
    dico={"1s": Orb1s, "2s": Orb2s,"2px": Orb2px, "2pz": Orb2pz, "2py":Orb2py, "3s": Orb3s, "3pz": Orb3pz, "3py": Orb3py, "3px": Orb3px, "3dz²": Orb3dz2, "3dxz": Orb3dxz, "3dxy": Orb3dxy,"3dyz": Orb3dyz, "3dx²-y²": Orb3dx2y2}
    dicoo={"1s": (10,35), "2s": (10,35),"2px":(0,90), "2py": (90,0), "2pz": (0,0),"3s": (10,35), "3pz": (0,0), "3px": (0,90), "3py": (90,0), "3dz²": (20,35), "3dxz": (0,90), "3dxy": (90,0),"3dyz": (0,0), "3dx²-y²": (90,0)}
    if "-p"in orbitale:
        plot(dico[orbitale.replace("-p","",1)], orbitale.replace("-p","",1), dicoo[orbitale.replace("-p","",1)])
    else:
        plot(dico[orbitale], orbitale,(10,35))
visu(orbitale)
