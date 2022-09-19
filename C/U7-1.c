#include <stdio.h>
#include <stdlib.h>

typedef struct element *list;
struct element { int value; list next; };

typedef struct node *tree;
struct node { int key; tree left, right;};

void printTree(tree t, int depth) { /* ausgabe eines baumes */
    if (t) {
        for (int i = 0; i < depth; i++) printf("\t");
        printf("%d\n", t->key);
        printTree(t->left, depth+1);
        printTree(t->right, depth+1);
    }
}

void printlist(list ls){
    printf("[");
    while (ls){
        printf("%d", ls->value);
        if(ls->next){
            printf(", ");
        }
        ls = ls->next;
    }
    printf("]");
}
// a)
tree createNode(int n, tree l, tree r){
    tree result = malloc(sizeof(struct node));
    result->key = n;
    result->left = l;
    result->right = r;
    return result;
}
// b)
void insertl(tree *tp, int n){
    // Ausnahme abfangen
    if (tp == NULL){
        return;
    }
    //Bis zu Blattknoten links gehen
    while(*tp != NULL){
        tp = &((*tp)->left);
    }
    // Neuen Knoten anlegen, Werte dort eintragen
    (*tp) = malloc(sizeof(struct node));
    (*tp)->key = n;
    (*tp)->left = NULL;
    (*tp)->right = NULL;
}

// c)
int leafprod(tree t){
    // Basisfall
    if (t == NULL){
        return 1;
    }
    // Tiefstes Level der Rekursion: Blattknoten
    if (t->left == NULL && t->right == NULL){
        return t->key;
    }
    // Rekursiver Aufruf
    return leafprod(t->left) * leafprod(t->right);
}

// d)
void defol(tree *tp){
    // Ausnahmen: der Baum existiert nicht
    if (tp == NULL){
        return;
    }
    if (*tp == NULL){
        return;
    }
    // Wenn der Baum, auf den gezeigt wird, schon ein Blatt ist:
    if ((*tp)->left == NULL && (*tp)->right == NULL){
        free(*tp);
        *tp = NULL;
    // sonst: weiter den Baum entlang gehen, bis Blatt gefunden wird
    } else {
        defol(&((*tp)->left));
        defol(&((*tp)->right));
    }
}

// e)
void append(list *lp, int n){
    while (*lp != NULL){
        lp = &((*lp)->next);
    }
    (*lp) = malloc(sizeof(struct element));
    (*lp)->value = n;
    (*lp)->next = NULL;
}

void treeToList(tree t, list *lp){
    if (t == NULL){
        return;
    }
    treeToList(t->left, lp);
    if(t->key % 2 == 0){
        append(lp, t->key);
    }
    treeToList(t->right, lp);
}

// f)
int count(tree t, int k){
    int counter = 0;
    if (t == NULL){
        return 0;
    }
    if (t->key == k){
        counter = 1;
    }
    return counter + count(t->left, k) + count(t->right, k);
}
tree baz(tree s, tree t){
    tree result;
    if (s == NULL){
        return NULL;
    }
    result = malloc(sizeof(struct node));
    result->key = count(t, s->key);
    result->left = baz(s->left, t);
    result->right = baz(s->right, t);
    return result;
}

int main(){
    tree example = createNode(4, createNode(5, NULL, NULL), createNode(2, createNode(0, NULL, NULL), NULL));
    insertl(&example, 6);
    insertl(&example, 7);
    list my_list = NULL;
    printTree(example, 0);
    treeToList(example, &my_list);
    printlist(my_list);
    printf("The product of all keys in the tree is %i.\n", leafprod(example));
    defol(&example);
    //printTree(example, 0);

    tree s = createNode(2, createNode(3, createNode(2, NULL, NULL), createNode(4, NULL, NULL)), createNode(1, NULL, NULL));
    tree t = createNode(2, createNode(2, NULL, NULL), createNode(3, NULL, NULL));
    printTree(s, 0);
    printTree(t, 0);
    tree baz_tree = baz(s,t);
    printTree(baz_tree, 0);
}
