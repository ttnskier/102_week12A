#https://github.com/ttnskier/102_week12A.git
#Tanner Elliott
#​CSCI 102 – Section C
#Week 12 - Part B
def PrintOutput(string):
    print('OUTPUT ', string)
def LoadFile(path):
    f = open(path , "r")
    out = []
    for x in f:
        out = out.append(f.readline())
    return out
def UpdateString(string , let , i):
    li = [ char for char in string]
    li[i] = let
    out = ""
    for x in li:
        out += x
    print('OUTPUT ' , out)
def FindWordCount( string , li ):
    out = string.count(li)
    return out
def ScoreFinder(names , scores , player):
    if player.capitalize() in names:
        a = names.index(player.capitalize())
        out = scores[a]
        print('OUTPUT ', player.capitalize() , 'got a score of ' ,out)
    else:
        print('OUTPUT player not found')
def Union(lst1 , lst2):
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 
def Intersection(lst1 , lst2 ):
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
def NotIn(lst1 , lst2):
    lst3 = [value for value in lst1 if value not in lst2] 
    return lst3 
