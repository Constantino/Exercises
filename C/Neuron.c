#include <stdio.h>
#include <stdlib.h>

int funcion_activacion(float x, int salidas[],float t);
double sumatoria(double *entradas, double *pesos, double umbral, int size);

int main(int argc, char *argv[]){

	int ctd = atof(argv[1]);
	
	double entradas[ctd];
	double pesos[ctd];
	double umbral = atof(argv[argc-2]);
	double t = atof(argv[argc-1]);

	for(int i=0;i<ctd;i++){
		
		entradas[i] = atof(argv[i+2]);
		pesos[i] = atof(argv[i+2+ctd]);

		printf("entradas[%d]: %f\n", i,entradas[i]);
		printf("pesos[%d]: %f\n", i,pesos[i]);

	}

	printf("umbral: %f\n", umbral);

	float sum = sumatoria(entradas,pesos,umbral,sizeof(entradas)/sizeof(double));
	
	printf("sumatoria: %f\n", sum);

	int salidas_sigmoidal[2] = {1,-1}; 
	int salidas_escalon[2] = {1,0}; 

	int salida_funcion_sigmoidal = funcion_activacion(sum,salidas_sigmoidal,0);
	int salida_funcion_escalon = funcion_activacion(sum,salidas_escalon,t);

	printf("Salida funcion_sigmoidal: %d\n", salida_funcion_sigmoidal);
	printf("Salida funcion_escalon: %d\n", salida_funcion_escalon);

	return 0;
}

double sumatoria(double *entradas, double *pesos, double umbral, int size){

	double sum = 0.0;
	
	for(int i=0; i<size; i++){

		sum += entradas[i]*pesos[i];

	}

	return sum-umbral;
}

int funcion_activacion(float x, int *salidas,float t){
	
	if(x >= t) return salidas[0];
	return salidas[1];

}