#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{

	int n;
	string s, buf;
	cin >> n;
	getline(cin, buf);
	getline(cin, s);
	int i = 1, j = 1;
	int k = 0;
	while (k != s.length())
	{
		if (s[k] == ' ')
		{
			k++;
			continue;
		}
		char a = s[k];
		if (a == 'L')
		{
			if (j - 1 != 0)
			{
				j -= 1;
			}
		}
		else if (a == 'R')
		{
			if (j + 1 != n + 1) {

				j += 1;
			}
		}
		else if (a == 'U')
		{
			if (i - 1 != 0)
			{

				i -= 1;
			}
		}
		else if (a == 'D')
		{
			if (i + 1 != n + 1)
			{
				i += 1;
			}
		}
		k++;
	}
	cout << i << " " << j;
	return 0;
}