#include <algorithm>
#include <iostream>
#include <iterator>
int maxNumArray(int * arr,int size);
int main(){
   
    int arr[]={10,20,40,15,17,18,19};
    int size = sizeof(arr)/sizeof(arr[0]);
std::cout << "MAX element =" <<     maxNumArray(arr,size)<<std::endl;    
return 0;
    
}

int maxNumArray(int * arr,int size){

int max=arr[0];
for (int i = 1; i < size; i++)
{
    if(arr[i]>max)
    {
        max=arr[i];

    }
}
return max;

}

