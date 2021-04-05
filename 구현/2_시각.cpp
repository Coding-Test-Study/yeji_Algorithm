#include<iostream>
using namespace std;
int main()
{
	int n;
	cin >> n;
	int cnt = 0;
	/*for (int i = 0; i <= n; i++)
	{
		for (int j = 0; j <= 59; j++)
		{
			for (int k = 0; k <= 59; k++)
			{
				if (k/10 == 3||i/10==3||j/10==3||i==3||j==3||k==3||i%10==3||j%10==3||k%10==3)
				{
					cnt++;
				}
			}
		}
	}
		*/
	for (int i = 0; i <= n; i++)
	{
		for (int j = 0; j <= 59; j++)
		{
			if (j == 3 || j / 10 == 3 || j % 10 == 3 || i == 3 || i / 10 == 3 || i % 10 == 3) cnt = cnt + 60;
			else cnt = cnt + 15;
		}
	}

	cout << cnt;

	return 0;
}