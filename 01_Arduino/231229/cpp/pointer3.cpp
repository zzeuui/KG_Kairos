
#include<stdio.h>

int main(void)
{ 
    int a = 0, b = 0, c = 0;
    int* ip = NULL;

    ip = &a; // &는 주소를 참조. a의 주소를 ip에 대입
    //*는 값을 참조. 즉, 값을 참조하기 위해서는 변수가 주소여야함.
    // ip의 값을 10으로 변경
    *ip = 10;
    printf("%d %d %d %d\n", a, b, c, *ip);

    ip = &b;
    *ip = 20;
    printf("%d %d %d %d\n", a, b, c, *ip);

    ip = &c;
    *ip = 30;
    printf("%d %d %d %d\n", a, b, c, *ip);

    return 0;
}
