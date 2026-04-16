class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {']' : '[',
        '}' : '{', ')' : '('}
        for i in s:
            if i in my_dict:
                top_element = stack.pop() if stack else '#'
                if my_dict[i] != top_element:
                    return False           
            else:
                stack.append(i)
        return stack == []




            
        

        