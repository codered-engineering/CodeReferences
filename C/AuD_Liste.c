
typedef struct element *list;
struct element{int value; list next;};

/*--------------------- Element anhaengen ------------------*/
void append(list *lp, int n)
{
    while(*lp)
    {
        lp = &((*lp)->next);
    }
    *lp = malloc(sizeof(struct element));
    (*lp)->value = n;
    (*lp)->next = NULL;
}

/*--------------------- Element entfernen ------------------*/
void delete_it(void *lp, int n)
{
    while(*lp)
    {
        if((*lp)->value == n)
        {
            list tmp = *lp;
            *lp = (*lp)->next;
            free(tmp);
            return;
        }
        lp = &((*lp)->next);
    }
}
void delete_rec(list *lp, int n)
{
    if(!(*lp) || !lp)
    {
        return;
    }
    if((*lp)->value == n)
    {
        list tmp = (*lp);
        *lp = (*lp)->next;
        free(tmp);
    }
    entfernen(&((*lp)->next), n);
}

/*--------------------- Elemente ausgeben ------------------*/
void printList(list l)
{
    printf("[");
    while(l)
    {
        printf("%d", l->value);
        if (l->next)
        {
            printf(", ");
        }
        l = l->next;
    }
    printf("]");
}

/*--------------------- Liste geordnet ------------------*/
int inOrder(list l)
{
    while(l->next)
    {
        if (l->value <= (l->next)->value)
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

/*--------------------- Liste 2 Baum ------------------*/
/* [2,4,7] -> 2 - 4 - 7
                    - 7
                - 4 - 7
                    - 7*/
typedef struct node *tree;
struct node{int key; tree left, right;};

tree full(list l)
{
    if (!l)
    {
        return 0;
    }
    tree wurzel = malloc(sizeof(tree));
    wurzel->key = l->value;
    wurzel->left = l->next;
    wurzel->right = l->next;
    return wurzel;
}

/*--------------- Summen der vorangegangenen Elementen -------------*/
typedef struct elem *LPtr;
struct elem{int value; LPtr next; int sum};

void summen(LPtr l, int s)
{
    if(!l)
    {
        return;
    }
    l->sum = s;
    summen(l->next, l->value + s);
}

/*--------------------- Elementwerte Aufsummieren ------------------*/
int summe_it(list l)
{
    int summe = 0;
    while (l)
    {
        summe += l->value;
        l = l->next;
    }
    return summe;
}

int summe_rec(list l)
{
    if(!l)
    {
        return 0;
    }
    return l->value + summe_rec(l->next);
}

/*--------------------- gerade Werte entfernen ------------------*/
void removeEvans_it(void *lp)
{
    while(*lp)
    {
        if((*lp)->value %2 == 0)
        {
            list tmp = *lp;
            *lp = (*lp)->next;
            free(tmp);
            return;
        }
        lp = &((*lp)->next);
    }
}
void removeEvans_rec(list *lp)
{
    if(!(*lp) || !lp)
    {
        return;
    }
    if((*lp)->value %2 == 0)
    {
        list tmp = (*lp);
        *lp = (*lp)->next;
        free(tmp);
    }
    removeEvans_rec(lp);
}
