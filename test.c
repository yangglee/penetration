#include<stdio.h>
#include<stdlib.h>
int main(int argc,char **argv){
	int **p,i;
	p=(int **)malloc(sizeof(int *)*10);
	for(i=0;i<0xa;i++){
		*(p+i)=(int *)malloc(sizeof(int)*0x100);
	}
	*(*(p+1)+5)=0x100;
	printf("0x%x\n",p[1][5]);
	for(i=0;i<10;i++){
		free(*(p+i));
		*(p+i)=NULL;
	}
	free(p);
}
