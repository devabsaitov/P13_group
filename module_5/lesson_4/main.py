from task import send_file
import time
gmails = [
    "muhammadnurpdp@gmail.com",
    "zokirislom01@gmail.com",
    "abdulboriy0207@gmail.com",
    "mirahmadhacker2007@gmail.com",
    "zikrilloh797@gmail.com",
    "qohhorovusmonjon@gmail.com",
    "ozodbekaxrorov3@gmail.com",
    "abdusalomabduvaliyev07@gmail.com",
    "Mr.Xayrullayev1506@gmail.com",
    "xaffiz92@gmail.com",
    "tamannoumarova321@gmail.com",
    "esamuratovf@gmail.com",
    "mirmukhammadmirkabilov@gmail.com"
]

start = time.time()
for i in gmails:
    send_file.delay(i)
print(time.time()-start)





