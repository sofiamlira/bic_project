import numpy as np
# from test import permutate_columns

def permutate_columns(matrix, ii, jj, k=None):
    w0 = matrix

    w0_copy1 = w0[:,jj].copy()
    w0_copy2 = w0[:,ii].copy()

    w0[:, ii] = w0_copy1
    w0[:, jj] = w0_copy2

    return w0

def non_zero_elements_of_column(matrix, string):

    if string == "column":
        M = matrix

        for ll in range(len(M[0,:])):
            k_aux = np.count_nonzero(M[:,ll])
                        
                        
            if ll==0:
                k = k_aux
                index = 0

            else:
                if k_aux < k:
                    k = k_aux
                    index = ll

        return k, index

    elif string == "row":
        return 0


def column_permutation(w):
    '''Algoritmo 3'''
    ii = 0
    jj = 0
    w0 = w

    m = int(np.log2(len(w0[0,:])))
    n = int(np.log2(len(w0[:,0])))

    k = 0
    k_aux = 0

    for jj in range(len(w0[0,:])):
        for ii in range(len(w0[:,0])):

            if ii == jj:
                M = w0[ii:, jj:]

                k, index = non_zero_elements_of_column(M, "column")
                cte = len(w0[0,:]) - len(M[0,:])
                index += cte #índice da matriz w0 (primeiro índice da matrix M)

                w0 = permutate_columns(w0, cte, index)

                test = non_zero_elements_of_column(M, "row")
                print(test)

                # w0_copy = w0[:,jj].copy()
                # w0[ii,:] = w0[ii+k-1,:]
                # w0[ii+k-1,:] = w0_copy
    return w0
        

                
                    
w0 = np.array([[0,0,0,1],
             [1,1,1,1],
             [0,1,1,0],
             [1,0,1,0]])

matriz_final = column_permutation(w0)
print(matriz_final)