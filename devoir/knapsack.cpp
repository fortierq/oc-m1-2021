#include <vector>

int knapsack(int C, int objects[][2])
{
    // à remplir et renvoyer la valeur maximum en prenant des objets dont le poids n'excède pas C
    return 0;
}

int main()
{
    // Exemple
    int objects[7][2] = {{2, 1}, {3, 7}, {6, 10}, {5, 10}, {8, 13}, {2, 1}, {2, 1}};
    // objects[k][0] est le poids du keme objet et objects[k][1] sa valeur
    return knapsack(10, objects);  // doit renvoyer 18
}
