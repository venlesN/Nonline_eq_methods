from sympy import diff
import tracemalloc
import time


def function(func_str: str, x: float):
    return eval(func_str, {'x': x})


def bisectionMethod(a, b, e, strFunc):
    while abs(a - b) > 2 * e:
        x0 = (a + b) / 2
        fx = function(strFunc, x0)
        fa = function(strFunc, a)
        fb = function(strFunc, b)

        if fx * fa < 0:
            b = x0
        elif fx * fb < 0:
            a = x0
        else:
            if fa == 0:
                return a
            if fb == 0:
                return b
            if fx == 0:
                return x0

    return (b + a) / 2


def chordMethod(a, b, e, strFunc):
    x1 = 0
    x0 = -10000
    while abs(x1 - x0) > e:
        x0 = x1
        fa = function(strFunc, a)
        fb = function(strFunc, b)

        if fb != fa:
            x1 = a - fa * (b - a) / (fb - fa)
        else:
            x1 = a

        fx = function(strFunc, x1)

        if fx * fa < 0:
            b = x1
        elif fx * fb < 0:
            a = x1
        else:
            if fa == 0:
                return a
            if fb == 0:
                return b
            if fx == 0:
                return x1

    return a if abs(a) < abs(b) else b


def newtonMethod(a, b, e, strFunc):
    x1 = (a + b) / 2
    x0 = -10000
    while abs(x1 - x0) > e:
        x0 = x1
        fa = function(strFunc, a)
        fdx = function(str(diff(strFunc)), x0)
        fx0 = function(strFunc, x0)

        if fdx != 0:
            x1 = x0 - fx0 / fdx
        else:
            x1 = x0

        fx = function(strFunc, x1)

        if fx * fa < 0:
            b = x1
        elif fa != 0:
            if fx == 0:
                return x1
            a = x1
        else:
            return a

    return b if abs(a) < abs(b) else a


def compare():
    bisect = 0
    chord = 0
    newton = 0
    bisect_memory = 0
    chord_memory = 0
    newton_memory = 0

    for i in range(0, 1000):
        start_t = time.perf_counter()
        tracemalloc.start()
        bisectionMethod(a, b, e, strFunc)
        bisect += time.perf_counter() - start_t
        _, bi_memory_diff = tracemalloc.get_traced_memory()
        bisect_memory += bi_memory_diff
        tracemalloc.stop()

        start_t = time.perf_counter()
        tracemalloc.start()
        chordMethod(a, b, e, strFunc)
        chord += time.perf_counter() - start_t
        _, ch_memory_diff = tracemalloc.get_traced_memory()
        chord_memory += ch_memory_diff
        tracemalloc.stop()

        start_t = time.perf_counter()
        tracemalloc.start()
        newtonMethod(a, b, e, strFunc)
        newton += time.perf_counter() - start_t
        _, ne_memory_diff = tracemalloc.get_traced_memory()
        newton_memory += ne_memory_diff
        tracemalloc.stop()

    print("По методу бисекции:", bisect / 1000, "cекунд на решение",
          "\n                   ", bisect_memory / 1000, "байт на решение\n  Результат:", bisectionMethod(a, b, e, strFunc),
          "\n")
    print("По методу хорд:", chord / 1000, "cекунд на решение",
          "\n               ", chord_memory / 1000, "байт на решение\n  Результат:", chordMethod(a, b, e, strFunc),
          "\n")
    print("По методу Ньютона:", newton / 1000, "cекунд на решение",
          "\n                   ", newton_memory / 1000, "байт на решение\n  Результат:", newtonMethod(a, b, e, strFunc),
          "\n")


if __name__ == '__main__':
    strFunc = input("Введите функцию, используя x как переменную(пишите х на английском): ")

    a = float(input("a: "))
    b = float(input("b: "))
    e = float(input("e: "))

    print()
    compare()
