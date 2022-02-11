import argparse
import numpy as np

def merge(A,B):
    '''
    Merge two 1D arrays while sorting
    
    @param A: 1D array of int
    @param B: 1D array of int
    @return C: Sorted merge between A and B 
    '''
    C = []
    
    lenA = len(A)
    lenB = len(B)

    i=0
    j=0

    while((i<lenA) and (j<lenB)):
        if(A[i]<B[j]):
            C.append(A[i])
            i +=1
        else:
            C.append(B[j])
            j+=1

    if(i<lenA):
        C.extend(A[i:])
    else:
        C.extend(B[j:])
    
    return C

def mergeSort(A):
    '''
    Merge Sort algorithm

    @param A: 1D array
    @return M: Sorted array
    '''
    n = len(A)
    half = int(n/2)
    if(n==1):
        return A
    
    P1= mergeSort(A[:half])
    P2= mergeSort(A[half:])
    M = merge(P1,P2)

    return M



def main():
    '''
    Assignment 2 Question 2: MergeSort implementation
    python3 sortME468.py n_elems

    @param n_elems: size of the vector to be randomly generated and sorted
    '''
    parser = argparse.ArgumentParser(description='MergeSort')
    parser.add_argument('n_elems', metavar='n_elems', type=int, nargs='+',
                    help='size of vector to be sorted')
    args = parser.parse_args()
    n_elems = args.n_elems

    A = np.random.randint(0,100,n_elems)
    print(f'{A[0]} {A[-1]}')
    
    M = mergeSort(A)
    print(f'{M[0]} {M[-1]}')


if __name__ == "__main__":
    main()