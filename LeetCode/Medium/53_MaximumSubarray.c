int maxSubArray(int* nums, int numsSize)
{
    int i, max, tmp;
    
    for (i = 0, tmp = 0, max = nums[0]; i < numsSize; i++) {
        tmp += nums[i];

        if (tmp > max)
            max = tmp;
        
        if (tmp < 0)
            tmp = 0;
    }

    return max;
}
