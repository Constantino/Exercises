#include <stdio.h>
#include <stdlib.h>

int funcion_escalon();
int funcion_sigmoidal();

int main(int argc, char *argv[]){

	double pesos[argc-1];

	for(int i=0;i<argc-1;i++){
		
		pesos[i] = atof(argv[i+1]);
		printf("w[%d]: %f\n", i,pesos[i]);
	}

	return 0;
}