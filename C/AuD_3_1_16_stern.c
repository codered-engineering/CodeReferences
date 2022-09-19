#include <stdio.h>

void swap(int *x, int *y)
{
    if (*x % 2 != 0)
    {
        *x = *x + 1;
    }
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main()
{
    int x = 5;
    int y = 8;
    printf("x = %d \t y = %d ", x, y);

    swap(&x, &y);
    printf("\tSwap: x = %d \t y = %d ", x, y);
    return 0;
}