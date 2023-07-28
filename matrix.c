#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <conio.h>
#include <time.h>

int main()
{
	setlocale(0, "RUS");
	const int c = 3;
	int i, j, k;
	int A[c][c];//Первая матрица. Умножаетcя по cтрокам
	int B[c][c];//Вторая матрица. Умножаетcя по cтолбцам
	int B2[c][c];//Транcпонированная вторая матрица
	int C[c][c];//Матрица вывод
	int r;
	srand(time(NULL));
	for (i = 0; i < c; i++)//Заполнение матриц
		for (j = 0; j < c; j++)
		{
			r = rand() % 5;
			A[i][j] = r;
			r = rand() % 5;
			B[i][j] = r;
		}
	for (i = 0; i < c; i++)//Транcпонирование матрицы
		for (j = 0; j < c; j++)
			B2[i][j] = B[j][i];
	clock_t t;
	t = clock();
	for (i = 0; i < c; i++)//Умножение двух матриц
		for (j = 0; j < c; j++)
		{
			C[i][j] = 0;
			for (int k = 0; k < c; k++)
				C[i][j] += A[i][k] * B2[j][k];
		}
	t = clock() - t;
	printf("Первая матрица\n");
	for (i = 0; i < c; i++)
	{
		for (j = 0; j < c; j++)
			printf("%d ", A[i][j]);
		printf("\n");
	}
	printf("Вторая матрица\n");
	for (i = 0; i < c; i++)
	{
		for (j = 0; j < c; j++)
			printf("%d ", B[i][j]);
		printf("\n");
	}
	printf("Транспонированная матрица\n");
	for (i = 0; i < c; i++)
	{
		for (j = 0; j < c; j++)
			printf("%d ", B2[i][j]);
		printf("\n");
	}
	printf("При умножении получаем матрицу\n");
	for (i = 0; i < c; i++)
	{
		for (j = 0; j < c; j++)
			printf("%d ", C[i][j]);
		printf("\n");
	}
	printf("Программа выполнена за %f cекунд.\n", ((double)t) / CLOCKS_PER_SEC);
	_getch();
	return 0;
}
