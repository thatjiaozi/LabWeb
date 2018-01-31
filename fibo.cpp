#include<iostream>
#include<vector>

using namespace std;

long fibbonnaci(int nTerm)
{
	vector<long> fib;
	fib.resize(2);

	fib[0] = 1;
	fib[1] = 1;

	for(int i = 2; i < nTerm; i++)
	{
		fib.push_back(fib[i - 1] + fib[i - 2]);
	}

	return fib.back();
}

int main()
{
	int nTerm;

	cin >> nTerm;

	cout << fibbonnaci(nTerm) << endl;
}
