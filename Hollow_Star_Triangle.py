'''
#01_Star
* * * * * * * 
*           *
*           *
*           *
*           *
*           *
* * * * * * *
'''
n=int(input("Enter Number of Rows: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
#02_Star
* 
* * 
*   * 
*     * 
*       * 
*         * 
* * * * * * * 
'''
n=int(input("Enter Number of Rows: "))
for i in range(n):
    for j in range(i+1):
        if j==0 or i==n-1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#03_Star
Comming Soon.....
'''