import os

#Utility function
def blockSwap(arr,d,i,n):
    if d < n/2:
        arr =  arr[-d:]+arr[d:n-d]+arr[i:d]
        return arr
    else:
        arr = arr[d:]+arr[n-d:d]+arr[i:n-d]
        return arr


#Main function
if __name__ == '__main__':
    Path = os.getcwd()
    input = open(Path+'/input.txt','r')
    output = open(Path+'/output.txt','w')

    arr = list(map(int,input.readline().split()))
    d = int(input.readline())
    newArr = blockSwap(arr,d,0,len(arr))

    output.write(str(newArr))
    output.close()