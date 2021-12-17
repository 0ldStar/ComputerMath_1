import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


def y(_x):
    return np.cos(_x + 0.3) - _x ** 2


def y1(_x):
    return -np.sin(_x + 0.3) - 2 * _x


def newtonsMethod(_a, _b, func, derivative, eps):
    if func(_a) * func(_b) >= 0:
        return
    n = 1
    _x0 = (_a + _b) / 2
    xn = func(_x0)
    xn1 = xn - func(xn) / derivative(xn)
    while abs(xn1 - xn) > eps:
        xn = func(xn)
        xn1 = xn - func(xn) / derivative(xn)
        n = n + 1
    print("Count NM  = %d" % n)
    return xn1


def simplyIterationMethod(_a, _b, func, l, eps):
    if func(_a) * func(_b) >= 0:
        return
    n = 1
    _x0 = (_a + _b) / 2
    xn = func(_x0)
    xn1 = xn - func(xn) / l
    while abs(xn1 - xn) > eps:
        xn = func(xn)
        xn1 = xn - func(xn) / l
        n = n + 1
    print("Count SIM = %d" % n)
    return xn1


def halfDevisionMethod(_a, _b, func, eps):
    n = 1
    if func(_a) * func(_b) >= 0:
        return
    _x = (_a + _b) / 2
    _y = func(a)
    yn = func(b)
    while abs(_y - yn) > eps:
        n = n + 1
        _x = (_a + _b) / 2
        yn = _y
        _y = func(_x)
        if func(_a) * _y < 0:
            _b = _x
        else:
            _a = _x
    print("Count HDM = %d" % n)
    return _x


a = 0.0
b = 2.0
e = 10e-5

x0 = newtonsMethod(a, b, y, y1, e)
x1 = simplyIterationMethod(a, b, y, -2, e)
x2 = halfDevisionMethod(a, b, y, e)
x3 = opt.fsolve(y, 0)[0]

print("NewtonsMethod:           |   %.10f" % x0)
print("simplyIterationMethod:   |   %.10f" % x1)
print("halfDivisionMethod:      |   %.10f" % x2)
print("opt.fsolve:              |   %.10f" % x3)
print("epsilon                  |   %.10f" % e)

x = np.arange(a, b, 0.01)
plt.plot(x, y(x), "-")
plt.vlines(x0, -5, 2, colors="r")
plt.grid()
plt.show()
