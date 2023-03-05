# 221RDB124 Veronika Musijaka 13.gr

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    # Initialize all heights to -1
    heights = [-1] * n

    def get_heights(node):
        # If the height of the node has already been calculated, return it
        if heights[node] != -1:
            return heights[node]
        # If the node is the root, its height is 1
        if parents[node] == -1:
            heights[node] = 1
        else:
            # Calculate the height of the parent and add 1 to it to get the height
            heights[node] = get_heights(parents[node]) + 1
        return heights[node]


    max_height = 0
    # Your code here
    for i in range(n):
        max_height = max(max_height, get_heights(i))
    return max_height


def main():
    # implement input form keyboard and from files
    user_input = str(input())
    if "I" in user_input:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    elif "F" in user_input:
        filename = str(input())
    # let user input file name to use, don't allow file names with letter a
        if "a" in filename:
            print("Enter a file name without letter 'a'")
            return
    # account for github input inprecision
        filename = "test/" + str(filename)
        
        with open(filename, 'r') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        print(compute_height(n, parents))
       
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))