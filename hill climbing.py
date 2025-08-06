def f(x):
    return -x**2 + 10*x

def hill_climb(start, step_size=0.1, max_iter=1000):
    current = start
    for _ in range(max_iter):  # loop for a max of max_iter steps
        next_x = current + step_size
        if f(next_x) > f(current):
            current = next_x
        else:
            break  
    return current, f(current)

result_x, result_f = hill_climb(start=0)
print("Local maximum at x =", round(result_x, 2))
print("Maximum value f(x) =", round(result_f, 2))
