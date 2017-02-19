"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""

"""
# 只在 python3 中好用
def t1():
    # 在python3中好用，2中不行
    # 
    s = "   - 321"
    
    while s:
        if s[0] in [" ", "  "]:
            s = s[1:]
        else:
            break

    try:
        w = int(s) # 在python2中，int("- 3") => -3
    except Exception as e:
        w = 0
        for i in range(0, len(s)):
            try:
                w = int(s[:i+1])
            except Exception as e:
                if i == 0:
                    continue
                else:
                    break
    if w >= 2**31:
        w = 2**31-1
    if w <= -2**31-1:
        w = -2**31
    return w
"""

# 在python2 和 python3中都可以
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        d = [str(i) for i in range(10)]
        r = []
        start = False

        while s:
            if s[0] in [" ", "  "]:
                s = s[1:]
            else:
                break

        f = ["+", "-"]
        if not s:
            return 0
        if s in f:
            return 0

        if s[0] not in f and s[0] not in d:
            return 0
        if len(s) > 1:
            if s[0] in f and s[1] not in d:
                return 0

        for i in range(1, len(s)):
            if s[i] in d:
                r.append(s[i])
            else:
                break
        r.insert(0, s[0])
        ret = "".join(r)
        if not ret:
            return 0
        w = int(ret)
        if w >= 2**31:
            w = 2**31-1
        if w <= -2**31-1:
            w = -2**31
        return w