#include<iostream>
#include<string>
using namespace std;
int main()
{
	string input;
	cin >> input;
	char r[8] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' };
	int row = 0;
	int col = input[1] - '0' - 1;
	for (int i = 0; i < 8; i++)
	{
		if (input[0] == r[i]) {
			row = i;
			break;
		}
	}
	int cnt = 0;
	int a1[4] = { -1,1 };

	for (int k = 0; k < 2; k++)
	{
		int r = row + a1[k] + a1[k];
		int c = col + (-1);
		if (r < 0 || r>8 || c < 0 || c>8)continue;
		else {
			cnt++;
		}
	}
	for (int k = 0; k < 2; k++)
	{
		int r = row + a1[k] + a1[k];
		int c = col + 1;
		if (r < 0 || r>8 || c < 0 || c>8)continue;
		else {
			cnt++;
		}
	}
	for (int k = 0; k < 2; k++)
	{
		int c = col + a1[k] + a1[k];
		int r = row + (-1);
		if (r < 0 || r>8 || c < 0 || c>8)continue;
		else {
			cnt++;
		}
	}
	for (int k = 0; k < 2; k++)
	{
		int c = col + a1[k] + a1[k];
		int r = row + 1;
		if (r < 0 || r>8 || c < 0 || c>8)continue;
		else {
			cnt++;
		}
	}

	cout << cnt;
	return 0;
}