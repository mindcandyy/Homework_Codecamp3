#!/usr/bin/env python
# coding: utf-8

# In[1]:


#quiz1
#ข้อ1
2345%13


# In[ ]:





# In[3]:


#ข้อ2
1567//17


# In[4]:


#ข้อ3
FirstName = 1
Firstname = 2
print(FirstName, Firstname)
#ไม่


# In[5]:


#ข้อ4
13Friday = 2
print(13Friday)
#ไม่ถูกต้อง


# In[6]:


#ข้อ5
print("{},{}".format(5,92))


# In[5]:


#Quiz2
#1
x = lambda y: y/3
print(x(3))


# In[6]:


#2
def avg(a,b,c,d):
    print((a+b+c+d)/4)
avg(1,2,3,4)


# In[8]:


#3
avg2 = lambda x,y,z: (x+y+z)/3
print(avg2(1,2,3))


# In[26]:


#quiz3
#1
lst = ["Yada","Klueabvichit",20]


# In[27]:


#2
del lst[2]
print(lst)


# In[33]:


#3
lst.insert(0,10)
print(lst)


# In[47]:


#4
del lst[3:]
lst.append(162)
lst.append(50)
print(lst)


# In[48]:


print(lst[3:])


# In[53]:


#quiz4
#1
a = [[[1,3],[3,4]],[5,[5,6]],[7,8]]
a[1][1][1]


# In[54]:


#2
lst2 = [["a","b",3],["c","d",10],["e","f",20],["g","h",12]]


# In[55]:


#3
del lst2[3]
print(lst2)


# In[58]:


#4
lst2.insert(0,["x","y",25])
print(lst2)


# In[67]:


lst2 = [["a","b",3],["c","d",10],["e","f",20],["g","h",12]]
del lst2[3]
lst2.insert(0,["x","y",25])


# In[68]:


#5
lst2[1][2] += 10
print(lst2)


# In[73]:


#quiz5
#1
lst3 = [1,2,3,4,5,6,7,8,9,10]
result = map(lambda x: x**3, lst3)
print(list(result))

def cube(x):
    return x**3
print(list(map(cube,lst3)))


# In[79]:


#2
final = filter(lambda x: (x**2)%2 != 0, lst3)
print(list(final))

def fnction(x):
    return (x**2)%2 != 0
print(list(filter(fnction,lst3)))


# In[80]:


#Quiz6
#1
lst4 = [1,2,3,4,5]
result3 = [(x*2)-1 for x in lst4]
print(result3)


# In[81]:


#2
lst5 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
result4 = [x**3 for x in lst5 if x%3 != 0]
print(result4)


# In[84]:


#quiz7
score = int(input())
if score >= 80:
    print("A")
elif score >= 70 and score < 80:
    print("B")
elif score >= 60 and score < 70:
    print("C")
elif score >= 50 and score < 60:
    print("D")
else:
    print("F")


# In[85]:


#quiz8
#1
A = [1,2,3,4,5]
B = [2,3,1,3,2]
result5 = map(lambda x,y: y**x, A,B)
print(list(result5))


# In[86]:


#2
name = ["a","b","c"]
number = [1,2,3]
final_score = [20,25,30]
mapped = list(zip(name,number,final_score))
print(mapped)


# In[87]:


#Quiz9
#1
from functools import reduce
lst6 = [5,2,1,3,2]
result6 = reduce(lambda x,y: x**y,lst6)
print(result6)


# In[88]:


#2
lst7 = [1,2,3,4,5,6,7,8,9,10]
result7 = reduce(lambda x,y : x*y,lst7)
print(result7)

