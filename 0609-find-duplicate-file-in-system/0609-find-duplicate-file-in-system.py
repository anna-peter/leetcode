from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # goal: return an array of arrays, where the contents of each file in a given array are equal (duplicate)

        # an input string is structured as ("file_path","file_name.ext", "file_name.ext",...)

# so we can split it out by the first " " to get the root and set of files

# create a set {} of file contents that were already seen
# should be like set["root/a/3.txt"]="(abcd)" where we always add the count
        seen = defaultdict(list)

        content_counts = defaultdict(list) #content_counts['(abcd)'] = 0 , etc

        duplicates = []


# when a file is seen for the second time, add it to the duplicates 
# but - how do we add the first file?? 

# first loop through the paths
        for dir in paths: 
            # then split out the root and files 
            root, files = dir.split(" ", 1)

            # loop through each file and grab contents
            for file in files.split(" "):
                file_name, content_tail = file.split("(")
                content = "("+ content_tail # we split it but add back the bracket to get (abcd)
                # print(content)
                
                file_path = root + "/"+file_name
                # print(f" file path {file_path} ")

                seen[content].append(file_path)
                # print(seen)

        duplicates = [path_arr for path_arr in seen.values() if len(path_arr)>1]
        # print(duplicates)
        return duplicates

                


        # add all file paths and then drop the subarrays with len ==1

            

# 