int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    int *ret_arr=(int*)malloc(sizeof(int)*2);
    *returnSize=2;
    int i,j;
    for(i=0;i<numsSize;i++)
    {
        for(j=i+1;j<numsSize;j++)
        {
            if(nums[i]+nums[j]==target)
            {
                
               *(ret_arr+0)=i;
                *(ret_arr+1)=j;                
                break;
            }
        }
    }   
    return ret_arr;
}
