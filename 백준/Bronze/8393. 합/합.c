#include <stdio.h>

int main() {

    int t, sum = 0;
    scanf("%d", &t);
    
    for (int i = 1; i <= t; i++) {
        sum += i;
    }

    printf("%d", sum);

    return 0;
}