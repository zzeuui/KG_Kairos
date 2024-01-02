#include <stdio.h>

int Square(int n){
	n = n*n;
	return n;
	
}
int main(void){
	int a = 3;
	int q = Square(a);
	printf("%d\n", q, a);
}






void Square(int *a){
	*a =  *a * *a;
}

int main(void){
	int a = 3;
	Square(&a);
	printf("%d\n", a);
}



