import numpy as np       
            
def householder(w):
    '''Algoritmo 2'''
    ii = 0   #indices of lines of the matrix
    jj = 0   #indices of columns of the matrix
    w0 = w   #matrix
    w0_copy = 0

    m = int(np.log2(len(w0[1,:])))
    n = int(np.log2(len(w0[:,1])))
    

    k = 0 #Número de elementos não nulos

    print(w0)

    for jj in range(len(w0[1,:])): #percorre colunas
        k=0
        w0_sum=0

        for ii in range(len(w0[:,1])): #percorre todas as linhas a partir de zero
#            print(np.count_nonzero(w0[ii:,jj]))
            k = np.count_nonzero(w0[ii:,jj]) #

            if k!=0:
                w0_copy = w0[ii,:].copy()
                w0[ii,:] = w0[ii+k-1,:]
                w0[ii+k-1,:] = w0_copy

                ii = ii+k
                k=0

            if jj<(2**m - 1):
                jj += 1
                break #COM OU SEM BREAK??
            
            
            
            print(w0)   
    
    return w0

w0 = np.array([[0,0,0,1],
             [1,1,1,1],
             [0,1,1,0],
             [1,0,1,0]])

M = householder(w0)
print(M)