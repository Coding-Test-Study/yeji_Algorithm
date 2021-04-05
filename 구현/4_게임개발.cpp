#include<iostream>
#include<vector>
using namespace std;
int n, m, x, y, dir;
vector<vector<int>>v;
vector<int>v1;
int r = 0, c = 0;
int cnt = 0;
int re(int r, int c, int d)
{
	if (r < 0 || r >= n || c < 0 || c >= m || v[r][c] == 1)
	{
		return 0;
	}
	if (v[r][c] == 0)
	{
		v[r][c] = 1;
		cnt++;
		re(r, c - 1, 3);
		re(r + 1, c, 2);
		re(r, c + 1, 1);
		re(r - 1, c, 0);
	}



}
int main(void)
{
	cin >> n;
	cin >> m;
	cin >> x;
	cin >> y;
	cin >> dir;

	for (int i = 0; i < n; i++)
	{
		v1.clear();
		for (int j = 0; j < m; j++)
		{
			int input;
			cin >> input;
			v1.push_back(input);
		}
		v.push_back(v1);
	}
	int r = 0, c = 0;
	if (dir == 0)dir = 3;
	else dir = dir - 1;
	re(x, y, dir);
	cout << cnt;
	return 0;
}