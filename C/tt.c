#include <stdio.h>
#include <stdlib.h>

typedef struct node *tree;
struct node{int key; tree left, right;};

typedef struct element *list;
struct element{int value; list next;};

void printTree(tree t, int depth)
{
    if(!t)
    {
        return;
    }
    for (int i = 0; i< depth; i++)
    {
        printf("\t");
    }
    printf("%d\n", t->key);
    printTree(t->left, depth+1);
    printTree(t->right, depth+1);
}


tree createNode(int n, tree l, tree r)
{
    tree t = malloc(sizeof(struct node));
    t->key = n;
    t->left = l;
    t->right = r;
    return t;
}

void insertl(tree *tp, int n)
{
    if(*tp && !(*tp)->left && !(*tp)->right)
    {
        (*tp)->left = createNode(n, NULL, NULL);
    }
    else 
    {
        tp = &((*tp)->left);
    }
}


void main()
{
    tree example = createNode(4, createNode(5,NULL,NULL), createNode(2,createNode(0,NULL,NULL),NULL));
    printTree(example, 0);




}