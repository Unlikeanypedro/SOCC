class Solution(object):
    def myAtoi(self, s):

        s = str(s)
        signal_ocurred = False
        value = ""
        i = 0

        while i < len(s):

            if not ( s[i] == " " or ord(s[i]) == 34):

                if s[i] in "0123456789":
                    value += s[i]
                    i += 1
                    signal_ocurred = True
            
                elif s[i] in "-+" and not signal_ocurred:
                    signal_ocurred = True
                    value += s[i]
                    i += 1

                else:
                    break

            else:
                if value:
                    break
                s = s[:i] + s[i+1:]

        
        if not value or (value in "+-"):
            return 0
        
        if int(value) >= (2**31):
            return 2**31 - 1

        if int(value) <= -(2**31):
            return -(2**31)

        return int(value) 


