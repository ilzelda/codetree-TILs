from collections import deque
from copy import deepcopy

N, M, K = map(int, input().split())

Turrets = [ list(map(int, input().split())) for _ in range(N)]

Logs = [ [0 for _ in range(M)] for _ in range(N)]

def compareMin(t1, t2):
    i1, j1 = t1
    i2, j2 = t2

    if Turrets[i1][j1] > Turrets[i2][j2]:
        return t2
    elif Turrets[i1][j1] < Turrets[i2][j2]:
        return t1
    else:
        if Logs[i1][j1] > Logs[i2][j2] :
            return t1
        elif Logs[i1][j1] < Logs[i2][j2] :
            return t2
        else:
            if i1 + j1 > i2 + j2:
                return t1
            elif i1 + j1 < i2 + j2:
                return t2
            else:
                if j1 > j2:
                    return t1
                else :
                    return t2

def findLeastSTR():
    is_first = True
    rtn_turret = (0, 0)

    for i in range(N):
        for j in range(M):
            if Turrets[i][j] == 0 : continue
            if is_first :
                rtn_turret = (i,j)
                is_first = False
                continue

            rtn_turret = compareMin(rtn_turret, (i,j))

    return rtn_turret

def raiseSTR(attacker):
    global Turrets

    Turrets[attacker[0]][attacker[1]] += N + M

def compareMax(t1, t2):
    i1, j1 = t1
    i2, j2 = t2

    if Turrets[i1][j1] > Turrets[i2][j2]:
        return t1
    elif Turrets[i1][j1] < Turrets[i2][j2]:
        return t2
    else:
        if Logs[i1][j1] > Logs[i2][j2] :
            return t2
        elif Logs[i1][j1] < Logs[i2][j2] :
            return t1
        else:
            if i1 + j1 > i2 + j2:
                return t2
            elif i1 + j1 < i2 + j2:
                return t1
            else:
                if j1 > j2:
                    return t2
                else :
                    return t1


def findMaxSTR(atk):
    is_first = True
    rtn_turret = (0, 0)

    for i in range(N):
        for j in range(M):
            if Turrets[i][j] == 0 : continue
            if (i,j) == atk : continue
            if is_first :
                rtn_turret = (i,j)
                is_first = False
                continue

            rtn_turret = compareMax(rtn_turret, (i, j))

    return rtn_turret

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def in_range(i,j):
    return 0<=i<N and 0<=j<M

min_dist = 1<<30
laser_turrets = []
visited = [ [False for _ in range(M)] for _ in range(N)]
def DFS(cur_i, cur_j, cur_dist, turrets, tgt):
    global min_dist, laser_turrets, visited

    if cur_i == tgt[0] and cur_j == tgt[1]:
        if min_dist > cur_dist:
            min_dist = cur_dist
            laser_turrets = deepcopy(turrets)
            if DEBUG : print(laser_turrets)
        return

    for d in range(4):
        next_i = cur_i + di[d]
        next_j = cur_j + dj[d]

        if not in_range(next_i, next_j):
            if d == 0:
                next_j = 0
            elif d == 1:
                next_i = 0
            elif d == 2:
                next_j = M - 1
            elif d == 3:
                next_i = N - 1

        if (next_i, next_j) in turrets : continue
        if Turrets[next_i][next_j] == 0 : continue
        if visited[next_i][next_j] : continue

        turrets.append( (next_i, next_j) )
        visited[next_i][next_j] = True

        DFS(next_i, next_j, cur_dist+1, turrets, tgt)

        visited[next_i][next_j] = False
        turrets.pop(-1)

def BFS(atk, tgt):
    global visited

    visited = [[False for _ in range(M)] for _ in range(N)]

    # (dist, dir)
    memo = [[ [1<<30, -1] for _ in range(M)] for _ in range(N)]
    memo[atk[0]][atk[1]][0] = 0

    q = deque()
    q.append(atk)
    visited[atk[0]][atk[1]] = True

    while len(q)>0:
        cur_i, cur_j = q.popleft()
        cur_dist, _ = memo[cur_i][cur_j]
        for d in range(4):
            next_i = cur_i + di[d]
            next_j = cur_j + dj[d]

            if not in_range(next_i, next_j):
                if d == 0:
                    next_j = 0
                elif d == 1:
                    next_i = 0
                elif d == 2:
                    next_j = M - 1
                elif d == 3:
                    next_i = N - 1


            if Turrets[next_i][next_j] == 0: continue
            if visited[next_i][next_j]: continue

            if memo[next_i][next_j][0] > cur_dist+1:
                memo[next_i][next_j] = (cur_dist+1, d)

            if (next_i, next_j) == tgt :
                return memo

            visited[next_i][next_j] = True
            q.append((next_i, next_j))

def make_list(atk, tgt, _memo):
    _list = []
    cur_i = tgt[0]
    cur_j = tgt[1]

    while( (cur_i, cur_j) != atk):
        _list.append( (cur_i, cur_j) )

        _, d = _memo[cur_i][cur_j]
        d = (d + 2) % 4
        cur_i = cur_i + di[d]
        cur_j = cur_j + dj[d]

        if cur_i < 0:
            cur_i = N-1
        if cur_j < 0:
            cur_j = M-1
        if cur_i > N-1:
            cur_i = 0
        if cur_j > M-1:
            cur_j = 0

    _list.append( (cur_i, cur_j) )

    return _list


def laserAttack(atk, tgt):
    global min_dist, laser_turrets, visited

    min_dist = 1 << 30
    laser_turrets = []
    visited = [[False for _ in range(M)] for _ in range(N)]

    # visited[atk[0]][atk[1]] = True
    # DFS(atk[0], atk[1], 0, [atk], tgt)

    memo = BFS(atk, tgt)
    if memo is not None:
        laser_turrets = make_list(atk, tgt, memo)

    if DEBUG : print("laser_turrets : ", laser_turrets)

    if len(laser_turrets)  >= 2 :
        laser_turrets.pop(0)
        laser_turrets.pop(-1)
        return True, laser_turrets
    else:
        return False, laser_turrets

def bombAttack(atk, tgt):
    bomb_di = [-1, -1, -1, +0, +1, +1, +1, +0]
    bomb_dj = [-1, +0, +1, +1, +1, +0, -1, -1]

    _turret_info = []
    for d in range(8):
        next_i = tgt[0] + bomb_di[d]
        next_j = tgt[1] + bomb_dj[d]

        if not in_range(next_i, next_j):
            if next_i < 0 : next_i = N-1
            if next_i > N-1 : next_i = 0
            if next_j < 0 : next_j = M-1
            if next_j > M-1 : next_j = 0

        if Turrets[next_i][next_j] == 0 : continue

        _turret_info.append((next_i, next_j))

    return _turret_info

def attacked(atk, tgt, _turret_info ):
    global Turrets

    damage = Turrets[atk[0]][atk[1]]

    Turrets[tgt[0]][tgt[1]] -= damage

    for i, j in _turret_info:
        Turrets[i][j] -= (damage//2)

def ready(_turret_info):
    global Turrets

    alive = 0

    for i in range(N):
        for j in range(M):
            Turrets[i][j] = max(Turrets[i][j], 0)

            if Turrets[i][j] == 0 : continue
            alive += 1
            if (i,j) in _turret_info : continue
            else : Turrets[i][j]+=1

    return alive

def debugTurrets(msg):
    print(msg, " : ")
    for row in Turrets:
        for n in row:
            print(f"{n:4d}", end=" ")
        print()

## main
# DEBUG = True
DEBUG = False

for k in range(1, K+1):
    if DEBUG : print(f"\n======{k}======")

    # 1
    attacker = findLeastSTR()
    if DEBUG : print("attacker : ", attacker)

    raiseSTR(attacker)
    if DEBUG :debugTurrets("after raise attacker")

    Logs[attacker[0]][attacker[1]] = k

    # 2
    target = findMaxSTR(attacker)
    if DEBUG : print("target : ", target)

    flag, turret_info = laserAttack(attacker, target)
    if not flag:
        if DEBUG : print("bomb")
        turret_info = bombAttack(attacker, target)
    else :
        if DEBUG : print("laser")

    attacked(attacker, target, turret_info)
    if DEBUG : debugTurrets("after attack")

    # 3, 4
    turret_info.append(attacker)
    turret_info.append(target)

    alive = ready(turret_info)
    if DEBUG : debugTurrets("ready")
    if alive == 1 : break

ans_turret = findMaxSTR((-1,-1))
print(Turrets[ans_turret[0]][ans_turret[1]])