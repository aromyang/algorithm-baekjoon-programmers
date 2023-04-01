def solution(park, routes):
    now = ()
    row = len(park)
    col = len(park[0])

    for i in range(row):
        for j in range(col):
            if park[i][j] == 'S':
                now = (i, j)

    for r in routes:
        direction, distance = r.split()
        distance = int(distance)
        r, c = now[0], now[1]
        if direction == 'N' and now[0] - distance >= 0:
            for _ in range(distance):
                r -= 1
                if park[r][c] == 'X':
                    r = now[0]
                    break
        elif direction == 'S' and now[0] + distance < row:
            for _ in range(distance):
                r += 1
                if park[r][c] == 'X':
                    r = now[0]
                    break
        elif direction == 'W' and now[1] - distance >= 0:
            for _ in range(distance):
                c -= 1
                if park[r][c] == 'X':
                    c = now[1]
                    break
        elif direction == 'E' and now[1] + distance < col:
            for _ in range(distance):
                c += 1
                if park[r][c] == 'X':
                    c = now[1]
                    break
        now = (r, c)

    return now
