import random
import time

count = 0
o = 0 #кіль.обмінів
start_time = 0
finish_time = 0

def sort(arr, size):
    global  count, o, start_time, finish_time

    
    for run in range(size-1):
        for i in range(size-1-run):
            count +=1
            if arr[i] > arr[i+1]:
                o +=1
                arr[i], arr[i+1] = arr[i+1],arr[i]
    # print(count)
                
arr = [random.randint(-1000, 1000) for _ in range(100)]
print("start arr: \n", arr)
print("\n")
start_time = time.time()
sort(arr, len(arr))

print("sort:\n", arr)
print("\n")
finish_time = time.time() - start_time
print("the lenght arr: ", len(arr))
print("time run : ", finish_time)
print("number of comparisons:" , count)
print("number of swamping:", o)
print("\n")
print("\n")


coun = 0
ob = 0 #кіль.обмінів
star_time = 0
end_time = 0

def ShellSort(data, size):
    interval = size // 2
    global  coun, ob, star_time, end_time
  
    
    while interval > 0:
        for i in range(interval, size):
            temp = data[i]
            j = i
            
            while j >= interval:
                if data[j - interval] <= temp:
                    break
                data[j] = data[j - interval]
                j -= interval
                ob += 1
                coun += 1
            data[j] = temp
            ob += 1
        interval //= 2
    
    
    
    return coun, ob, end_time

data =[random.randint(-1000, 1000) for _ in range(100)]
print("start arr:", data)
star_time = time.time()
print("\n")

ShellSort(data, len(data))
print('sorted :', data)
end_time = time.time() - start_time
print('length of array:', len(data))
print('time run:', end_time)
print('number of comparisons:', coun)
print('number of swappings:', ob)


