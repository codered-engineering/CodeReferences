#include <stdio.h>
#include <stdlib.h>

typedef struct element *list;
struct element{int key; list next;};

void delete_n(list *l, int n)
{
    while(*l)
    {
        if((*l)->key == n)
        {
            list temp = *l;
            *l = (*l)->next;
            free(temp);
        }
        else
        {
            l = &((*l)->next);
        }
    }

}

void append(list *l, int n)
{
    while (*l)
    {
        l = &((*l)->next);
    }

    *l = malloc(sizeof(struct element));
    (*l)->key = n;
    (*l)->next = NULL;
}

void printList(list l)
{
    printf("\n[");
    while (l)
    {
        printf("%d, ", l->key);
        l = l->next;
    }
    printf("]");
}

int inOrder(list l)
{
    while(l->next)
    {
        if (l->key <= (l->next)->key)
        {
            l = l->next;
        }
        else
        {
            return 0;
        }
    }
    return 1;
}

void main()
{
    list ls = NULL;

    append(&ls, 2);
    append(&ls, 11);
    append(&ls, 3);
    append(&ls, 9);
    printList(ls);
    delete_n(&ls, 3);
    printList(ls);
    printf("\n %d", inOrder(ls));
   
}