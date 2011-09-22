def flatten_triangle(t):
    while len(t) > 1:
        t[-2] = [max(p + t[-1][i], p + t[-1][i + 1]) for i, p in enumerate(t[-2])]
        del t[-1]
    return t

with open('problem67_triangles.txt', 'r') as triangle_file:
    print(flatten_triangle([[int(entry) for entry in line.split(' ')] for line in triangle_file])[0][0])
