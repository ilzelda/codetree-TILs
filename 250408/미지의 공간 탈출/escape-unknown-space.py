from collections import deque

N, M, F = map(int, input().split())

village = [list(map(int, input().split())) for _ in range(N)]

cuboid = [ [list(map(int, input().split())) for _ in range(M)] for _ in range(5)]

incidents = []
for _ in range(F):
    r, c, d, v = map(int, input().split())
    incidents.append([r,c,d,v])

# print(cuboid[0])

# 동 서 남 북
di = [0,0,1,-1]
dj = [1,-1,0,0]

# 인접한 면 매핑 정보
# 위 왼 오
side_face_mapping = { 0 : [4, 2, 3],
                      1 : [4, 3, 2],
                      2 : [4, 1, 0],
                      3 : [4, 0, 1],
                      4 : [3, 1, 0, 2]}

def in_range(i,j, size):
    return 0<=i<size and 0<=j<size

def generateGraph(_cuboid):
    _graph = dict()
    for face_id in range(5):
        for i in range(M):
            for j in range(M):
                _graph[(face_id, i, j)] = []

                # 같은 평면에 있는 것들 이어주기
                for d in range(4):
                    connected_i = i + di[d]
                    connected_j = j + dj[d]
                    if in_range(connected_i, connected_j, M):
                        _graph[(face_id, i, j)].append((face_id, connected_i, connected_j))

                # 가생이의 경우 다른 평면에 있는 것들 이어주기
                if i==0: # 위쪽 평면과 이어주기
                    conn_face_id = side_face_mapping[face_id][0]
                    if face_id == 0:
                        conn_i = M-1-j
                        conn_j = M-1
                    elif face_id == 1:
                        conn_i = j
                        conn_j = 0
                    elif face_id == 2:
                        conn_i = M-1
                        conn_j = j
                    elif face_id == 3:
                        conn_i = 0
                        conn_j = M-1-j
                    elif face_id == 4:
                        conn_i = 0
                        conn_j = M-1-j
                    _graph[(face_id, i, j)].append((conn_face_id, conn_i, conn_j))

                if j==0: # 왼쪽 평면과 이어주기
                    conn_face_id = side_face_mapping[face_id][1]
                    if face_id == 0:
                        conn_i = i
                        conn_j = M-1
                    elif face_id == 1:
                        conn_i = i
                        conn_j = M-1
                    elif face_id == 2:
                        conn_i = i
                        conn_j = M-1
                    elif face_id == 3:
                        conn_i = i
                        conn_j = M-1
                    elif face_id == 4:
                        conn_i = 0
                        conn_j = i
                    _graph[(face_id, i, j)].append((conn_face_id, conn_i, conn_j))

                if j==M-1: # 오른쪽 평면과 이어주기
                    conn_face_id = side_face_mapping[face_id][2]
                    if face_id != 4:
                        conn_i = i
                        conn_j = 0
                    else:
                        conn_i = 0
                        conn_j = M-1-i
                    _graph[(face_id, i, j)].append((conn_face_id, conn_i, conn_j))

                if face_id == 4 and i==M-1 : # 아래 평면과 이어주기
                    conn_face_id = side_face_mapping[face_id][3]
                    conn_i = 0
                    conn_j = j
                    _graph[(face_id, i, j)].append((conn_face_id, conn_i, conn_j))

    return _graph

def find_exit(_village):
    min_i, min_j = N, N
    max_i, max_j = 0, 0

    for i in range(N):
        for j in range(N):
            if _village[i][j] == 3 :
                min_i = min(min_i, i)
                min_j = min(min_j, j)

                max_i = max(max_i, i)
                max_j = max(max_j, j)

    # 북 / 남 체크
    for i in [min_i-1, max_i+1]:
        for j in range(min_j, max_j + 1):

            if _village[i][j] == 0:
                # print("exit coord in village is : ", (i, j))
                if i == min_i-1 : # 북
                    return (i, j), (3,M-1,M-1-(j-min_j))
                elif i == max_i+1 : # 남
                    return (i, j), (2,M-1,(j-min_j))

    # 동 / 서 체크
    for j in [min_j - 1, max_j + 1]:
        for i in range(min_i, max_i + 1):

            if _village[i][j] == 0:
                # print("exit coord in village is : ", (i, j))

                if j == min_j - 1: # 서
                    return (i, j), (1, M-1, (i-min_i))
                elif j == max_j + 1: # 동
                    return (i, j), (0, M-1, M-1-(i-min_i))

def find_start(_cuboid):
    for i in range(M):
        for j in range(M):

            if _cuboid[4][i][j] == 2:
                return (4,i,j)

def BFS_3D(_graph, _start, _dest):
    visited = [ [[False for _ in range(M)] for _ in range(M)] for _ in range(5)]
    distance = [ [[0 for _ in range(M)] for _ in range(M)] for _ in range(5)]

    queue = deque()
    queue.append(_start)
    visited[_start[0]][_start[1]][_start[2]] = True
    distance[_start[0]][_start[1]][_start[2]] = 0


    while(len(queue)>0):
        current = queue.popleft()
        cur_f, cur_i, cur_j = current
        cur_dist = distance[cur_f][cur_i][cur_j]

        for connected in graph[current]:
            next_f, next_i, next_j = connected

            if visited[next_f][next_i][next_j]: continue
            if cuboid[next_f][next_i][next_j] != 0 : continue

            visited[next_f][next_i][next_j] = True
            distance[next_f][next_i][next_j] = cur_dist+1

            if connected == _dest :
                dest_f, dest_i, dest_j = _dest
                return distance[dest_f][dest_i][dest_j]

            queue.append(connected)

def update_village(time_ground):
    global village

    for inci in incidents:
        r, c, d, v = inci
        cur_i, cur_j = r, c
        village[cur_i][cur_j] = 1

        for t in range(time_ground):
            if t != 0 and t % v == 0:
                next_i = cur_i + di[d]
                next_j = cur_j + dj[d]
                if not in_range(next_i, next_j, N): break
                if village[next_i][next_j] != 0 : break

                village[next_i][next_j] = 1

def find_goal():
    for i in range(N):
        for j in range(N):
            if village[i][j] == 4 :
                return (i,j)

def BFS_2D(_start, _goal, _init_time):
    global village

    q = deque()
    distances = [ [ 0 for _ in range(N)] for _ in range(N)]
    visited = [ [ False for _ in range(N)] for _ in range(N)]

    # 초기 이상현상
    for info in incidents:
        cur_r, cur_c, _, _ = info
        if village[cur_r][cur_c] != 0: continue

        village[cur_r][cur_c] = 1

    if village[_start[0]][_start[1]] == 0:
        visited[_start[0]][_start[1]] = True
        q.append(_start)
        distances[_start[0]][_start[1]] = _init_time + 1

    while len(q) > 0:
        cur_i, cur_j  = q.popleft()
        cur_dist = distances[cur_i][cur_j]

        if village[cur_i][cur_j] == 4 : return distances[cur_i][cur_j] # 도착했으면 리턴

        next_dist = cur_dist + 1

        # 다음것 추가하기 전 이상현상을 업데이트
        for info in incidents:
            cur_r, cur_c, d, v = info

            if next_dist % v == 0:
                w = next_dist // v
                new_r, new_c = cur_r + w*di[d], cur_c + w*dj[d]

                if not in_range(new_r, new_c, N) : continue
                if village[new_r][new_c] != 0: continue

                village[new_r][new_c] = 1

        for d in range(4):
            next_i, next_j = cur_i + di[d], cur_j + dj[d]

            if not in_range(next_i, next_j, N) : continue
            if village[next_i][next_j] == 1 or village[next_i][next_j] == 3 : continue
            if visited[next_i][next_j] : continue

            visited[next_i][next_j] = True
            distances[next_i][next_j] = next_dist

            q.append((next_i, next_j))

    return -1


graph = generateGraph(cuboid)
# print("graph : (4,0,0) is connected with\n", graph[(4,0,0)])

dest2D, dest3D = find_exit(village)
# print("destination coord : ", dest2D, dest3D)

start = find_start(cuboid)
# print("start coord : ", start)

time_ground = BFS_3D(graph, start, dest3D)
# time_ground+=1
# print("time to arrive ground : ", time_ground)

update_village(time_ground)
# for row in village:
#     print(*row)

goal2D = find_goal()
# print("goal : ", goal2D)

ans = BFS_2D(_start = dest2D, _goal = goal2D, _init_time = time_ground)

print(ans)