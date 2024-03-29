#include <bits/stdc++.h>
using namespace std;

// Find missing values in an array
int main(int argc, char const *argv[])
{
    // Method 1
    int A[10] = {1, 2, 3, 4, 5, 6, 8, 9, 10, 11};
    int sum = 0;
    int n;
    for (int i = 0; i < 10; i++)
    {
        sum = sum + A[i];
    }

    int s = 66;
    cout << s - sum << endl;

    // Method 2  Applicable any starting index
    int B[10] = {4, 5, 6, 8, 9, 10, 11, 12, 13, 14};
/*Logic:
    4 - 0 = 4 5 - 1 = 4 6 - 2 = 4 8 - 3 = 5*/

        int l = 4;
    int m = 10;
    int dif = l - 0;
    for (int i = 0; i < m; i++)
    {
        if (B[i] - i != dif)
        {
            cout << "the missing number is " << dif + i << endl;
            break;
        }
    }
    // Missing Multiple values
    int C[10] = {4, 5, 6, 10, 11, 13, 14, 15, 16, 17};
    n = 10;
    int diff = 4 - 0;
    for (int i = 0; i < n; i++)
    {
        if (C[i] - i != diff)
        {
            while (C[i] - i > diff)
            {
                cout << "The missing Numbers are " << i + diff << endl;
                diff++;
            }
        }
    }
    int D[7] = {4, 6, 7, 8, 10, 12, 13};
    int H[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int l = 4;
    int h = 13;
    int n = 7;
    for (int i = 0; i < n; i++)
    {
        H[D[i]]++;
    }
    for (int i = l; i <= h; i++)
    {
        if (H[i] == 0)
        {
            cout << i << endl;
        }
    }
    int lastduplicate;
    int E[10] = {4, 5, 5, 9, 6, 6, 8, 10, 12, 13};

    for (int i = 0; i < 10; i++)
    {
        if (E[i] == E[i + 1] && E[i] != lastduplicate)
        {
            cout << "The Duplicate Numbers are " << E[i] << endl;
        }
        lastduplicate = E[i];
    }

    // find pair of sum is k   a+b=k  Using Hash Table
    // complexity O(n)
    int k = 10;
    int n = 10;
    int F[] = {4, 5, 5, 9, 7, 6, 8, 10, 12, 13};
    int H[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    for (int i = 0; i < n; i++)
    {
        if (H[k - F[i]] != 0)
        {
            cout << F[i] << " " << k - F[i] << " " << k << endl;
        }
        H[F[i]]++;
    }

    // for sorted array
    int n = 10;
    int i = 0;
    int j = n - 1;
    int k = 15;

    int L[] = {4, 5, 5, 6, 7, 8, 10, 12, 13, 15, 17};
    cout << "the Pairs are " << endl;
    while (i < j)
    {
        if (L[i] + L[j] == k)
        {

            cout << L[i] << " " << L[j] << " " << k << endl;
            i++;
            j--;
        }
        else if (L[i] + L[j] < k)
        {
            i++;
        }
        else
        {
            j--;
        }
    }

    int A[] = {4, 5, 5, 6, 7, 8, 10, 12, 13, 15, 17};
    int min = A[0];
    int max = A[0];
    int m = 11;

    for (int i = 0; i < m; i++)
    {
        if (A[i] < min)
        {
            min = A[i];
        }
        else if (A[i] > max)
        {
            max = A[i];
        }
    }
    cout << "Min Elemnt is : " << min << endl
         << "Max element is : " << max;
    return 0;
}