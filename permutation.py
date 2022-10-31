import numpy as np

def column_permutation(w):
    '''Algoritmo 3'''
    ii = 0
    jj = 0
    kk = 0
    ll = 0
    w0 = w
    M = 0
    M_copy = 0
    M0 = 0

    k = 0
    k_aux = 0

    for jj in range(len(w0[1,:])):
        for ii in range(len(w0[:,1])):

            if ii == jj:
                M = w0[ii:, jj:]
                

                for ll in range(len(M[1,:])): #ll é o índice das colunas da matriz M
                    for kk in range(M[:,1]): #kk é o índice das linhas da matriz M
                        k_aux = np.count_nonzero(M[kk:,jj])

                        if k_aux < k:
                            k = k_aux
                            ll = kk

                w0_copy = w0[:,jj].copy()
                w0[ii,:] = w0[ii+k-1,:]
                w0[ii+k-1,:] = w0_copy
    return w0
        

                
                    
w0 = np.array([[0,0,0,1],
             [1,1,1,1],
             [0,1,1,0],
             [1,0,1,0]])

M = column_permutation(w0)