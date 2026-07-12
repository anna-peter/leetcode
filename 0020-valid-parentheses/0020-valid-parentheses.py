class Solution:
    def isValid(self, s: str) -> bool:
        # write a map of each open bracket and its count
        # a corresponding closed bracket deducts the count (check if its>0 first)
        # final state should be 0 for all
        # opened_brackets = {"(":0, "{":0, "[":0}
        # for bracket in s:
        #     print(bracket)
        #     if bracket in opened_brackets:
        #         opened_brackets[bracket] +=1
        #         print("added "+bracket)
        #         continue
        #     target = self.reverse(bracket)
        #     print("target "+target)
        #     if target in opened_brackets.keys() and opened_brackets.get(target)>0:
        #         opened_brackets[target]-=1
        #     else:
        #         return False
        # print("brackets "+str(opened_brackets))
        # return all(brack==0 for brack in opened_brackets.values())
        if len(s)==1:
            return False
        brackets = []
        for brack in s:
            comp = self.reverse(brack)
            if comp =="":
                # we have an opening bracket, add it
                brackets.append(brack)
                continue
            # we have a closed bracket but no corresponding open ones
            if len(brackets)==0:
                return False
            # closed bracket, check if the last item on the stack is the complement, return false if not
            if brackets.pop() != comp:
                return False
        # check if the stack is empty, we should have popped all open brackets
        return len(brackets)==0



    
    def reverse(self, b:str)-> str:

        brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
        }
        return brackets.get(b,"")
            