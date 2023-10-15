#include <iostream>
#include <ostream>
void max3();
int  main() {

    max3();

    return 0;
}
void max3(){
    int x=0;
    int y=0;
    int z=0;
    // Take input from user 
    std::cout<<"PLease enter the 3 numbers: "<<std::endl;
    std::cin>>x;
    std::cin>>y;
    std::cin>>z;
    // Get the max of the 3 numbers

    int max=x;
    if(max==y && max ==z) // Check if numbers are equal
    {
        std::cout<<"Numbers are equal"<<std::endl;
        max=x;
    }
    else if(y>=max && y>z)
    {
        max=y;
    }
    else if (z>=max && z>y) {
        max=z;
    
    }
    else if (z==y && z>=max) {
        max = z; 
       
    }
    else
    {
        std::cout << "Please enter valid numbers" << std::endl;
    }
   
    printf("Max equal = %d \n",max);
}