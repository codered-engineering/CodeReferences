#include <stdio.h>
#include <stdlib.h>

typedef struct element *list;
struct element {int value; list next;};

typedef struct node *tree;
struct node {int key; tree left, right;};

void printTree(tree t, int depth) { /* ausgabe eines baumes */
    if (t) {
        for (int i = 0; i < depth; i++) printf("\t");
        printf("%d\n", t->key);
        printTree(t->left, depth+1);
        printTree(t->right, depth+1);
    }
}

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

/* ---------------------- a) --------------------- */
tree createNode(int n, tree l, tree r)
{
    tree tc = malloc(sizeof (struct node));
    tc->key = n;
    tc->left = l;
    tc->right = r;

    return tc;
}

/* ---------------------- b) --------------------- */
void insertl(tree *tp, int n)
{
    while (*tp)
    {
        tp = &((*tp)->left);
    }
    *tp = malloc(sizeof(struct node));
    (*tp)->key = n;
    (*tp)->left = NULL;
    (*tp)->right = NULL;
}

/* ---------------------- c) --------------------- */
int leafprod(tree t)
{
    if(!t)
    {
        return 1;
    }
    if(!t->left && !t->right)
    {
        return t->key;
    }
    
    return leafprod(t->left) * leafprod(t->right);

}

/* ---------------------- d) --------------------- */
void defol(tree *tp)
{
    if (!(*tp)->left && !(*tp)->right)
    {
        free(*tp);
        *tp = NULL;
    }
    else
    {
        defol(&((*tp)->left));
        defol(&((*tp)->right));
    }
}

/* ---------------------- e) --------------------- */
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
void treeToList(tree t, list *lp)
{
    if (t == NULL)
    {
        return;
    }
    treeToList(t->left, lp);
    if(t->key%2 == 0)
    {
        append(lp, t->key);
    }
    treeToList(t->right, lp);
}

/* ---------------------- f) --------------------- */
int countValue(tree t, int n)
{
    if(!t)
    {
        return 0;
    }
    if(t->key == n)
    {
        return 1 + countValue(t->left, n) + countValue(t->right, n);
    }
    else 
    {
        return 0 + countValue(t->left, n) + countValue(t->right, n);
    }
}

tree baz(tree s, tree t)
{
    if(!s)
    {
        return NULL;
    }
    tree res = malloc(sizeof(struct node));
    res->key = countValue(t, s->key);
    res->left = baz(s->left, t);
    res->right = baz(s->right, t);
    return res;    
}



void main()
{
    tree example = createNode(4, createNode(5, NULL, NULL), 
                    createNode(2,createNode(3,NULL,NULL), NULL));
    printTree(example,0);
    insertl(&example, 10);
    printTree(example,0);
    printf("LeafProd: %i\n", leafprod(example));

    list treelist = NULL;
    treeToList(example, &treelist);
    printList(treelist);

    tree s = createNode(2, createNode(3, createNode(2, NULL, NULL), createNode(4, NULL, NULL)), createNode(1, NULL, NULL));
    tree t = createNode(2, createNode(2, NULL, NULL), createNode(3, NULL, NULL));
    printTree(s, 0);
    printTree(t, 0);
    tree baz_tree = baz(s,t);
    printTree(baz_tree, 0);


}