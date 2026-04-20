# Problem 71: Simplify Path

# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory 
# in a Unix-style file system, convert it to the simplified canonical path.
# Rules: 
# 1. A single period '.' means the current directory.
# 2. A double period '..' means moving up one directory level.
# 3. Multiple slashes such as '//' are treated as a single slash '/'.
# 4. The path must start with a single '/' and not end with a '/' unless it is just the root "/".

# Approach 1: Brute Force (slicing )
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = path.split("/")
        res = ""
        
        for i in range(len(parts)):
            fol = parts[i]
            if fol == "" or fol == ".":
                continue
                
            elif fol == "..":
                if res != "":
                    prev_slash_ind = res.rfind("/")
                    res = res[:prev_slash_ind]
                    
            else:
                res += "/" + fol
        
        if res == "":
            return "/"
        return res

# Time Complexity: O(n^2): concatenation and slicing forces comp to create new string copies repeatedly.

# Approach 2: Stack
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = path.split("/")
        stk = []
        
        for i in range(len(parts)):
            fol = parts[i]
            if fol == "" or fol == ".":
                continue
                
            elif fol == "..":
                if len(stk) > 0:
                    stk.pop()
                    
            else:
                stk.append(fol)

        return "/" + "/".join(stk)

# Time Complexity: O(N)