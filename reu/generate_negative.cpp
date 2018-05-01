#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

bool occur[210][210][210] = {0};
const int TEST_SET_SIZE = 2525;

void read(string file)
{
	freopen(file.c_str(), "r", stdin);
	int a, b, c, d;
	while (cin >> a >> b >> c >> d)
	{
		occur[a][b][c] = 1;
	}
}

int main()
{
	for (int i = 1; i < 6; ++i)
	{
		string file = "enron_train_" + (char(i + '0'));
		file = file + ".txt";
		read(file);
	
		file = "enron_test_" + (char(i + '0'));
		file = file + ".txt";
		read(file);
	}

	freopen("enron_train_6.txt", "w", stdout);
	for (int i = 0; i < TEST_SET_SIZE; ++i)
	{
		int a = rand() % 200, b = rand() % 200, c = rand() % 200;
		while (occur[a][b][c])
		{
			a = rand() % 200;
			b = rand() % 200;
			c = rand() % 200;
		}

		occur[a][b][c] = 1;
		cout << a << ' ' << b << ' ' << c << ' ' << 0 << endl;
	}
}
