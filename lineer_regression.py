import matplotlib.pyplot as plt
import numpy


#this is change
all_dict={}


m=open('physics_midterm.txt','r')
f=open('physics_final.txt','r')
for row in m:
    all_dict[row[0:11]]=[row[12:16]]

for row in f:
    all_dict[row[0:11]].append(row[12:16])
print(all_dict)
#cleaning data
cl_dict={}
for i in all_dict:

    try:
        if not( all_dict[i][0]==''or all_dict[i][1]==''or all_dict[i][0]=='0.00'or all_dict[i][1]=='0,00'):
            cl_dict[i]=all_dict[i]
    except:
        pass
print(cl_dict)
#dividing
x=[]
y=[]
for i in cl_dict:
    x.append(int(float(cl_dict[i][0].replace(',','.'))))
    y.append(int(float(cl_dict[i][1].replace(',','.'))))
print((x))
print((y))
mymodel = numpy.poly1d(numpy.polyfit(x, y, 6))

myline = numpy.linspace(1, 100, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()



