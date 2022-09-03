/*
author: Leo
date: ??/??/????
*/
#include <iostream>
using namespace std;
using std::cout;
using std::cin;
using std::endl; 

int age {18};

int main(int argc, char *argv[]) {
    // comment me
    int a = 133;
    cout << a << endl;
    float b = 1.2;
    /*
    Life is tired
    */
    cout << b << endl;
    int* dyn = new int;
    *dyn = 134444;
    cout << *dyn << endl;
    delete dyn;
    cout << "Hello World!!" << endl;
    return 0;
}