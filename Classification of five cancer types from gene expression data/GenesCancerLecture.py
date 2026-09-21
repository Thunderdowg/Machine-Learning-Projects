# -*- coding: utf-8 -*-

# Adresse des deux fichiers de donnees
# https://drive.google.com/drive/folders/14ZtZtNNZX3O8LSjIoVSOkYdJkaW68evL

import numpy as np

print("N'oubliez pas de mettre votre numero d'etudiant") 
etudiant = 100 # nombre à  remplacer par votre numéro d'etudiant
np.random.seed(etudiant)

# On lit la premiere ligne pour obtenir le nombre de colonnes
X = np.loadtxt("data.csv",max_rows=1,delimiter=",",dtype=str)
nvars=len(X)-1

# Lecture des donnees correpondant a la moitie des individus.
print("Sont lues les donnees correpondant aux trois quarts des individus",
      "(tiree aleatoirement sur la base de votre numero d'etudiant)")
X = np.loadtxt("data.csv",skiprows=1,delimiter=",")
nech=3*X.shape[0]//4
y =np.loadtxt("labels.csv",delimiter=",",skiprows=1,dtype=str)
per=np.random.permutation(X.shape[0])[:nech]
X,y = X[per,:], y[per,1]
print("Nombre de lignes, nombre de colonnes : ",X.shape)

# Elimination des variables constantes
l=np.std(X,axis=0)>1.e-8
X=X[:,l]
print("Nombre de lignes et colonnes, apres elimination des variables constantes: ",X.shape)


