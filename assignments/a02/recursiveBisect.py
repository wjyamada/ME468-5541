import numpy as np

def test_f(x):
    '''
    Evaluate the function

    @param x: input
    @return e**x-4
    '''
    return np.exp(x)-4

def find_root(xlow,xhi,it=1):
    if xhi-xlow < 10**(-6):
        return xlow
    
    xhalf = (xlow+xhi)/2

    val = test_f(xhalf)
    print(f'Iteration {it}: {xlow} {xhi} {xhalf} {val}')

    if(np.sign(test_f(xlow))==np.sign(val)):
        xstar = find_root(xhalf,xhi,it+1)
    else:
        xstar = find_root(xlow,xhalf,it+1)
    
    return xstar

def main():
    xstar = find_root(-0.2, 6.0)
    print(f'{xstar} {test_f(xstar)}')

if __name__=="__main__":
    main()