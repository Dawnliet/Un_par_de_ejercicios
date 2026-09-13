#include <iostream>
#include <vector>
using namespace std;


// Puse los include y el namespace globales para que no me diera error el archivo, se supone que la solucion puede ser un main en otro archivo 
// si hacen un main en este archvio bueno ya tienen las librerias y el namespace
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        using namespace std;

        int free_pos = 0;

        for(int i = 0; i < nums.size(); i++)
        {
            
            if(nums[i] != 0)
            {
                swap(nums[i], nums[free_pos]);
                free_pos += 1;
            }
            
        }
    }
};