import numpy as np

def column_permutation(w):
    '''Algoritmo 3'''
    ii = 0
    jj = 0
    w0 = w

    for ii in range(len(w0[1,:])):
        for jj in range(len(w0[:,1])):
            M = w0[ii:, jj:]

            for kk in range(len(M[:,1])):
                k = np.count_nonzero(w0[ii:,jj])

                
                    
w0 = np.array([[0,0,0,1],
             [1,1,1,1],
             [0,1,1,0],
             [1,0,1,0]])

M = column_permutation(w0)
