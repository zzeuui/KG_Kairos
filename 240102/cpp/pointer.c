#include <stdio.h>

int main(void){
	char uga[][100] = {"Uga", "Uga", "Uga", "Uga", "Uga"};
	for(int i=0; i<5; i++){
		printf("%s\n", uga[i]);
	}

	char *uga[] = {"hello", "world", "this"};
	for(int i=0; i<3; i++){
		print("%s\n", uga[i]);
	}



	
	char **str_array;
	int array_size = 3;

	str_array = (char **)malloc(sizeof(char *)*array_size);
	for(int i=0; i<array_size; i++){
			str_array[i] = (char *)malloc(sizeof(char *)*10);
			strcpy(str_array[i], "Hello, World!");
	}
	for(int i=0; i<array_size;i++){
		printf("%s\n", str_array[i]);
	}
	for(int i=0;i<arrat_size;i++){
		free(str_array[i]);
	}


}

