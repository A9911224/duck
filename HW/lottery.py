# coding: utf-8
get_ipython().magic('pylab inline')
a = input("第一個數字")
b = input("第二個數字")
c = 0
if float(a)%2==1:
    c=c+100
if float(b)%3==2:
    c=c+200
if a==b:
    c=c+50
print("您中了",c,"元")
