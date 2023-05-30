# IO -> Input Output



#
#
# import time
# import threading
#
# def test(n):
#     time.sleep(1)
#     print(n)
#
#
# start = time.time()
# threads= []
# for i in range(1000000):
#     thread = threading.Thread(target=test, args=(i,))
#     thread.start()
#     threads.append(thread)
#
# for i in threads:
#     i.join()
#
# print(time.time() - start)




# f1 -> 5 secund,
# f2 -> 10 secund,
# f3 > 6 secund
#
# import time
# import threading
# def f1():
#     time.sleep(5)
#     print("f1")
#
# def f2():
#     time.sleep(10)
#     print("f2")
#
# def f3():
#     time.sleep(6)
#     print("f3")
#
#
# if __name__ == '__main__':
#
#     start = time.time()
#     thread1 = threading.Thread(target=f1)
#     thread2 = threading.Thread(target=f2)
#     thread3 = threading.Thread(target=f3)
#
#     thread1.start()
#     thread2.start()
#     thread3.start()
#     thread3.join()
#     thread2.join()
#     thread1.join()
#
#     print(time.time() -start)


# MultiProcessing

# import multiprocessing
# import time
# def f1(name):
#     time.sleep(2)
#     return "Hello " + name
#
# start = time.time()
# print(multiprocessing.cpu_count())
# with multiprocessing.Pool(8) as p:
#     print(p.map(f1, range(1,1000)))
#
# print(time.time() - start)

import multiprocessing
import time


def f1(n):
    time.sleep(2)
    print(n)

def f2(n):
    time.sleep(2)
    print(n)

def f3(n):
    time.sleep(2)
    print(n)

if __name__ == '__main__':
    mpl = []
    start = time.time()

    mp = multiprocessing.Process(target=f1 , args=(1,))
    mp1 = multiprocessing.Process(target=f2 , args=(2,))
    mp2 = multiprocessing.Process(target=f3 , args=(3,))
    mp.start()
    mp1.start()
    mp2.start()

    mp.join()
    mp1.join()
    mp2.join()


    print(time.time() - start)

# def file_open(filename):
#     with open(filename , "r") as f:
#         data = f.read()
#     return data
#
# def file_write(filename, data):
#     with open(filename , "w") as f:
#         f.write(data)











