import threading
import time

reciptionist = threading.Semaphore(1)

def enter_examinationroom(n):
    print(f"patient {n} is waiting for his turn")
    reciptionist.acquire()
    print(f"patient {n} is in the examination room")
    time.sleep(2)
    print(f"patient {n} is out of the examination room")
    reciptionist.release()

patients = []
for i in range(5):
    Patient = threading.Thread(target=enter_examinationroom,args=(i,))
    patients.append(Patient)
    Patient.start()








# import threading
# import time

# reciptionist = threading.Semaphore(1)

# def enter(n):
#     print(f"patient {n} is waiting")
#     reciptionist.acquire()
#     print(f"patient {n} entered")
#     time.sleep(3)
#     print(f"patient {n} out")
#     reciptionist.release()

# patients = []
# for i in range(5):
#     patient = threading.Thread(target=enter,args=(i,))
#     patients.append(patient)
#     patient.start()