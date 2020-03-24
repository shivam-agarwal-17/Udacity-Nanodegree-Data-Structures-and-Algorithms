## File Recursion

### Design Choice

In this problem, we are required to find the list of files matching given suffix under given directory. Python list being a dynamic array was a natural choice to keep appending file paths as and when encountered while traversing directory and it's sub-directories.

### Time Complexity

Each file or sub-directory under the input directory is only visited once, hence, it follows linear time complexity -- O(N) where, N is total number of entities counted recursively under the input directory.

### Space Complexity

Assuming N is total number of entities counted recursively under the input directory, then, we would have a function call stack of space complexity O(N) as I call find_files() recursively at each sub-drectory. 

I also maintain a list of files, that would have a space complexity of O(N).