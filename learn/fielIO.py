s = "hello world \n 中国人"
# with open('test.txt','a+') as f:
#     f.write(s)
#
# with open('test.txt','r') as f:
#     content = f.read()
#     print(content)

# import pickle
# n = 7
# i = 120000
# lst = [[1,2,3],[2,3,4]]
# f = open('test2.dat','wb')
# try:
#     pickle.dump(n,f)
#     pickle.dump(i,f)
#     pickle.dump(lst,f)
# except:
#     print("io error")
# finally:
#     f.close()
# import pickle
#
# f = open('/home/sholy/can_0.bin','rb')
# # n = pickle.load(f)
# for i in range(1000):
#     x = pickle.load(f)
#     print(x)
# f.close()
# import psutil
# print(psutil.cpu_count())
# print(psutil.cpu_count(logical=False))
# print(psutil.cpu_percent())
# print(psutil.cpu_percent(percpu=True))
