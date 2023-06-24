int romanToInt(char * s)
{
    int num=0; char x; int n=strlen(s);
        for(int i=0;i<n;i++)
        {
            if(s[i]=='I')
            {
                if(s[i+1]!='V'&&s[i+1]!='X')
                num+=1;
                else if(s[i+1]=='V'||s[i+1]=='X')
                num-=1;
            }
            if(s[i]=='V')
            num+=5;
            if(s[i]=='X')
            {
                if(s[i+1]!='L'&&s[i+1]!='C')
                num+=10;
                else if(s[i+1]=='L'||s[i+1]=='C')
                num-=10;
            }
            if(s[i]=='L')
            num+=50;
            if(s[i]=='C')
            {
                if(s[i+1]!='D'&&s[i+1]!='M')
                num+=100;
                else if(s[i+1]=='D'||s[i+1]=='M')
                num-=100;
            }
            if(s[i]=='D')
            num+=500;
            if(s[i]=='M')
            num+=1000;
        }
        return(num);
}
