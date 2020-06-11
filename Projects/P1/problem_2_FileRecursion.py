#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if os.path.isfile(path): # edge case, when suppied path is a file by itself -- added as per suggestion in code review
        if path.endswith(suffix):
            return [path]

    path_list = []
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        
        if os.path.isfile(file_path) and file_path.endswith(suffix):
            path_list.append(file_path)
            
        elif os.path.isdir(file_path):
            path_list.extend(find_files(suffix, file_path))
            
    return path_list

def test_file_recursion():
    print("\nTest case 1: attempt to get files with suffix present under path")
    file_list_1 = find_files(".c", "./testdir")
    print(f"Files found: {len(file_list_1)}")
    print(*file_list_1, sep='\n')
    # Files found: 4
    # ./testdir/subdir3/subsubdir1/b.c
    # ./testdir/t1.c
    # ./testdir/subdir5/a.c
    # ./testdir/subdir1/a.c

    print("\nTest case 2: attempt to get files with suffix present under path -- same as test case but different extension")
    file_list_2 = find_files(".gitkeep", "./testdir")
    print(f"Files found: {len(file_list_2)}")
    print(*file_list_2, sep='\n')
    # Files found: 2
    # ./testdir/subdir4/.gitkeep
    # ./testdir/subdir2/.gitkeep

    print("\nTest case 3: attempt to get files with suffix NOT present under path")
    file_list_3 = find_files(".txt", "./testdir")
    print(f"Files found: {len(file_list_3)}")
    print(*file_list_3, sep='\n')
    # Files found: 0
    # 

    print("\nTest case 4: attempt to get files with suffix when supplied path is a file itself") # added as per suggestion in code review
    file_list_4 = find_files(".c", "./testdir/t1.c")
    print(f"Files found: {len(file_list_4)}")
    print(*file_list_4, sep='\n')
    # Files found: 1
    # ./testdir/t1.c

if __name__ == "__main__":
    test_file_recursion()

