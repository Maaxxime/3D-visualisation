#PROJET PYTHON

#Importer les librairies
import numpy as np
from mayavi import mlab


a0=0.52 #rayon de bohr
A=a0**(-3/2) # Constante utile pour la rédaction
#On utilise les coordonnées sphériques et ses 3 composantes
def r(x,y,z): 
    return np.sqrt(x**2+y**2+z**2)
def theta(x,y,z):
    return np.arccos(z/r(x,y,z))
def phi(x,y,z):
    return np.arctan(y/x)


#On demande à l'utilisateur quelle OA il veut afficher

orbitale=input("Quel est le choix de l'orbitale ?")
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
    return rad2px(r)*np.sqrt(3)/(np.sqrt(8*np.pi))*np.sin(theta)*np.sqrt(2)*np.cos(phi)
def Orb2px(r, theta, phi):
    return FO2px(r,theta,phi)**2
#2py
def FO2py(r,theta,phi):
    return rad2px(r)*np.sqrt(3)/(np.sqrt(8*np.pi))*np.sin(theta)*np.sin(phi)*np.sqrt(2)
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
x,y,z = np.mgrid[-20:20:100j,-20:20:100j,-20:20:100j]#Tableau 3D quadrillant toutes les valeurs spatiales

# On affiche nos valeurs avec mlab
def plot(orbitale):
    o=orbitale(r(x,y,z), theta(x,y,z), phi(x,y,z))
    mlab.figure()
    mlab.contour3d(o,contours=20,transparent=False)
    mlab.colorbar()
    mlab.outline()
    mlab.show()
def visu(orbitale):
    dico={"1s": Orb1s, "2s": Orb2s,"2px": Orb2px, "2pz": Orb2pz, "2py":Orb2py, "3s": Orb3s, "3pz": Orb3pz, "3py": Orb3py, "3px": Orb3px, "3dz²": Orb3dz2, "3dxz": Orb3dxz, "3dxy": Orb3dxy,"3dyz": Orb3dyz, "3dx²-y²": Orb3dx2y2}    
    plot(dico[orbitale])
visu(orbitale)