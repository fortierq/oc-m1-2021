#include <vector>
#include <iostream>
using namespace std;

int knapsack(int C, int objects[][2])
{
    int n = sizeof(objects[0]) - 1; //Nombre d'objets
    int v[C + 1][n + 1];            //Déclaration de la matrice résultat

    for (int c = 0; c <= C; c++)
    {
        v[c][0] = 0;
    }

    for (int k = 1; k <= n; k++)
    {
        for (int c = 0; c <= C; c++)
        {
            // Si le poids de l'objet est inférieur à la capacité du sac
            if (c - objects[k][0] >= 0)
            {
                v[c][k] = max(v[c][k - 1], v[c - objects[k][0]][k - 1] + objects[k][1]);
            }

            // Si le poids du nouvel element dépasse la capacité du sac
            else
            {
                v[c][k] = v[c][k - 1];
            }
        }
    }
    return v[C][n];
}

int main()
{
    int objects[7][2] = {{2, 1}, {3, 7}, {6, 10}, {5, 10}, {8, 13}, {2, 1}, {2, 1}};
    // objects[k][0] est le poids du keme objet et objects[k][1] sa valeur

    cout << knapsack(10, objects); // doit renvoyer 18
    return 0;
}

//Maissa Arbi - M1 IAD
