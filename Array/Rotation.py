import os

#Utility function

#Main function
if __name__ == '__main__':
    Path = os.getcwd()
    input = open(Path+'/input.txt','r')
    output = open(Path+'/output.txt','w')

    arr = list(map(int,input.readline().split()))
    d = int(input.readline())
    arr = arr[d:]+arr[0:d]

    output.write(str(arr))
    output.close()