#include <stdio.h>
int main () {
    int i = 1;
    printf("%s\n", *(char*)&i ? "LittleEndian" : "BigEndian" );
    return 0;
}
