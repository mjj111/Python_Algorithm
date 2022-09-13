#include <iostream>
#include <random>
#include <stdio.h> 
#include <stdlib.h> 

void Main() {

    int arr[20];

    std::cout << "20개의 난수: ";
    for (int i = 0; i < 20; i++) {
        arr[i] = rand() % 100;
        std::cout << arr[i];
        std::cout << " ";
    }

    std::cout << std::endl;
    int tmp = arr[0];

    for (int i = 1; i < 20; i++) {
        if (arr[i] > tmp) {
            tmp = arr[i];
        }
    }

    std::cout << "최댓값 : " << tmp << std::endl;
   

}
