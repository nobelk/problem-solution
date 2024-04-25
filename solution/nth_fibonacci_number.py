def getNthFib(n):
    # Write your code here.
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 1
    else:
        values = [0, 1, 1]
        for n in range(3,n):
            values.append(values[n-2] + values[n-1])
    return values[n]