#include<iostream>
#include<vector>
using namespace std;

vector<vector<int>>map;
vector<int>map2;
int subx[4] = { -1,0,1,0 };
int suby[4] = { 0,-1,0,1 };
int main() {
	int n, m, x, y, d;
	cin >> n; cin >> m;
	cin >> x; cin >> y; cin >> d;
	for (int i = 0; i < n; i++)
	{
		map2.clear();
		for (int j = 0; j < m; j++)
		{
			int input;
			cin >> input;
			map2.push_back(input);
		}
		map.push_back(map2);
	}
	int cnt = 0;

	map[x][y] = 2; cnt++;

	int dcnt = 0;
	while (1)
	{
		d = (d + 1) % 4;

		int sx = x, sy = y;
		sx = sx + subx[d];
		sy = sy + suby[d];
		if ((sx < 0 && sy < 0 && sx >= n && sy >= m)|| map[sx][sy] == 1|| map[sx][sy] == 2) {
			dcnt++;
		}
		
		else
		{
			x = sx; y = sy;
			cnt++;
			map[x][y] = 2;
			dcnt = 0;
		}

		if (dcnt == 4)
		{
			sx = x - subx[d];
			sy = y - suby[d];
			if (map[sx][sy] == 1)break;
			else
			{
				x = sx; y = sx;
				dcnt = 0;
			}
		}

	}
	cout << cnt;

	return 0;
}