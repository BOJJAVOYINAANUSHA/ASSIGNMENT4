# -*- coding: utf-8 -*-
"""ASSIGNMENT4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttz5ucjuVuoqsV9ZW3DMig3gA4-C8HLZ
"""

# -*- coding: utf-8 -*-
"""parabola.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1Rs-sQcmWrZ5ukWAQpfxal4mnMS3OC21p
"""


#Functions related to line
import numpy as np


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

#Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

#Radius and centre of the incircle
#of triangle ABC
def icentre(A,B,C,k1,k2):
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  N=np.vstack((n1-k1*n2,n2-k2*n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = n1@(I-B)
  #Intersection
  return I,r

dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])

#Parabola for quadforms 2.45
#Code by B.ANUSHA
#Jun 12, 2021


 #Program to plot  a parabola
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linalg as LA

#if using termux
import subprocess
import shlex
#end if


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

len = 50

#Standard parabola

y1 = np.linspace(-5,5,len)
y2 = np.power(y1,2)

y = np.vstack((y1,y2))

#Given parabola parameters
V = np.array(([1,0],[0,0]))
u = np.array([0,-2])
F = 0

#Affine transformation
g = np.array([0,1])
vcm = g-u
vcp = g+u
A = np.vstack((V,vcp.T))
b = np.append(vcm,-F)
c = LA.lstsq(A,b,rcond=None)[0]
#c = np.array(c)
c = c.reshape(2,1)
print(c)

#Generating the parabola
x_par = y + c


#Tangent
p = np.array([1,0])
m = np.array(([-2,-1]))

#Generating points on the tangent T
T = line_dir_pt(m,p,-5,18)

#Plotting parabola
x=(y*y + 2)/3 
plt.plot(x_par[0,:],x_par[1,:],label='$x^2=4y$')


#plotting tangent T
plt.plot(T[0,:],T[1,:],label='Normal')

#Plotting all points
plt.plot(p[0], p[1], 'o')
plt.text(p[0] * (1 + 0.5), p[1] * (1 - 0.1) , 'p')

ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#plt.show()