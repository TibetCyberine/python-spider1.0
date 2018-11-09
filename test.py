
#多个变量换行输出，如何定义间隔
'''!!
a,b,c=1,2,3
print(a,b,c,sep ="\n")
'''
#这种输出方法换行时会多出一个空格符号。
'''
a,b,c=1,2,3
print (a,"\n",b,"\n",c)
'''
#while 循环
"""
apple = 1
while (apple<= 10):
    print(apple)
    apple = apple +1
"""
'''
while True:
    print("i'm true")
'''
#for循环
'''
t_list = [1,2,5,6,879,46,864,784,6122,7987,5]
for i in t_list:
        print(i)
print("over")
'''
#for 内置函数range,(1,10)意思是1到9
#默认取值宽度是1，输出为1，2，3，4，5，6，7，8，9
#（1，10，2）的意思是从1到9
#取值宽度是2，输出为1，3，5，7，9
''''
for i in range(1,10,2):
        print(i)
print("over")
'''
#if else 和elif（else if）
'''
apple =int (input("请输入一个正整数\n"))
if apple<10:
	print("apple<10")
elif apple ==10:
	print("apple = 10")
else:
	print("apple > 10")
print("over")
'''
#定义函数
'''
def apple():
	print("这是一个函数")
appl = 10
while  appl==10:
	apple()
	appl=appl-1
''' 
#含参数函数调用
'''
def app(a,b):
	c=a**b
	print("c is ",c)

app(5,6)
'''
#p14
#莫烦pyhon
##
##写文件和追加文件
'''
apptext = "\n追加"
my_file = open("my_file.txt","a")
my_file.write(apptext)
my_file.close()
'''
###读文件
file = open ("my_file.txt","r")
content = file.read()
print(content)


































