def naturalsize(count):
    fcount = float(count)
    k = 1024
    m = k * k
    g = m * k
    if fcount < k:
        return str(count) + 'B'
    if fcount >= k and fcount < m:
        return f'{fcount/k:.2f}KB'
    if fcount >= m and fcount < g:
        return f'{fcount/m:.2f}MB'
    return f'{fcount/g:.2f}GB'
