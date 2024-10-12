def find_max_val_wall(wall):
    max_info = {'val' : 0, 'angle' : 270, 'ji': (5,5)}

    for center_i in range(1, 4):
        for center_j in range(1, 4):

            for angle in [90, 180, 270]:
                temp_wall = rotate(wall, center_i, center_j, angle)

                v, idx_list = DFS(temp_wall)

                if v > max_info['val']:
                    max_info['val'] = v
                    max_info['angle'] = angle
                    max_info['i'] = center_i
                    max_info['j'] = center_j
                    max_info['wall'] = temp_wall
                    max_info['idx'] = idx_list

                elif v == max_info['val']:
                    if angle < max_info['angle']:
                        max_info['val'] = v
                        max_info['angle'] = angle
                        max_info['i'] = center_i
                        max_info['j'] = center_j
                        max_info['wall'] = temp_wall
                        max_info['idx'] = idx_list

                    elif angle == max_info['angle']:
                        if (j, i) < max_info['ji']:
                            max_info['val'] = v
                            max_info['angle'] = angle
                            max_info['i'] = center_i
                            max_info['j'] = center_j
                            max_info['wall'] = temp_wall
                            max_info['idx'] = idx_list

    return max_info



def rotate(wall, i, j, angle):
    temp = [row[:] for row in wall]
    target = [row[j-1:j+2] for row in temp[i-1:i+2]]

    if angle == 90:
        rotated = list(map(list,zip(*target[::-1])))
    elif angle == 180:
        rotated = [row[::-1] for row in target[::-1]]
    elif angle == 270:
        rotated = [row[:] for row in list(map(list,zip(*target)))[::-1]]

    for r_i, d_i in enumerate(range(-1,2)):
        temp[i + d_i][j-1:j+2] = rotated[r_i]

    return temp

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def generate_next_ij(i, j):
    next_ij = []
    for n in range(4):
        new_i = i + di[n]
        new_j = j + dj[n]

        if new_i >= 0 and new_j >= 0 and new_i < 5 and new_j < 5:
            next_ij.append((new_i, new_j))

    return next_ij

def DFS(temp):
    value = 0
    idx_list = []

    visited = [[False]*5 for _ in range(5)]
    for start_i in range(5):
        for start_j in range(5):
            if visited[start_i][start_j] : continue

            visited[start_i][start_j] = True
            queue = [(start_i, start_j)]

            current_num = temp[start_i][start_j]
            current_count = 1
            history = [(start_i, start_j)]

            while(len(queue)>0):
                i, j = queue.pop(0)
                next_ijs = generate_next_ij(i, j)
                for new_i, new_j in next_ijs:
                    if not visited[new_i][new_j] and temp[new_i][new_j] == current_num:
                        visited[new_i][new_j] = True
                        current_count += 1
                        queue.append((new_i, new_j))
                        history.append((new_i, new_j))

            if current_count >= 3:
                value += current_count
                idx_list += history

    return value, idx_list



K, M = map(int, input().split())

wall = [[0] * 5 for _ in range(5)]

for i in range(5):
    row = list(map(int, input().split()))
    for j, num in enumerate(row):
        wall[i][j] = num

new_pieces = list(map(int, input().split()))

# # debug
# print('origin:')
# for row in wall:
#     print(row)
#
# # for angle in [90,180,270]:
# for angle in [270]:
#     print(angle, end=':\n')
#     temp = rotate(wall, 1,1, angle)
#     for row in temp:
#         print(row)
#     # break

candidate = 0
for k in range(K):
    ans = 0
    max_info = find_max_val_wall(wall)
    wall = max_info['wall']
    indicies = max_info['idx']
    indicies = sorted(indicies, key=lambda x : (x[1],-x[0]))
    ans += max_info['val']

    while True:
        for i, j in indicies:
            wall[i][j] = new_pieces[candidate]
            candidate += 1

        _, indicies = DFS(wall)
        indicies = sorted(indicies, key=lambda x: (x[1], -x[0]))

        if len(indicies) == 0: break
        else: ans+=len(indicies)

    if ans != 0: print(ans, end=' ')