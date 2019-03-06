from numpy import array, empty
from pylab import plot, show, xlabel, ylabel, linspace

def gaussian_Elim(A, v):
    '''
    solves the system of equations associated with the matrix A and vector v
    :param A: square matrix
    :param v: vector
    :return: vector containing the solutions to the system of eqns
    '''
    N = len(v)
    # Gaussian Elimination
    for m in range(N):

        # Divide by the diagonal element
        div = A[m,m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    # Backsubstitution
    x = empty(N, float)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i] * x[i]

    return x
