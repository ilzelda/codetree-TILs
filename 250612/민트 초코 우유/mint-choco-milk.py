from collections import deque
from functools import cmp_to_key

N, T = map(int, input().split())

class Person:
    def __init__(self, _b=0):
        self.b = _b
        self.p = [0, 0, 0]

Prefer = [ list(input().strip()) for _ in range(N)]
Belief = [ list(map(int, input().split())) for _ in range(N)]
People = [ [ Person() for _ in range(N)] for _ in range(N) ]
# print(Prefer)
# print(Belief)

# init
for i in range(N):
    for j in range(N):
        if Prefer[i][j] == 'T':
            People[i][j].p[0] = 1
        elif Prefer[i][j] == 'C':
            People[i][j].p[1] = 1
        else :
            People[i][j].p[2] = 1

        People[i][j].b = Belief[i][j]

def increaseBelief():
    global People

    for i in range(N):
        for j in range(N):
            People[i][j].b += 1

di = [-1, 1,  0, 0]
dj = [ 0, 0, -1, 1]

def in_range(i,j):
    return 0<=i<N and 0<=j<N

def makeGroup():
    visited = [ [False for _ in range(N)] for _ in range(N) ]

    groups = []

    for start_i in range(N):
        for start_j in range(N):
            if visited[start_i][start_j] : continue

            _group = [(start_i, start_j)]

            q = deque()

            visited[start_i][start_j] = True
            q.append((start_i, start_j))
            cur_val = People[start_i][start_j].p
            while(len(q) > 0):
                cur_i, cur_j = q.popleft()

                for d in range(4):
                    next_i = cur_i + di[d]
                    next_j = cur_j + dj[d]

                    if not in_range(next_i, next_j) : continue
                    if visited[next_i][next_j] : continue
                    if cur_val != People[next_i][next_j].p : continue

                    visited[next_i][next_j] = True
                    _group.append((next_i, next_j))
                    q.append((next_i, next_j))

            groups.append(_group)

    return groups

def selectChief(_groups):

    chiefs = []

    for G in _groups:
        chief_i, chief_j = G[0]

        for i, j in G:
            update_flag = False
            if People[i][j].b > People[chief_i][chief_j].b:
                update_flag = True
            elif People[i][j].b == People[chief_i][chief_j].b:
                if i < chief_i :
                    update_flag = True
                elif i == chief_i :
                    if j < chief_j :
                        update_flag = True

            if update_flag :
                chief_i = i
                chief_j = j

        chiefs.append((chief_i, chief_j, People[chief_i][chief_j].b))

    return chiefs

def updateBelief(_groups, _chiefs):
    global People

    for i, G in enumerate(_groups):
        chief_i, chief_j, _ = _chiefs[i]
        for i, j in G:
            if (i,j) != (chief_i, chief_j):
                People[i][j].b -= 1
            else :
                People[i][j].b += (len(G) - 1)

def compareGroup(idx1, idx2):
    p1 = People[idx1[0]][idx1[1]]
    p2 = People[idx2[0]][idx2[1]]

    if sum(p1.p) > sum(p2.p) : # 그룹으로 정렬
        return 1
    elif sum(p1.p) == sum(p2.p):  # 같은 그룹이라면
        if p1.b < p2.b:
            return 1
        elif p1.b == p2.b:
            if idx1[0] > idx2[0] :
                return 1
            elif idx1[0] == idx2[0]:
                if idx1[1] > idx2[1]:
                    return 1
                else :
                    return -1
            else:
                return -1
        else :
            return -1

    else :
        return -1

def sortChief(_chief_list):
    sorted_chiefs = sorted(_chief_list, key=cmp_to_key(compareGroup))
    return sorted_chiefs

def spread(_chief_list):
    global People

    blocked = []

    for n, (i, j, _) in enumerate(_chief_list):
        if (i, j) in blocked : continue

        dir = People[i][j].b % 4

        x = People[i][j].b - 1
        People[i][j].b = 1

        next_i = i + di[dir]
        next_j = j + dj[dir]

        while(in_range(next_i, next_j)):
            if People[i][j].p != People[next_i][next_j].p :
                blocked.append((next_i, next_j))
                y = People[next_i][next_j].b
                if x > y : # 강한전파
                    People[next_i][next_j].p = People[i][j].p
                    x -= (y+1)
                    People[next_i][next_j].b += 1
                    if x <= 0 : break

                else : # 약한전파
                    for p_idx in range(3):
                        if People[i][j].p[p_idx] == 1:
                            People[next_i][next_j].p[p_idx] = 1
                    People[next_i][next_j].b += x
                    x = 0
                    break


            next_i += di[dir]
            next_j += dj[dir]

        if DEBUG : printPeople(f"전파 후({n}) : ({(_chief_list[n][0], _chief_list[n][1])})")

def printAnswer():
    # TCM, TC, TM, CM, M, C, T
    ans = [ 0 for _ in range(7)]

    for i in range(N):
        for j in range(N):
            prefer = makePrefer(People[i][j])
            b = People[i][j].b
            if prefer == "TCM": ans[0] += b
            elif prefer == "TC": ans[1] += b
            elif prefer == "TM": ans[2] += b
            elif prefer == "CM": ans[3] += b
            elif prefer == "M": ans[4] += b
            elif prefer == "C": ans[5] += b
            elif prefer == "T": ans[6] += b

    print(*ans)


###############################
def makePrefer(P):
    prefer = ""
    p_list = ['T', 'C', 'M']

    for i in range(3):
        if P.p[i] == 1: prefer += p_list[i]

    return prefer

def printPeople(msg):
    print(msg)


    for row in People:
        for P in row:
            prefer = makePrefer(P)

            print(f"[{prefer:>3}:{P.b:2d}]", end=' ')
        print()
    print(DIVIDER)

def printGroups(msg, _groups):
    print(msg)
    for i, G in enumerate(_groups):
        print(f"{i}:",end='')
        print(G)
    print(DIVIDER)

def printCheif(msg, _chief_list):
    print(msg)
    print(_chief_list)
    ijs = [(i,j) for i,j,b in _chief_list]
    p_list = ['T', 'C', 'M']

    for _i, row in enumerate(People):
        for _j, P in enumerate(row):
            is_chief = ' '
            if (_i,_j) in ijs: is_chief = "@"

            prefer = ""
            for i in range(3):
                if P.p[i] == 1: prefer += p_list[i]

            print(f"[{is_chief}{prefer:>3}:{P.b:2d}]", end=' ')
        print()
    print(DIVIDER)

def printsorted(msg, _chief_list):
    print(DIVIDER)
    print(msg)

    for n, (i, j, _) in enumerate(_chief_list):
        print(f"[{n+1}] {makePrefer(People[i][j]):>3}- B={People[i][j].b:2d},{(i,j)}" )

    print(DIVIDER)


DEBUG = False
# DEBUG = True
DIVIDER = "=============================================="
if DEBUG : printPeople("초기 신앙")

for _ in range(T):
    ## 아침 ##
    increaseBelief()
    if DEBUG : printPeople("아침")

    ## 점심 ##
    # print([True, True, False] == [True, True, False])
    # print([True, True, False] == [True, False, False])
    groups = makeGroup()
    if DEBUG : printGroups("그룹짓기",groups)

    chief_list = selectChief(groups)
    if DEBUG : printCheif("대표", chief_list)

    updateBelief(groups, chief_list)
    if DEBUG : printPeople("대표 증가")

    ## 저녁 ##
    chief_list = sortChief(chief_list)
    if DEBUG : printsorted("대표 순서 정렬", chief_list)

    spread(chief_list)

    ## 하루끝 ##
    printAnswer()

    # break