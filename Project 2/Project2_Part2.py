import random
import math
import csv 

csvFile = open("outputCSV.csv","w")
txt = open("output.txt","w+")
write_outfile = csv.writer(csvFile)

def ValidateInputLine(fileinput):
    job = fileinput.split()
    if job[2] == "Small":
        if int(job[3]) > 3 and int(job[3]) < 7:
            if int(job[4]) > 39 and int(job[4]) < 81:
                if int(job[5]) > 19 and int(job[5]) < 41:
                    if 0 == int(job[6]) % 50:
                        ReturnJob =[int(job[0]),int(job[1]),job[2],int(job[3]),int(job[4]),int(job[5]),int(job[6])]
                        return ReturnJob
                    
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    if job[2] == "Medium":
        if int(job[3]) > 8 and int(job[3]) < 12:
            if int(job[4]) > 59 and int(job[4]) < 121:
                if int(job[5]) > 39 and int(job[5]) < 81:
                    if 0 == int(job[6]) % 100:
                        ReturnJob=[int(job[0]),int(job[1]),job[2],int(job[3]),int(job[4]),int(job[5]),int(job[6])]
                        return ReturnJob
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    if job[2] == "Large":
        if int(job[3]) > 23 and int(job[3]) < 27:
            if int(job[4]) > 119 and int(job[4]) < 221:
                if int(job[5]) > 59 and int(job[5]) < 111:
                    if 0 == int(job[6]) % 250:
                        
                        ReturnJob =[int(job[0]),int(job[1]),job[2],int(job[3]),int(job[4]),int(job[5]),int(job[6])]
                        return ReturnJob
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

class Memory_Entire_Unit:

    def __init__(self, memBlock_sz, memTotal):
        self.memBlock_sz = memBlock_sz
        self.memTotal = memTotal
        self.entireMem = [[''] * memBlock_sz for i in range(memTotal)]

#=============================================================================================
#                   FUNCTIONS - GENERATE SMALL, MEDIUM, LARGE JOBS
#                             - GENERATE ARRIVAL TIME UNIT FOR EACH JOBS
#                             - VALIDATE USER INPUT FOR PERCENTAGES OF EACH TYPE OF JOB
# =============================================================================================

def GenerateTimeUnit(counter):
   timeUnit = 0
   timeUnit = random.randint(0, 4) + counter
   return (timeUnit)
 
 
def GenerateSmlJob(time, cnt_j):
   RunningSize = random.randint(4, 6)
   CodeSize = random.randint(40, 80)
   StackSize = random.randint(20, 40)
   HeapElement = RunningSize * 50
   txt.write(str(cnt_j)+" "+ str(time) + " Small " + str(RunningSize) + " " + str(CodeSize) + " " + str(StackSize) + " " + str(HeapElement)+"\n")
   write_outfile.writerow([str(cnt_j), str(time) , "Small" , str(RunningSize) , str(CodeSize) , str(StackSize) , str(HeapElement)])
 
def GenerateMedJob(time, cnt_j):
   RunningSize = random.randint(9, 11)
   CodeSize = random.randint(60, 120)
   StackSize = random.randint(40, 80)
   HeapElement = RunningSize * 100
   txt.write(str(cnt_j)+" "+str(time) + " Medium " + str(RunningSize) + " " + str(CodeSize) + " " + str(StackSize) + " " + str(HeapElement)+"\n")
   write_outfile.writerow([str(cnt_j),str(time) , "Medium " , str(RunningSize) , str(CodeSize) , str(StackSize) , str(HeapElement)])
 
 
def GenerateLrgJob(time, cnt_j):
   RunningSize = random.randint(24, 26)
   CodeSize = random.randint(120, 220)
   StackSize = random.randint(60, 120)
   HeapElement = RunningSize * 250
   txt.write( str(cnt_j)+ " " + str(time) + " Large " + str(RunningSize) + " " + str(CodeSize) + " " + str(StackSize) + " " + str(HeapElement)+"\n")
   write_outfile.writerow([str(cnt_j), str(time) , "Large " , str(RunningSize) , str(CodeSize) , str(StackSize) , str(HeapElement)])
 
def CheckValidInt(jobs):
   while True:
       sml_job = input("please enter the percentage of " + jobs + " jobs ")
       try:
           sml_job = int(sml_job)
           if int(sml_job) < 0:
               print("A percentage must be 0 to 100")
           else:
               return sml_job
       except ValueError:
           print("Error! must be an integer number")
           
def printMemory(size, mem, blckSize):
    block = 0
    cell = 0

    print("===================================================")
    for block in range(len(size)):

        for cell in range(blckSize):

            if mem.entireMem[block][cell] != '':

                print(mem.entireMem[block][cell][0], end=" ")

            elif mem.entireMem[block][cell] == '':
                print('-', end=" ")

        print("\n")

Memory_IsFull = False
#=============================================================================
#
#       4 TYPES OF ALLOCATING ALGORITHMS FUNCTIONS
#           -First Fit
#           -Best Fit
#           -Next Fit
#           -Worse Fit
#       ALLOCATION and DEALLOCATION FUNCTIONS
#=============================================================================

#FIRST ALLOCATION FUNCTION 
#=============================================================================
def FFalloc(allMem, Job, blckSize, segment):
    cnt_block = 0
    loc_start = 0

    global Memory_IsFull

    tempSize = math.ceil(Job[segment] / blckSize)

    for loc in range(len(allMem.entireMem)):

        if allMem.entireMem[loc][0] == '':
            cnt_block = cnt_block + 1

        if cnt_block >= tempSize:
            loc_start = loc - tempSize + 1
            break

    if cnt_block < tempSize:
        Memory_IsFull = True

    return loc_start

#NEXT ALLOCATION FUNCTION 
#=============================================================================
def NFalloc(allMem, Job, blckSize, segment, loc):
    cnt_block = 0
    loc_start = 0
    start = loc
    tempSize = math.ceil(Job[segment] / blckSize)
    Found = False
    temp_loc =0
    
    global Memory_IsFull

    while loc < len(allMem.entireMem):

        if allMem.entireMem[loc][0] == '':

            temp_loc = loc

            while allMem.entireMem[temp_loc][0] == '' and temp_loc < len(allMem.entireMem) - 1:
                cnt_block += 1

                temp_loc += 1

            if cnt_block >= tempSize:
                Found = True
                loc_start = loc
                break
        
        cnt_block =0 
        
        if loc >= len(allMem.entireMem):
            loc = 0
            while loc < start:
                if allMem.entireMem[loc][0] == '':

                    temp_loc = loc

                    while allMem.entireMem[temp_loc][0] == '' and temp_loc < len(allMem.entireMem) - 1:
                        cnt_block += 1
                        temp_loc += 1

                    if cnt_block >= tempSize:
                        Found = True
                        loc_start = loc
                        break 
                    cnt_block =0 
        loc += 1
        
    if Found == False:
        Memory_IsFull = True

    return loc_start

#BEST ALLOCATION FUNCTION 
#=============================================================================
def BFalloc(allMem, Job, blckSize, segment):
    cnt_block = 0
    loc_start = 0
    loc = 0

    temp_loc = 0
    global Memory_IsFull
    foundSpace = False

    diff = 10000000000  # Large number to set it as default

    tempSize = math.ceil(Job[segment] / blckSize)

    BestFit = [loc_start, diff]

    while loc < len(allMem.entireMem):

        if allMem.entireMem[loc][0] == '':

            temp_loc = loc

            while allMem.entireMem[temp_loc][0] == '' and temp_loc < len(allMem.entireMem) - 1:
                cnt_block += 1
                temp_loc += 1

            diff = cnt_block - tempSize

            if diff < BestFit[1] and diff >= 0:
                foundSpace = True
                BestFit[0] = loc
                BestFit[1] = diff
            

            loc = temp_loc
            cnt_block = 0

        loc += 1

    if foundSpace == False:
        Memory_IsFull = True

    return BestFit[0]

#WORSE ALLOCATION FUNCTION 
#=============================================================================              
def WFalloc(allMem, Job, blckSize, segment):

    loc =0 
    size =0 
    
     
    temp_loc =0
    global Memory_IsFull
    
    WorseFit = [loc, size]

    cnt_block =0

    temp_loc =0
    found = False
    
    jobSize = math.ceil(Job[segment] / blckSize)

    while loc < len(allMem.entireMem):

        
        if allMem.entireMem[loc][0] =='':
            temp_loc  =loc
        
            while allMem.entireMem[temp_loc][0] == '' and  temp_loc != len(allMem.entireMem)-1 :
      
                cnt_block +=1 
                temp_loc +=1
                
            if cnt_block > WorseFit[1] and cnt_block >= jobSize:
                
                found = True
                WorseFit[0] = loc
                WorseFit[1] = cnt_block
                              
            cnt_block =0
            loc  = temp_loc
        
        loc+=1 
    
    if found  == False: 
        Memory_IsFull = True
           
    return WorseFit[0]
# ALLOCATING JOBS INTO MEMORY FUNCTION 
#=============================================================================       
def Allocation(myMemory, Job, loc, blckSize, segment):
    cell = 0
    block = 0
    cnt_cell = 0

    block = loc

    while cnt_cell < Job[segment]:

        if cell >= blckSize:
            cell = 0
            block += 1

        if block < len(myMemory.entireMem) and cell < blckSize:
            myMemory.entireMem[block][cell] = Job
            cell += 1

        cnt_cell += 1

# DE-ALLOCATING JOBS FROM MEMORY FUNCTION 
#=============================================================================  
def DeAllocation(myMemory, total_mem, blckSize, Jobs_InProgress):
    block = 0
    cell = 0

    for block in range(total_mem):

        for cell in range(blckSize):

            if myMemory.entireMem[block][cell] != '':

                if myMemory.entireMem[block][cell][0] == Jobs_InProgress[0]:
                    myMemory.entireMem[block][cell] = ''



# =============================================================================================
#                   MAIN ()- Random Job Generation
#                       -User Input for percentages of small, medium, Large
#                       -User Input for # of Cells in Memory Block, Memory Size
#                       -Option for losted objects
#                       -MEMORY ALLOCATION, DEALLOCATION
# =============================================================================================


JobHolder = []

time = 0
cnt_job =0
job_type = 0
job_arrv_tm = ""
job_info = ""

Jobs_InProgress = []
JobHeapList = []

cur_time = 0
start_loc = 0
job = 0

lenProgress = 0
lenJobElement = 0

heapRunTime = 0
heapSize = 0
heapJob = 0
heapType = 0

heap_alloc = 0

TotNumJobs = 50 


# =========================================================================================

#               -VALIDATES USER INPUT FOR PERCENTAGES OF SMALL, MEDIUM, LARGE
#                   TOTAL PERCENTAGES OF JOBS MUST ADD UP TO 100%
#               - GENERATE INPUT FILE OF RANDOMS (SMALL, MEDIUM, LARGE)
#
# =========================================================================================

while True:
   while True:
       sml_job = CheckValidInt("Small")
       break
   while True:
       med_job = CheckValidInt("Med")
       break
   while True:
       lrg_job = CheckValidInt("Large")
       break
   total = int(sml_job)+int(med_job)+int(lrg_job)
   if int(total) == 100:
       break
   else:
       print("Error! All 3 jobs must equal 100%")
 
number_sml_jobs =  TotNumJobs * (int(sml_job) / 100)
number_med_jobs = TotNumJobs * (int(med_job) / 100)
number_lrg_jobs = TotNumJobs * (int(lrg_job) / 100)

while time < TotNumJobs:
 
   if time % 5 == 1:
       
       cnt_job +=1 
       while True:
 
           job_type = random.randint(1, 3)
 
           if number_sml_jobs == 0 and number_med_jobs == 0 and number_lrg_jobs == 0:
               job_type = 0
               break
 
           if job_type == 1 and number_sml_jobs > 0:
               number_sml_jobs -= 1
               break
 
           if job_type == 2 and number_med_jobs > 0:
               number_med_jobs -= 1
               break
           # if the job is large
           if job_type == 3 and number_lrg_jobs > 0:
               number_lrg_jobs -= 1
               break
           
       if job_type == 1:
           job_arrv_tm = GenerateTimeUnit(time)
           GenerateSmlJob(job_arrv_tm, cnt_job)
 
       elif job_type == 2:
           job_arrv_tm = GenerateTimeUnit(time)
           GenerateMedJob(job_arrv_tm, cnt_job)
 
       elif job_type == 3:
           job_arrv_tm = GenerateTimeUnit(time)
           GenerateLrgJob(job_arrv_tm, cnt_job)
 
   time += 1

txt.close()
# =========================================================================================
#  ZAID- WILL NEED TO UPDATE THIS WITH YOUR CODE
# ASK THE USER TO ENTER THE CELLS FOR EACH MEMORY BLOCK
#
# =========================================================================================
while (True):

    memory_unit_sz = input("Please enter the size of the Memory Block that is a multiple of 8: ")
    memory_unit_sz = int(memory_unit_sz)

    if (memory_unit_sz % 8 == 0 and memory_unit_sz > 0):
        break
    elif (memory_unit_sz < 0):
        print("Please enter a positive integer")

    else:
        print("Please enter a valid number!")
        
# =========================================================================================
# ZAID- WILL NEED TO UPDATE THIS WITH YOUR CODE      
# ASK THE USER TO ENTER THE TOTAL SIZE OF MEMORY
        
# =========================================================================================
while (True):
    total_mem = input("Please enter the Total Size of the Memory: ")
    total_mem = int(total_mem)

    if (total_mem > 0):
        break

    print("Please enter a valid size! ")
# =========================================================================================
    
 # ZAID- WILL NEED TO UPDATE THIS WITH YOUR CODE     
# ASK THE USER TO ENTER IF THEY WOULD LIKE TO SIMULATE LOSTED OBJECTS
    
# =========================================================================================
while (True):
    option_lost_obj = input("Would you like to simulate losted objects ? y or n")

    if (option_lost_obj == 'y' or option_lost_obj == 'n'):
        break

    print("Please type in a valid key entry! y or n")

print('\n')
# =========================================================================================
    
 # ZAID- WILL NEED TO UPDATE THIS WITH YOUR CODE     
# ASK THE USER TO ENTER IF THEY WOULD LIKE TO SIMULATE LOSTED OBJECTS
    
# =========================================================================================

while (True):
    althm = input("CHOOSE WHICH ALGORITHM:\n 1-FIRST FIT \n 2-NEXT FIT \n 3-BEST FIT \n 4-WORSE FIT")
    althm = int(althm) 
    
    if(althm > 0 and althm < 5 ):
        break

TotalSizeMem = total_mem * memory_unit_sz
totMemAlloc = 0
PrcntMemUse = []
myMemoryUnit = Memory_Entire_Unit(memory_unit_sz, total_mem)

rand_job_input_file = open("output.txt", "r")
jobRequest = ""

while cur_time < 100:
    
    holdJob = (peek_line(rand_job_input_file))
    holdJob = holdJob.split()
    
    if not holdJob ==[]:
          
        if int(holdJob[1]) == int(cur_time):
            
            jobRequest = rand_job_input_file.readline()
            
            if not ValidateInputLine(jobRequest):
                print("Error Job has been Rejected due to job formatent!")
            else:
                JobHolder.append(ValidateInputLine(jobRequest))
            
     
   
    
    # CHECKS ALL THE JOBS IN JOB HOLDER LIST
    for cur_job in range(len(JobHolder)):
        
        # CHECK IF JOBS HAS ARRIVED TO THE MEMORY
        if cur_time == JobHolder[cur_job][1]:  
            
            # create the heap elements
            for heap in range(JobHolder[cur_job][6]):       
                
                heapRunTime = random.randint(1, JobHolder[cur_job][3])
                heapType = JobHolder[cur_job][2]
                heapSize = random.randint(20, 50)
                heapJob = JobHolder[cur_job][0]

                JobHeapList.append([heapJob, "NA", JobHolder[cur_job][2], heapRunTime, heapSize])

            #ALLOCATE CODE PORTION
            if althm == 1:    
                start_loc = FFalloc(myMemoryUnit,JobHolder[cur_job], memory_unit_sz,4)
                
            elif althm == 2: 
                start_loc = BFalloc(myMemoryUnit, JobHolder[cur_job], memory_unit_sz, 4)
                
            elif althm == 3:
                start_loc = NFalloc(myMemoryUnit, JobHolder[cur_job], memory_unit_sz, 4, start_loc)
                
            elif althm == 4:     
                start_loc = WFalloc(myMemoryUnit, JobHolder[cur_job], memory_unit_sz, 4)

            if Memory_IsFull == False:
                Allocation(myMemoryUnit, JobHolder[cur_job], start_loc, memory_unit_sz, 4)
                totMemAlloc += JobHolder[cur_job][4]
                Jobs_InProgress.append(JobHolder[cur_job])

            #ALLOCATE STACK PORTION
            if althm == 1:    
                start_loc = FFalloc(myMemoryUnit,JobHolder[cur_job], memory_unit_sz,5)
                
            elif althm == 2: 
                start_loc = BFalloc(myMemoryUnit, JobHolder[cur_job], memory_unit_sz, 5)
                
            elif althm == 3:
                start_loc = NFalloc(myMemoryUnit, JobHolder[cur_job], memory_unit_sz, 5, start_loc)
                
            elif althm == 4:     
                start_loc = WFalloc(myMemoryUnit, JobHolder[cur_job], memory_unit_sz, 5)

            if Memory_IsFull == False:
                
                Allocation(myMemoryUnit, JobHolder[cur_job], start_loc, memory_unit_sz, 5)
                Jobs_InProgress.append(JobHolder[cur_job])
                totMemAlloc += JobHolder[cur_job][5]
            

#=====================================================================================================

# ALLOCATES THE HEAP ELEMENTS INTO THE MEMORY - SMALL, MEDIUM, LARGE

#=====================================================================================================

    if Memory_IsFull == True:
        print("MEMORY IS EITHER FULL, TOO SMALL, OR CANNOT ALLOCATE ANYMORE JOBS! ")
        break
    
    if len(JobHeapList) != 0 and Memory_IsFull == False:

        if JobHeapList[0][2] == "Small":

            while heap_alloc < 50 and len(JobHeapList) != 0:

                start_loc = FFalloc(myMemoryUnit, JobHeapList[0], memory_unit_sz,4)

                if Memory_IsFull == False:

                    Allocation(myMemoryUnit, JobHeapList[0], start_loc, memory_unit_sz, 4)
                    Jobs_InProgress.append(JobHeapList[0])    
                    totMemAlloc += JobHolder[cur_job][5]
                    JobHeapList.pop(0)

                elif Memory_IsFull == True:
                    break

                heap_alloc +=1


        elif JobHeapList[0][2] == "Medium" :

            while  heap_alloc < 100 and len(JobHeapList) != 0:

                start_loc = FFalloc(myMemoryUnit, JobHeapList[0], memory_unit_sz, 4)

                if Memory_IsFull == False:

                    Allocation(myMemoryUnit, JobHeapList[0], start_loc, memory_unit_sz, 4)
                    Jobs_InProgress.append(JobHeapList[0])
                    totMemAlloc += JobHolder[cur_job][5]
                    JobHeapList.pop(0)

                elif Memory_IsFull == True:

                    break

                heap_alloc +=1

        elif JobHeapList[0][2] =="Large":

            while heap_alloc < 250 and len(JobHeapList) !=0:

                start_loc = FFalloc(myMemoryUnit, JobHeapList[0], memory_unit_sz, 4)

                if Memory_IsFull == False:

                    Allocation(myMemoryUnit, JobHeapList[0], start_loc, memory_unit_sz, 4)
                    Jobs_InProgress.append(JobHeapList[0])
                    totMemAlloc += JobHolder[cur_job][5]
                    JobHeapList.pop(0)

                elif Memory_IsFull == True:

                    break 

                heap_alloc +=1
      

    heap_alloc = 0

    print("Time: " + str(cur_time))
    #print("My Memory Contents After Allocation: ")
    #printMemory(myMemoryUnit.entireMem, myMemoryUnit, memory_unit_sz)

    #DEALLOCATES JOBS ONCE RUNTIME IS DONE==========================
    lenProgress = len(Jobs_InProgress)

    while job < lenProgress:

        if int(Jobs_InProgress[job][3]) <= 1 and Jobs_InProgress[job][0] % 100 !=0  and option_lost_obj == "y":
            DeAllocation(myMemoryUnit, total_mem, memory_unit_sz, Jobs_InProgress[job])
            lenProgress -= 1
        
            Jobs_InProgress.pop(job)
            job -= 1

        job += 1

    job = 0

    # DECREMENT THE REMAINING TIME FOR THE JOB WHEN ITS MEMORY==========================
    for cnt in range(len(Jobs_InProgress)):
        Jobs_InProgress[cnt][3] -= 1

    PrcntMemUse.append(totMemAlloc / TotalSizeMem )
    
    cur_time += 1


temp=0
for i in range(len(PrcntMemUse)):
    temp+= PrcntMemUse[i]
    
temp = temp / len(PrcntMemUse)
    


PrcntMemAlloc = (totMemAlloc / TotalSizeMem) *100
print("-------------------------------------------------------------")
print("Memory Management Metrics")    
print("-------------------------------------------------------------")
print("Number of Small Jobs: " + str(number_sml_jobs))
print("Number of Medium Jobs: "+ str(number_med_jobs))
print("Number of Large Jobs: "+ str(number_lrg_jobs))
print("\n")

print("Total Memory Defined: " + str(TotalSizeMem))
print("Amount of Memory Allocated: " + str(totMemAlloc))
print("% Memory in Use: " + str(temp))
print("% Internal Fragmentation: ")
print("% Memory Free: " )
print("% External Fragmentation: ")
print("Largest Free Space: ")
print("Smallest Free Space: ")
print("\n")

print("Numbr of Lost Objects:")
print("Total memory size of lost objects: ")
print("%Memory  of lost objects: ")
print("\n")

print("Number of Allocation: ")
print("Numbr of Allocation Operations: ")
print("Avg Numb of Alloc Operations: ")
print("Number of Free Requests: ")
print("Number of Free Operations: ")
print("Avg Numbr of alloc operations: ")
