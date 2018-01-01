#coding:utf-8
'''
Created on 2016年11月29日

@author: admin
'''
from testLogin import HDU
from time import sleep
lang = 0
pid = 1000
code = '''
#include<stdio.h>
int main()
{
 int a,b;
 while(scanf("%d%d",&a,&b)!=EOF)
 printf("%d\\n",a+b);
 return 0;
}
'''
hdu = HDU('1881140227','WWYhao110') 
if(hdu.login()):
    if(hdu.submit(pid, lang, code)):
        sleep(2)
        hdu.getstatus()
