bool isPalindrome(int x)
{
    if(x<0)
    return false;
    if(x==0 || x/10==0)
    return true;
    
    long rev_x=0;
    int og_x=x;
    int rem;
    while(x!=0)
    {
        rem=x%10;
        rev_x=rev_x*10+rem;
        x=x/10;
    }
    if(rev_x==og_x)
    return(true);
    else
    return(false);
}
