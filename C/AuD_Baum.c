typedef struct node *tree;
struct node{int key; tree left, right;};

/* AGS 3.2.10a ----------------------------------------------------
 * Heap - Eigenschaft
 */
int isHeap(tree t)
{
    int heap = 0;
    if(!t)
    {
        return 1;
    }

    if(t->left)
    {
        heap = isHeap(t->left) && (t->left->key < t->key);
    }
    else
    {
        heap = 1;
    }

    if(t->right)
    {
        heap = isHeap(t->right) && (t->right->key < t->key);
    }
    return heap;
}
/* AGS 3.2.10b ----------------------------------------------------
 * Summe aller Werte
 */
int summe(tree t)
{
    if (!t)
    {
        return 0;
    }
    return t->key + summe(t->left) + summe(t->right);
}

/* AGS 3.2.12 ----------------------------------------------------
 * Baum 2 List (inkl. Pfadlaenge)
 */
typedef struct ele *LPtr;
struct ele{int value, pfad; LPtr next;};

void append_list_avl(LPtr *lp, int val, int pf)
{
    while(*lp)
    {
        lp = &((*lp)->next);
    }
    *lp = malloc(sizeof(struct ele));
    (*lp)->value = val;
    (*lp)->pfad = pf;
    (*lp)->next = NULL;
}

void zickzack(tree t, LPtr l, int pfad)
{
    if(!t || !l)
    {
        return;
    }
    pfad ++;
    append_list_avl(&l, t->key, pfad);
    if(pfad%2 == 0)
    {
        zickzack(t->right, l, pfad);
    }
    else
    {
        zickzack(t->left, l, pfad);
    }
}
tree baum;
LPtr liste;
zickzack(baum, liste, 0);

/* AGS 3.2.16 ----------------------------------------------------
 * Entfernen von Knoten im binären Suchbaum (z.B. Heap)
 */
void node_insert(tree *tp, tree node)
{
    if(!node)
    {
        return;
    }
    if(!(*tp))
    {
        *tp = node;
    }
    else if(node->key < (*tp)->key)
    {
        node_insert(&(*tp)->left, node);
    }
    else
    {
        node_insert(&(*tp)->right, node);
    }
    return;
}
void node_del(tree *tp, int n)
{
    if(!(*tp))
    {
        return;
    }
    if((*tp)->key == n)
    {
        tree tmp = *tp;
        (*tp) = tmp->left;
        node_insert(tp, tmp->right);
        tmp->left = NULL;
        tmp->right = NULL;
        free(tmp);
    }
    else if(n < (*tp)->key)
    {
        node_del(&(*tp)->left, n);
    }
    else
    {
        node_del(&(*tp)->right, n);
    }
}

/* AGS 3.2.17 ----------------------------------------------------
 * AVL-Baum-Struktur, AVL-Baeume vereinen -> "insert_avl ist gegeben"
 */
typedef struct avl_node *BPtr;
struct avl_node {int value, balance; BPtr left, right;};

void union_avl(BPtr baum1, BPtr *baum2)
{
    if(!baum1)
    {
        return;
    }
    insert_avl(baum2, baum1->value); 
    union_avl(baum1->left, baum2);
    union_avl(baum1->right, baum2);  
}

/* AGS 3.2.18 ----------------------------------------------------
 * Baum 2 List (mitte -> links -> rechts)
 */
typedef struct element *list;
struct element{int value; list next;};

void append_list(list *lp, int n)
{
    if(!(*lp))
    {
        *lp = malloc(sizeof(struct element));
        (*lp)->value = n;
        (*lp)->next = NULL;
    }
    else
    {
        append_list(&(*lp)->next, n);
    }
}

void tree_2_list(tree t, list *lp)
{
    if(!t)
    {
        return;
    }
    append_list(lp, t->key);
    tree_2_list(t->left, lp);
    tree_2_list(t->right, lp);
}

/*------ Baum 2 List -> nur gerade Werte (links -> mitte -> rechts) ------*/
void treeToList(tree t, list *lp)
{
    if (!t)
    {
        return;
    }
    treeToList(t->left, lp);
    if(t->key % 2 == 0){
        append_list(lp, t->key);
    }
    treeToList(t->right, lp);
}

/* AGS 3.2.42b ----------------------------------------------------
 * Blaetter gerade Werte?
 */
int leavesEven(tree t)
{
    if(!t)
    {
        return 1;
    }
    if(!(t->left) && !(t->right) && t->key%2 == 0)
    {
        return 1; 
    }
    else if(t->key%2 != 0)
    {
        return 0;
    }
    
    return leavesEven(t->left) && leavesEven(t->right);
}

/* AGS 3.2.42c ----------------------------------------------------
 * wie oft kommt Wert n im Teilbaum n vor -> int Anzahl ersetzt int Wert
 */
int countOccur(tree t, int anz)
{
    if (!t)
    {
        return 0;
    }
    if(t->key == anz)
    {
        return 1 + countOccur(t->left, anz) + countOccur(t->right, anz);
    }
    else
    {
        return countOccur(t->left, anz) + countOccur(t->right, anz);
    }
}

void occur(tree t, int k)
{
    if (!t)
    {
        return;
    }
    t->key = countOccur(t, k);
    occur(t->left, k);
    occur(t->right, k);
}

/* AGS 3.2.44a ----------------------------------------------------
 * Linksbaum - Prominenz
 */
int prom_it(tree t)
{
    int p = 0;
    while(!t)
    {
        if(!(t->left))
        {
            t = t->right;
        }
        else
        {
            t = t->left;
        }
        p ++;
    }
    return p;
}
int prom_rec(tree t)
{
    if(!t)
    {
        return 0;
    }
    if(!(t->left))
    {
        return 1 + prom(t->right);
    }
    else
    {
        return 1 + prom(t->left);
    }
}

/* AGS 3.2.44b ----------------------------------------------------
 * Ist es ein Links- oder Rechtsbaum (Prominenz)
 */
int isRightist(tree t)
{
    if(!t)
    {
        return 1;
    }
    return ((prom(t->left) <= prom(t->right)) &&
            isRightist(t->left) && isRightist(t->right))
}

/* AGS 3.2.49b ----------------------------------------------------
 * Hoehe
 */
int height(tree t)
{
    if(!t)
    {
        return 0;
    }
    int hl = height(t->left);
    int hr = height(t->right);

    if(hl > hr)
    {
        return hl+1;
    }
    return hr+1;
}

/* AGS 3.2.49c ----------------------------------------------------
 * BFS
 */
tree bfs(tree t)
{
    if(!t)
    {
        return NULL;
    }
    tree bf = malloc(sizeof(struct node));
    bf->key = height(t->right) - height(t->left);
    bf->left = bfs(t->left);
    bf->right = bfs(t->right);
    return bf;
}

/*--------------------- Blaetter produkt ------------------*/
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

/*--------------------- Anfuegen (links) ------------------*/

/*--------------------- Anfuegen (rechts) ------------------*/

/*--------------------- Summe Blaetter ------------------*/





