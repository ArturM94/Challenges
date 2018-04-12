def hello_func(n):
    if n == 0:
        return
    else:
        print('Hello World')
        hello_func(n - 1)


hello_func(10)
