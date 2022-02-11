import argparse
import time
import numpy as np
import matplotlib.pyplot as plt

def m1(A,b,n,out):
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
    mu = np.mean(t)
    sigma = np.std(t)
    out.append(t)
    return (c[-1] , mu, sigma)

def m2(A,b,n,out):
    c = np.zeros(n).T
    t = []
    for i in range(20):
        ti = time.perf_counter()
        c = A@b
        tf = time.perf_counter()
        t_perf = tf - ti
        t.append(t_perf)
    mu = np.mean(t)
    sigma = np.std(t)
    out.append(t)
    return (c[-1] , mu, sigma)


def main():
    X = [2**9, 2**10, 2**11, 2**12, 2**13]
    n_try = 1
    # X = [1, 10]
    mu1 = []
    sigma1 = []
    mu2 = []
    sigma2 = []

    out1 = []
    out2 = []

    for n in X:
        print(n)
        vals = np.random.uniform(-1,1,n*n)
        A = vals.reshape((n,n))
        b = np.ones(n)
        _, mu, sigma = m1(A,b,n,out1)
        mu1.append(mu)
        sigma1.append(sigma)
        _, mu, sigma = m2(A,b,n,out2)
        mu2.append(mu)
        sigma2.append(sigma)
    

    if(n_try==0): #Question 1 plots
        plt.title('Linux - Intel i7-9750H - 32 GB')
        plt.errorbar(X,mu1,yerr=[i*3 for i in sigma1],color="blue",label=r"double-for$\pm 3\sigma$")
        plt.errorbar(X,mu2,yerr=[i*3 for i in sigma2],color="red",label=r"numpy$\pm 3\sigma$")
        plt.legend()
        plt.ylabel("Time (s)")
        plt.xlabel("n")
        plt.xscale('log',basex=2)
        plt.grid()
        plt.savefig('plot.png')

        np.save('X.npy',X)
        np.save('mu1.npy',mu1)
        np.save('simga1.npy',sigma1)
        np.save('mu2.npy',mu2)
        np.save('simga2.npy',sigma2)

    elif(n_try==1): #save data
        np.save("out1.npy",out1)
        np.save("out2.npy",out2)


if __name__ == "__main__":
    main()
