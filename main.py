import sympy as sm,matplotlib.pyplot as plt
import math
import tabulate
data=[];Data=[];x_val=[];y_val=[]
def newton(func,x,error_accepted):
    def f(x):
        f = eval(func)
        return f

    def diff(func):
        x = sm.symbols('x')
        result = sm.diff(func, x)
        return str(result)

    def fu(x):
        p=eval(diff(func))
        return p

    c=x
    x = x - (f(x) / fu(x))
    error=abs(c-x)
    n=0
    while error_accepted < error :
        c = x
        data.append(n)
        n=n+1
        data.append(str(x))
        x_val.append(round(x,2))
        x = x - (f(x) / fu(x))
        data.append(f(x))
        y_val.append(round(f(x),2))
        a=data.copy()
        Data.append(a)
        data.clear()
        error = abs(c - x)
    print("The root is %0.4f" %x)
newton('3*x**2-1',2,0.001)
print(tabulate.tabulate(Data,headers=['x','f(x)'],tablefmt='fancy_grid'))

plt.style.use('seaborn')
plt.title("Newton Rapson",color='lime')
plt.plot(x_val,y_val,color='deepskyblue',linewidth=1,marker='*',markersize=8,label='f(x)')
plt.legend()
plt.xlabel('x axis',color='red')
plt.ylabel('y axis',color='red')
plt.show()