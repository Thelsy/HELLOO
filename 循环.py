# 列表之循环
name1 = [1, 2, 3, 4]
for st in name1:
    print(st)
print("----------------------------------------------")
# range(开始数，结束数，1/2)此方法能生成你指定范围的数字需要指定开始数&结束数，其中第三个参数可以来控制生成的数是奇数还是偶数
# 九九乘法表
for s in range(1, 10):
    for i in range(1, s+1):
        print(str(s)+" X "+str(i)+" = "+str(s * i),end=" ")
    print()
print("----------------------------------------------")
# 计算1，10的乘方运算
sum1 = []
for i in range(1,11):
    sum1.append(i**2)
print(sum1)
print("----------------------------------------------")
# 对数字进行简单运算的方法 min()求出最小值，max()最大值，sum()总和

for i in range(1, 21):
    print(i)


st = []
for i in range(1, 1000000+1):
    st.append(i)
print(min(st), max(st))
print(sum(st))
st1 = []
for i in range(1, 22, 2):
    st1.append(i)
for stq in st1:
    print(stq)




name2 = [1, 2, 3, 4]
print(name2[:])