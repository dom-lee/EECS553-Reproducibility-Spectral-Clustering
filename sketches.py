# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:03:16 2022

@author: sachg
"""


### As Rademacher variable is 1/sqrt{2} sub-gaussian


#### Code requirement , require a global (d,n) matrix A
### d is the dimension of every image
### m is the number of images

import numpy as np
import math
from sympy.stats import Rademacher

def Sketch(_type_="GA"):
    d= np.shape(A)[0] ### dimensionality of each node(image)
    m= np.shape(A)[1] #### number of nodes(images)
    delta=0.1 ## Sketch failure probability
    epsilon=0.4 ## should be less than 0.5
    epsilon_2 =epsilon**2 
    if _type_ =="GA":
        GA = Gaussian_JL(alpha=1,delta=delta,d=d,m=m,eps_2=epsilon_2)
        return GA
    if _type_ =="SG":
        SG_A = Sub_Gaussian_JL(alpha=12,delta=delta,d=d,m=m,eps_2=epsilon_2)
        return SG_A
    if _type_ == "SRHT":
        Z_A =zero_padding(d=d,m=m)
        d_new= np.shape(Z_A)[0]
        SRHT_A = SRHT(Z_A=Z_A,alpha=20,delta=delta,d=d_new,m=m,eps_2=epsilon_2)
        return SRHT_A
    if _type_ =="Sp_SRHT":
        Z_A =zero_padding(d=d,m=m)
        d_new= np.shape(Z_A)[0]
        sparsity_alpha=2
        Sp_SRHT_A = Sparse_RHT(Z_A=Z_A,alpha=20,delta=delta,sparsity_alpha=sparsity_alpha,d=d_new,m=m,eps_2=epsilon_2)
        return Sp_SRHT_A
    return
        
        
### Make Data suitable for Hadamard transformation
def zero_padding(d,m):
    degree = int(2**(np.ceil(math.log(d,2))) -d)
    zero_pad = np.zeros((degree,m))
    t_A = np.concatenate((A,zero_pad),axis=0)
    return t_A


## Gaussian Johnson Lindenstrauss Sketch
def Gaussian_JL(alpha,delta,d,m,eps_2):
    sketch_size = int(alpha*12*math.log(m/delta)/eps_2) ### Gives the smallest sketch size
    S = np.random.random((sketch_size,d))/math.sqrt(sketch_size)
    GA = S.dot(A)
    return GA



### Sub_Gaussian Johnson Lindenstrauss Sketch with Rademacher rabdom variable
def Sub_Gaussian_JL(alpha, delta,d,m,eps_2):
    ### Rademacher vector is 1/sqrt(log2) sub-gaussian
    sketch_size = int(alpha*((1/math.sqrt(np.log(2)))**4)*math.log(m/delta)/eps_2)
    S=np.random.binomial(1, 0.5, size=(sketch_size,d))
    S[S==0]=-1
    S=S/math.sqrt(sketch_size)
    SG_A = S.dot(A)
    return SG_A

### Subsampled Randomized Hadamard Transformation
def SRHT(Z_A,alpha,delta,d,m,eps_2):
    
    ### orthogonally randomize the subspace
    padded_dim =np.shape(Z_A)[0]
    sketch_size = int(alpha*(np.log(padded_dim/2)**2)*np.log(m/delta)/eps_2)
    diag = np.random.binomial(1,0.5,size=padded_dim)
    diag[diag==0]=-1
    RHT = np.zeros(np.shape(Z_A))
    
    ### Rotate and get randomized directions to flatten leverage scores
    for i in range(m):
        RHT[:,i] = Hadamard(diag*Z_A[:,i])
        
    ### Uniform subsampling on constant coherence subspace
    Sub_sample = np.random.choice(np.arange(padded_dim),sketch_size)
    SRHT_A = np.sqrt(padded_dim/sketch_size)*RHT[Sub_sample,:]
    return SRHT_A


### Fast JLT with Sparse Randomized Hadamard Transformation
def Sparse_RHT(Z_A,alpha,delta,sparsity_alpha,d,m,eps_2):
    
    print("Still to be coded")
    return
    ### orthogonally randomize the subspace
    padded_dim =np.shape(Z_A)[0]
    sketch_size =alpha*np.log(m/delta)/eps_2
    sparsity = sparsity_alpha*(np.log(padded_dim/delta))**2
    diag = np.random.binomial(1,0.5,size=padded_dim)
    diag[diag==0]=-1
    RHT = np.zeros(np.shape(Z_A))
    
    ### Rotate and get randomized directions to flatten leverage scores
    for i in range(m):
        RHT[:,i] = Hadamard(diag*Z_A[:,i])
    
    S = Sparse_Sub_gaussian(r=sketch_size,c=padded_dim,sparsity = sparsity)
    ### Sparse Sub-gaussian Sketching
    
    Sp_RHT_A = S.dot(RHT)
    
    return Sp_RHT_A

### Hadamard transformation
def Hadamard(x):
    ### Base-case
    if np.size(x)<=1:
        return x
    ### Divide-conquer
    else:
        a= x[0:int(np.size(x)/2)]+ x[int(np.size(x)/2):]
        b= x[0:int(np.size(x)/2)]- x[int(np.size(x)/2):]
        return np.concatenate((Hadamard(a), Hadamard(b)),axis=0)

def Hadamard_2(x):
    ### Base-case
    if np.shape(x)[0]<=1:
        return x
    ### Divide-conquer
    else:
        a= x[0:int(np.shape(x)[0]/2),:]+ x[int(np.shape(x)[0]/2):,:]
        b= x[0:int(np.shape(x)[0]/2),:]- x[int(np.shape(x)[0]/2):,:]
        return np.concatenate((Hadamard_2(a), Hadamard_2(b)),axis=0)
    

### Sparse Sub-gaussian Matrix-- complete this function later.
def Sparse_Sub_gaussian(r,c,sparsity):
    S = np.zeros((r,c))
    for i in range(r):
        idx = np.random.choice(np.arange(c),sparsity)   
    return
