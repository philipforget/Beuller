with open('problem67_triangles.txt.bak', 'r') as triangle_file:
    print reduce(
        lambda r1, r2: map(
            lambda en: max(en[1] + r1[en[0]], en[1] + r1[en[0] + 1]),
            enumerate(r2)),
        [[int(entry) for entry in line.split(' ')] for line in triangle_file][::-1])[0]
