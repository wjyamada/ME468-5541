from turtle import position
import numpy as np
import matplotlib.pyplot as plt

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

def boxplot(X,Y1,Y2):
    ticks = [r'$2^9$', r'$2^{10}$', r'$2^{11}$',r'$2^{12}$',r'$2^{13}$']
    plt.figure()
    df = plt.boxplot(Y1,positions=np.array(range(5))*2.0-0.4,sym='', widths=0.6)
    nump = plt.boxplot(Y2,positions=np.array(range(5))*2.0+0.4, sym='', widths=0.6)
    set_box_color(df, '#D7191C') 
    set_box_color(nump, '#2C7BB6')
    plt.plot([], c='#D7191C', label='double-for')
    plt.plot([], c='#2C7BB6', label='numpy')
    plt.legend()

    plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    plt.xlim(-2, len(ticks)*2)
    plt.title("boxplot comparisons")
    plt.grid()
    plt.savefig("boxplot.png")
    plt.show()

def loglog(X,Y1,Y2):
    mu1 = np.mean(np.array(Y1),axis=1)
    sigma1 = np.std(np.array(Y1),axis=1)
    mu2 = np.mean(np.array(Y2),axis=1)
    sigma2 = np.std(np.array(Y1),axis=1)
    plt.figure()
    plt.plot(X,mu1,'-o',color="blue",label=r"double-for")
    plt.plot(X,mu2,'-o',color="red",label=r"numpy")
    plt.legend()
    plt.ylabel("Time (s)")
    plt.xlabel("n")
    plt.yscale('log',basey=10)
    plt.xscale('log',basex=2)
    plt.title('log-log plot')
    plt.grid()
    plt.savefig('loglog.png')
    plt.show()

def main():
    print("Loading data...")
    X = np.load("X.npy")
    print(f"X loaded with shape {X.shape}")
    method1 = np.load("out1.npy").tolist()
    print(f"Double for times loaded with shape {len(method1)}")
    method2 = np.load("out2.npy").tolist()
    print(f"Numpy times loaded with shape {len(method2)}")
    print("Generating plots...")
    boxplot(X,method1,method2)
    loglog(X,method1,method2)

if __name__ == "__main__":
    main()