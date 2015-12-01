#include <stdio.h>
#include <stdlib.h>

int funcion_escalon();
int funcion_sigmoidal();
double sumatoria(double *entradas, double *pesos, double umbral);

int main(int argc, char *argv[]){

	int ctd = atof(argv[1]);
	
	double entradas[ctd];
	double pesos[ctd];
	double umbral = atof(argv[argc-1]);

	for(int i=0;i<ctd;i++){
		
		entradas[i] = atof(argv[i+2]);
		pesos[i] = atof(argv[i+2+ctd]);

		printf("entradas[%d]: %f\n", i,entradas[i]);
		printf("pesos[%d]: %f\n", i,pesos[i]);

	}

	printf("umbral: %f\n", umbral);

	printf("sumatoria: %f\n", sumatoria(entradas,pesos,umbral));

	return 0;
}

double sumatoria(double *entradas, double *pesos, double umbral){

	double sum = 0.0;
	int size = sizeof(entradas)/sizeof(entradas[0]);

	for(int i=0; i<2; i++){

		sum += entradas[i]*pesos[i];
	}

	return sum-umbral;
}