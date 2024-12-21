def findpath2list(a,b):
    c = (b[0]-a[0], b[1]-a[1])
    s1=""
    s2=""
    
    if c[0]>0:
        s1 = "v"*abs(c[0])
    elif c[0]<0:
        s1 ="^"*abs(c[0])
        
    if c[1]>0:
        s2 = ">"*abs(c[1])
    elif c[1]<0:
        s2 ="<"*abs(c[1])
        
    if c[0]==0:
        return [s2+"A"]
    elif c[1]==0:
        return [s1+"A"]
    elif b==(1,0) or a==(1,0):
        if c[0]>0:
            return [s1+s2+"A"]
        else:
            return [s2+s1+"A"]
    else:
        return [s1+s2+"A", s2+s1+"A"]
    
def findpathlist (a, b):
    c = (b[0]-a[0], b[1]-a[1])
    s1=""
    s2=""
    
    
    if c[0]>0:
        s1 = "v"*abs(c[0])
    elif c[0]<0:
        s1 ="^"*abs(c[0])
        
    if c[1]>0:
        s2 = ">"*abs(c[1])
    elif c[1]<0:
        s2 ="<"*abs(c[1])
        
    
    if c[0]==0:
        return [s2+"A"]
    elif c[1]==0:
        return [s1+"A"]
    
    if a[0]==3 and b[1]==0:
        return [s1+s2+"A"]
    elif b[0]==3 and a[1]==0:
        return [s2+s1+"A"]
    
    else:
        return [s1+s2+"A", s2+s1+"A"]
  
  
def level1list (solve):
    keypad = {"7": (0, 0), "8": (0, 1), "9": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "1": (2, 0), "2": (2, 1), "3": (2, 2), "0": (3, 1), "A": (3, 2)}
    
    ans = [""]
    for i in range(0, len(solve)-1):
        temp = findpathlist(keypad[solve[i]], keypad[solve[i+1]])
        output = []
        for x in ans:
            for y in temp:
                output.append(x+y)
        ans = output.copy()            
    return ans

def level2list (solve):
    keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

    solve = 'A'+solve
    ans = [""]
    for i in range(0, len(solve)-1):
        temp = findpath2list(keypad[solve[i]], keypad[solve[i+1]])
        output = []
        for x in ans:
            for y in temp:
                output.append(x+y)
        ans = output.copy()  
    return ans

        
inp = ["540A", "839A", "682A", "826A", "974A"]
nums =[540, 839, 682, 826, 974]

# ans = 0
# for i in range(len(inp)):
#     wordlist = level1list(inp[i])  
#     #print("wordlist", wordlist)
#     wordlist2 = []
#     wordlist3 = []
#     for word in wordlist:
#         for w in level2list(word)

#             wordlist2.append(w)
#     #print(wordlist2)
#     for word in wordlist2:
#             for w in level2list(word)

#                 wordlist3.append(w)
#     best = len(wordlist3[0])
#     bestanswer = wordlist3[0]
#     for item in wordlist3:
#         if len(item)< best:
#             best = len(item)
#             bestanswer = item
#     print(bestanswer)
#     print(best)
#     ans += best * nums[i]
    
# print(ans)

mycode = ['0','1','2','3','4','5','6','7','8','9','A']

dictlevel1 = dict()
for i in mycode:
    for j in mycode:

        inp = i+j
        wordlist = level1list(inp)  
        # print(inp)
        wordlist2 = dict()
        wordlist3 = dict()
        for word in wordlist:
            for w in level2list(word):
                wordlist2[w] = word
        #print(wordlist2)
        for word in wordlist2.keys():
                for w in level2list(word):
                    wordlist3[w]=word
        best = len(list(wordlist3.keys())[0])
        bestanswer = list(wordlist3.keys())[0]
        for item in wordlist3.keys():
            if len(item)< best:
                best = len(item)
                bestanswer = item
        word2 = wordlist3[bestanswer]
        word1 = wordlist2[word2]
        dictlevel1[(i,j)] = word1
# print(dictlevel1)


def level1_v2 (solve):
    solve = "A" + solve
    # print(solve)
    ans = ""
    for i in range(0, len(solve)-1):
        #print(solve[i], solve[i+1], dictlevel1[(solve[i], solve[i+1])])
        ans=ans+  dictlevel1[(solve[i], solve[i+1])]
                  
    return ans

def findpath2_v2(a,b):
    c = (b[0]-a[0], b[1]-a[1])
    s1=""
    s2=""

    if a == (0, 1) and b == (1, 2):
        return "v>A"
    if b == (0, 1) and a == (1, 2):
        return "<^A"
    
    if a == (0, 2) and b == (1, 1):
        return "<vA"
    if b == (0, 2) and a == (1, 1):
        return "^>A"

    if c[0]>0:
        s1 = "v"*abs(c[0])
    elif c[0]<0:
        s1 ="^"*abs(c[0])
        
    if c[1]>0:
        s2 = ">"*abs(c[1])
    elif c[1]<0:
        s2 ="<"*abs(c[1])
        
    if c[0]==0:
        return s2+"A"
    elif c[1]==0:
        return s1+"A"
    elif b==(1,0) or a==(1,0):
        if c[0]>0:
            return s1+s2+"A"
        else:
            return s2+s1+"A"
    else:
        return s2+s1+"A"

def level2_v2 (solve):
    keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

    solve = 'A'+solve
    ans = ""
    for i in range(0, len(solve)-1):
        ans = ans + findpath2_v2(keypad[solve[i]], keypad[solve[i+1]]) 
    return ans


calc_cash = dict()
def calc(codes, power):
    if power==0:
        return len(codes)
    else:
        s = codes.split('A')
        s.pop()
        ins = 0 
        for i in range(len(s)):
            s[i] = s[i]+"A"
            if (s[i],power) in calc_cash.keys():
                ins+=calc_cash[(s[i],power)]
            else:
                temp = calc(level2_v2(s[i]),power-1)
                calc_cash[(s[i],power)] = temp
                ins+=temp
        return ins
            

inp = ["803A", "528A", "586A", "341A", "319A"]
nums = [803, 528, 586, 341, 319]

ans = 0
for i in range(len(inp)):
    word = level1_v2(inp[i])  

    w = level2_v2(word)
    temp = calc(w, 24)
    ans += temp * nums[i]
    
print(ans)