from copy import deepcopy
from collections import deque

K, M = map(int, input().split())

Wall = [ list(map(int, input().split())) for _ in range(5)]

Pieces = list(map(int, input().split()))

Piece_idx = 0

def circulateWall(center_i, center_j, degree):
    _wall = deepcopy(Wall)
    sub_wall = deepcopy([row[center_j-1:center_j+2]for row in _wall[center_i-1:center_i+2]])
    for rotate in range(degree // 90):
        rotated = [list(row)[::-1] for row in zip(*sub_wall)]
        sub_wall = rotated

    for i, row in enumerate(range(center_i-1, center_i+2)):
        _wall[row][center_j - 1:center_j + 2] = sub_wall[i]

    return _wall

def in_range(i,j):
    return 0<=i<5 and 0<=j<5

def searchWall(_wall):
    visited = [ [False for _ in range(5)] for _ in range(5)]

    q = deque()

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total_val = 0
    coords = []

    for i in range(5):
        for j in range(5):
            if visited[i][j] : continue

            visited[i][j] = True
            q.append((i, j))
            cur_val = _wall[i][j]
            count = 1
            tmp_coords = [(i,j)]

            while(len(q)>0):
                cur_i, cur_j = q.popleft()

                for d in range(4):
                    next_i = cur_i + di[d]
                    next_j = cur_j + dj[d]

                    if not in_range(next_i, next_j) : continue
                    if visited[next_i][next_j] : continue
                    if cur_val != _wall[next_i][next_j] : continue

                    visited[next_i][next_j] = True
                    q.append((next_i, next_j))
                    count+=1
                    tmp_coords.append((next_i,next_j))

            if count>=3 :
                total_val += count
                coords.extend(tmp_coords)

    return total_val, coords


def updateInfo(ans_info, new_info):
    if ans_info["val"] > new_info["val"] :
        return ans_info
    elif ans_info["val"] < new_info["val"] :
        return new_info

    elif ans_info["deg"] > new_info["deg"] :
        return new_info
    elif ans_info["deg"] < new_info["deg"] :
        return ans_info

    elif ans_info["c_j"] > new_info["c_j"] :
        return new_info
    elif ans_info["c_j"] < new_info["c_j"] :
        return ans_info

    elif ans_info["c_i"] < new_info["c_i"] :
        return ans_info
    else :
        return new_info


def findValue():
    max_val = -1
    info = {"val":-1} # center i, center j, degree, coords, val
    for c_i in range(1,4):
        for c_j in range(1, 4):
            for deg in [90, 180, 270]:
                _wall = circulateWall(c_i,c_j, deg)

        #         for row in _wall:
        #             print(*row)
        #         break
        #     break
        # break

                _val, _coords = searchWall(_wall)

                info = updateInfo(info, {"c_i" : c_i,
                                   "c_j" : c_j,
                                   "deg" : deg,
                                   "coords" : _coords,
                                   "val" : _val})

    return info

# def sort_coords(i, j):


def updateWall(_info):
    global Wall, Piece_idx

    sorted_coord = sorted(_info["coords"], key = lambda coord : (coord[1], -coord[0]) )

    for i, j in sorted_coord:
        Wall[i][j] = Pieces[Piece_idx]
        Piece_idx += 1

## main
for k in range(K):
    turn_value = 0
    nothing_to_found = False

    info = findValue()

    if info["val"] == 0 :
        nothing_to_found = True
        break


    turn_value += info["val"]
    Wall = circulateWall(info["c_i"], info["c_j"], info["deg"])

    while True:
        updateWall(info)
        _val, _coords = searchWall(Wall)

        if _val == 0: break

        turn_value += _val
        info["coords"] = _coords


    print(turn_value, end=" ")

