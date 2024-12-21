def findpath2list(a,b):
    key = (a, b)
    if key in cache_findpath2list:
        return cache_findpath2list[key]
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
        result = [s2+"A"]
    elif c[1]==0:
        result = [s1+"A"]
    elif b==(1,0) or a==(1,0):
        if c[0]>0:
            result = [s1+s2+"A"]
        else:
            result = [s2+s1+"A"]
    else:
        result = [s1+s2+"A", s2+s1+"A"]
    cache_findpath2list[key] = result
    return result
    
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

mycode = ['0','1','2','3','4','5','6','7','8','9','A']

dictlevel1 = dict()
for i in mycode:
    for j in mycode:

        inp = i+j
        wordlist = level1list(inp)  
        print(inp)
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
print(dictlevel1)


def level1_v2 (solve):
    solve = "A" + solve
    print(solve)
    ans = ""
    for i in range(0, len(solve)-1):
        print(solve[i], solve[i+1], dictlevel1[(solve[i], solve[i+1])])
        ans=ans+  dictlevel1[(solve[i], solve[i+1])]
                  
    return ans

def findpath2_v2(a,b):
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
        return s2+"A"
    elif c[1]==0:
        return s1+"A"
    elif b==(1,0) or a==(1,0):
        if c[0]>0:
            return s1+s2+"A"
        else:
            return s2+s1+"A"
    else:
        return s1+s2+"A"

def level2_v2 (solve):
    keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

    solve = 'A'+solve
    ans = ""
    for i in range(0, len(solve)-1):
        ans = ans + findpath2_v2(keypad[solve[i]], keypad[solve[i+1]]) 
    return ans

inp = ["803A", "528A", "586A", "341A", "319A"]
nums =[803, 528, 586, 341, 319]

ans = 0
word = level1_v2(inp[i])  
w = level1_v2(level2_v2(word))
ans += len(w) * nums[i]
    
print(ans)