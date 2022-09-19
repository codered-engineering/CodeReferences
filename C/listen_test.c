#include <stdio.h>
#include <stdlib.h>

typedef struct element *list;
struct element{int key; list next;};

void append(list *la, int n)
{
    while (*la)
    {
        la = &((*la)->next);
    }
    *la = (list) malloc(sizeof(struct element));
    (*la)->key = n;
    (*la)->next = NULL;

}

void printList(list lp)
{
    printf("[");
    while(lp)
    {
        printf("%d", lp->key);
        lp = lp->next;
        if (lp)
        {
            printf(", ");
        }
    }
    printf("]");
}

int inOrder(list lo)
{
    while (lo)
    {
        if(lo->next == NULL)
        {
            break;
        }
        else if (lo->key > (lo->next)->key)
        {
           return 0; 
        }
        lo = lo->next;
    }
    return 1;
}


void main()
{
    list ls = NULL;
    append(&ls, 3);
    append(&ls, 7);
    append(&ls, 9);
    append(&ls, 11);
    printList(ls);
    printf("\nListe ist aufsteigend geordnet: %d", inOrder(ls));
}