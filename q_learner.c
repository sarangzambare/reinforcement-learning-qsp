//

#include<stdio.h>
#include<stdlib.h>

struct Qubit{

	float theta;
	float phi;

};

struct Operator{

	float a;
	float b;
	float c;
	float d;
};

void setQubit(struct Qubit *bit,float theta,float phi){

	bit->theta = theta;
	bit->phi = phi;
}

void setOperator(struct Operator *op,float a,float b,float c,float d){

	op->a = a;
	op->b = b;
	op->c = c;
	op->d = d;
}

int main(){

	struct Qubit bit;

	SetQubit(&bit,23.0,24.0);

	printf("%f is the answer \n",bit.theta-23);

	return 0;
}



