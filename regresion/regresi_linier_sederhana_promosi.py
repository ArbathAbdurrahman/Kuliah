import matplotlib.pyplot as plt
from scipy import stats

# data promosi
# x = [10,28,29,35,48,55,71,73,80,88,91,111,131,144,160]
# y = [29,47,55,65,79,82,92,95,100,102,110,124,127,130,152]

# rumah
x = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]
y = [245,312,279,308,199,219,405,324,319,255]

print(len(x))
print(len(y))
slope,intercept,r,p,std_err = stats.linregress(x,y)
print("Slope =",slope)
print("Intercept =",intercept)
print("R =",r) #keakuratan
print("error =",std_err)

def wkwk(x):
    return slope * x + intercept

mymodel = list(map(wkwk,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()

print("jika biaya promosi = ", wkwk(2000))