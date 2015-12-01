#include <stdio.h>
#include <stdlib.h>

int funcion_escalon();
int funcion_sigmoidal();

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

	return 0;
}