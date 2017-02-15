# coding: utf-8
# 利用 kmp 算法匹配子串


def overlay(p):
    ret = {}
    ret[0] = -1

    suit = False # 上一个是否是匹配的
    i = 1
    k = 0 # 匹配上的个数
    while i < len(p):
        if suit == False:
            if p[0] == p[i]:
                ret[i] = 0
                suit = True
                k += 1
            else:
                ret[i] = -1
                k = 0
        else:
            if p[k] == p[i]:
                k += 1
                ret[i] = k - 1
                suit = True
            else:
                j = 0
                start = i-k+1
                while start + j <= i:
                    if p[j] == p[start+j]:
                        j += 1
                    else:
                        start += 1
                        j = 0
                if j > 0:
                    suit = True
                else:
                    suit = False
                ret[i] = j-1
                k = j-1
        i += 1
    return ret


def t():
    s = "annbcadanacadsannannabnna"
    p = "annabbb"

    i = 0
    k = 0 # 已匹配的个数
    ret = overlay(p)

    while i < len(s)-len(p)+1:

        for j in range(len(p)):
            if p[j] == s[i+j]:
                k += 1
            else:
                if ret[k] > -1:
                    i = i + k - ret[k]
                else:
                    i += 1
                k = 0
                break
        if k == len(p):
            return i

    else:
        return -1 # 不匹配


if __name__ == "__main__":
    k = t()
    print(k)