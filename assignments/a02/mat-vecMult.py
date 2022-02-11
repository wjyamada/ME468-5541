import argparse
import time
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Multiply Matrix by a Vector by using double for loop.')
    parser.add_argument('n', metavar='n', type=int, nargs='+',
                    help='vector size')
    args = parser.parse_args()
    [n] = args.n
    vals = np.random.uniform(-1,1,n*n)
    A = vals.reshape((n,n))
    b = np.ones(n)
    c = np.zeros(n).T

    t = []

    for i in range(20):
        ti = time.perf_counter()
        for i in range(n):
            for j in range(n):
                c[i] += A[i,j]*b[j]
        tf = time.perf_counter()
        t_perf = tf - ti
        t.append(t_perf)
    print(c[-1])
    print(np.mean(t))
    print(np.std(t))

    t2 = []
    for i in range(20):
        ti = time.perf_counter()
        c = A@b
        tf = time.perf_counter()
        t_perf = tf - ti
        t2.append(t_perf)
    print(c[-1])
    print(np.mean(t2))
    print(np.std(t2))

if __name__ == "__main__":
    main()
