#include <stdio.h>
#include <stdlib.h>

typedef struct L_ele *LPtr;
struct L_ele{int key; LPtr next;} l_element;

void  anfuegen(LPtr *lp, int n)
{
    if(*lp)
    {
        anfuegen(&((*lp))->next, n);
    }
    else if(!(*lp))
    {
        *lp = malloc(sizeof(struct L_ele));
        (*lp)->key = n;
        (*lp)->next = NULL;
    }
}

void entfernen(LPtr *lp, int n)
{
    if((*lp)->key == n)
    {
        LPtr tmp = (*lp);
        *lp = (*lp)->next;
        free(tmp);
    }
    else if((*lp)->next)
    {
        entfernen(&((*lp)->next), n);
    }
}

void printList(LPtr l)
{
    printf("[");
    while(l)
    {
        printf("%d", l->key);
        if (l->next)
        {
            printf(", ");
        }
        l = l->next;
    }
    printf("]");
}



void main()
{

    LPtr lstart = NULL;
    anfuegen(&lstart, 1);
    anfuegen(&lstart, 3);
    anfuegen(&lstart, 2);
    anfuegen(&lstart, 3);
    anfuegen(&lstart, 4);
    printList(lstart);
    entfernen(&lstart, 2);
    printList(lstart);
    entfernen(&lstart, 1);
    printList(lstart);
    entfernen(&lstart, 4);
    printList(lstart);


}