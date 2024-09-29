y = [245,312,279,308,199,219,405,324,319,255]
x = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]

sigmax = 0
for i in range(len(x)):
    sigmax += x[i]

sigmay = 0
for i in range(len(y)):
    sigmay += y[i]

sigmaxy = 0
for i in range(len(x)):
    sigmaxy += (y[i] * x[i])

sigmax2 = 0
for i in range(len(x)):
    sigmax2 += (x[i] * x[i])
sigmax_2 = sigmax * sigmax

n = 10

b = (n * sigmaxy - sigmax*sigmay) / (n * sigmax2 - sigmax_2)
a = (sigmay * sigmax2 - sigmax*sigmaxy)/(n*sigmax2-sigmax_2)

hasil = a+b*2000

print("sigma x :",sigmax)
print("sigma y :",sigmay)
print("sigma xy :",sigmaxy)
print("sigma x^2:",sigmax2)
print("sigma (x)^2 :",sigmax_2)
print("untuk a :",a)
print("untuk b :",b)
print("hasilnya adalah",hasil)



