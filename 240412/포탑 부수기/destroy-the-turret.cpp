#include <iostream>
#include <vector>

using namespace std;

int N, M, K;
		   
int di[8] = { 0, 1, 1, 1, 0, -1, -1 };
int dj[8] = { 1, 1, 0, -1, -1, -1, 0 };

struct Turret {
	int attack;
	int last_turn = 0;
	bool is_fought = false;
};

typedef pair<int, int> Coord;

int real_i(int i) {
	if (i >= N) i -= N;
	else if (i < 0) i += N;
	
	return i;
}

int real_j(int j) {
	if (j >= N) j -= M;
	else if (j < 0) j += M;

	return j;
}

Coord find_weak(vector< vector<Turret> >& world) {
	Coord coord = { 0, 0 }; // (i, j)
	
	int min_val = 5001;
	int max_turn = 0;
	int sum_ij = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (world[i][j].attack == 0) continue;

			if (world[i][j].attack < min_val) { // 가장 약한 포탑
				coord.first = i;
				coord.second = j;

				min_val = world[i][j].attack;
				max_turn = world[i][j].last_turn;
				sum_ij = i + j;

			}
			else if (world[i][j].attack == min_val) { // 공격력이 같다면
				if (world[i][j].last_turn > max_turn) { // 턴수가 가장 큰 것
					coord.first = i;
					coord.second = j;

					min_val = world[i][j].attack;
					max_turn = world[i][j].last_turn;
					sum_ij = i + j;

				}
				else if (world[i][j].last_turn == max_turn) { // 턴수도 같다면
					if ((i + j) > sum_ij) { // 행열 합이 제일 큰것
						coord.first = i;
						coord.second = j;

						min_val = world[i][j].attack;
						max_turn = world[i][j].last_turn;
						sum_ij = i + j;
					}
					else if ((i + j) == sum_ij) { // 행열 합도 같다면
						if (j > coord.second) { // 열이 큰 것
							coord.first = i;
							coord.second = j;

							min_val = world[i][j].attack;
							max_turn = world[i][j].last_turn;
							sum_ij = i + j;
						}
					}
				}
			}
		}
	}

	return coord;
}


Coord find_strong(vector< vector<Turret> >& world) {
	Coord coord = { 0, 0 }; // (i, j)

	int max_val = 0;
	int min_turn = 1001;
	int sum_ij = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (world[i][j].attack == 0) continue;

			if (world[i][j].attack > max_val) { // 가장 강한 포탑
				coord.first = i;
				coord.second = j;

				max_val = world[i][j].attack;
				min_turn = world[i][j].last_turn;
				sum_ij = i + j;

			}
			else if (world[i][j].attack == max_val) { // 공격력이 같다면
				if (world[i][j].last_turn < min_turn) { // 턴수가 가장 작은 것(오래된것)
					coord.first = i;
					coord.second = j;

					max_val = world[i][j].attack;
					min_turn = world[i][j].last_turn;
					sum_ij = i + j;

				}
				else if (world[i][j].last_turn == min_turn) { // 턴수도 같다면
					if ((i + j) < sum_ij) { // 행열 합이 제일 작것
						coord.first = i;
						coord.second = j;

						max_val = world[i][j].attack;
						min_turn = world[i][j].last_turn;
						sum_ij = i + j;
					}
					else if ((i + j) == sum_ij) { // 행열 합도 같다면
						if (j < coord.second) { // 열이 작은 것
							coord.first = i;
							coord.second = j;

							max_val = world[i][j].attack;
							min_turn = world[i][j].last_turn;
							sum_ij = i + j;
						}
					}
				}
			}
		}
	}

	return coord;
}

vector<Coord> shortest_path;

void try_laser(vector< vector<Turret> >& world, vector<vector<int>> visited, Coord start, Coord dest, vector<Coord> path) {
	if (start.first == dest.first && start.second == dest.second) {
		if (shortest_path.size() > path.size()) shortest_path = path;
		return;
	}
	else {
		Coord next;
		for (int d = 0; d < 8; d += 2) {
			next.first = real_i(start.first + di[d]);
			next.second = real_j(start.second + dj[d]);
			
			if (world[next.first][next.second].attack == 0 || visited[next.first][next.second] == 1) continue;
			
			visited[next.first][next.second] = 1;

			vector<Coord> new_path(path);
			new_path.push_back(next);
			try_laser(world, visited, next, dest, new_path);
			visited[next.first][next.second] = 0;
		}
	}
}



int main() {
		cin >> N >> M >> K;

		vector< vector<Turret> > world(N, vector<Turret>(M));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cin >> world[i][j].attack;
			}
		}

		for (int turn = 1; turn <= K; turn++) {
			auto attacker_coord = find_weak(world);
			Turret& attack_turret = world[attacker_coord.first][attacker_coord.second];
			attack_turret.last_turn = turn;
			attack_turret.is_fought = true;
			attack_turret.attack += (M + N);
			int attack_val = attack_turret.attack;

			auto victim_coord = find_strong(world);

			// laser 경로가 있는지 체크
			vector< vector<int> > visited(N, vector<int>(M, 0));
			shortest_path = vector<Coord>(N + M - 1);
			try_laser(world, visited, attacker_coord, victim_coord, vector<Coord>());

			// laser 공격
			if (shortest_path.size() < N+M-1) {
				for (int i = 0; i < shortest_path.size(); i++) {
					int vi = shortest_path[i].first;
					int vj = shortest_path[i].second;

					int result;
					if (i < shortest_path.size() - 1) {
						result = world[vi][vj].attack - (attack_val / 2);
					}
					else result = world[vi][vj].attack - attack_val;

					world[vi][vj].attack = result < 0 ? 0 : result;
					world[vi][vj].is_fought = true;
				}
			}
			else { // 포탄 공격
				for (int d = 0; d < 8; d++) {
					int vi = real_i(victim_coord.first + di[d]);
					int vj = real_j(victim_coord.second + dj[d]);

					if (vi == attacker_coord.first && vj == attacker_coord.second) continue;

					int result = world[vi][vj].attack - (attack_val / 2);
					world[vi][vj].attack = result < 0 ? 0 : result;
					world[vi][vj].is_fought = true;
				}
				int result = world[victim_coord.first][victim_coord.second].attack - attack_val;
				world[victim_coord.first][victim_coord.second].attack = result < 0 ? 0 : result;
				world[victim_coord.first][victim_coord.second].is_fought = true;
			}

			// 정비
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (world[i][j].attack != 0 && !world[i][j].is_fought) world[i][j].attack += 1;
					world[i][j].is_fought = false;
				}
			}
		}

		int max_attack = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (world[i][j].attack > max_attack) max_attack = world[i][j].attack;
			}
		}
		cout << max_attack << '\n';

	return 0;
}