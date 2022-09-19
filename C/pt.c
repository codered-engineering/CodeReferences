#include <stdio.h>
void pt(int *pp)
{
    printf("\n\n pt *");
    printf("\n%d", pp);
    printf("\n%d", *pp);
    printf("\n%d", &pp);
}
void pu(int pp)
{
    printf("\n\n pt *");
    printf("\n%d", pp);
    printf("\n%d", &pp);
}
int main()
{
    int a = 5;
    int b = 7;
    int *p = &a;

    printf("\n%d", p);
    printf("\n%d", *p);
    printf("\n%d", &p);
    pt(p);
    
}