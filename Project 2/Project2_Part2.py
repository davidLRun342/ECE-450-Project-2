import random
import math
import csv 

csvFile = open("outputCSV.csv","w")
txt = open("output.txt","w+")
txtLog = open("Log.txt", "w+")
txtSumm = open("Summary_Output.txt", "w+")

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


def FindLrgFreeSpace(allMem):

    loc =0 
    size =0 
    
    temp_loc =0
    global Memory_IsFull
    
    WorseFit = [loc, size]

    cnt_block =0

    temp_loc =0
    found = False

    while loc < len(allMem.entireMem):

        
        if allMem.entireMem[loc][0] =='':
            temp_loc  =loc
        
            while allMem.entireMem[temp_loc][0] == '' and  temp_loc != len(allMem.entireMem)-1 :
      
                cnt_block +=1 
                temp_loc +=1
                
            if cnt_block > WorseFit[1] :
                
                found = True
                WorseFit[0] = loc
                WorseFit[1] = cnt_block
                              
            cnt_block =0
            loc  = temp_loc
        
        loc+=1 
    
    if found  == False: 
        Memory_IsFull = True
           
    return WorseFit[1]


def FindSmallFreeSpace(allMem):

    loc =0 
    size =1000000 
    
    temp_loc =0
    global Memory_IsFull
    
    WorseFit = [loc, size]

    cnt_block =0

    temp_loc =0
    found = False
    
    while loc < len(allMem.entireMem):

        
        if allMem.entireMem[loc][0] =='':
            temp_loc  =loc
        
            while allMem.entireMem[temp_loc][0] == '' and  temp_loc != len(allMem.entireMem)-1 :
      
                cnt_block +=1 
                temp_loc +=1
                
            if cnt_block < WorseFit[1] :
                
                found = True
                WorseFit[0] = loc
                WorseFit[1] = cnt_block
                              
            cnt_block =0
            loc  = temp_loc
        
        loc+=1 
    
    if found  == False: 
        Memory_IsFull = True
           
    return WorseFit[1]

def printMetrics(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
    txtSumm.write("----------------------------------------------------------")
    txtSumm.write("\n% Memory in Use: " + str(a))
    txtSumm.write("\n% Memory Free: " + str (round(b, 2)))
    txtSumm.write("\n% Internal Fragmentation: " + str(c))
    txtSumm.write("\n% External Fragmentation: " + str(d))
    txtSumm.write("\nLargest Free Space: " + str(e))
    txtSumm.write("\nSmallest Free Space: " + str(f))
    txtSumm.write("\nNumbr of Lost Objects:" + str(g))
    txtSumm.write("\nTotal memory size of lost objects: " + str(h))
    txtSumm.write("\n% Memory of lost objects: " + str(i))
    txtSumm.write("\nNumber of Allocation: " + str(j))
    txtSumm.write("\nNumbr of Operations: " +str(k))
    txtSumm.write("\nAvg Numb of Alloc Operations: " + str(l ))
    txtSumm.write("\nNumber of Free Requests: " +str(m))
    txtSumm.write("\nNumber of Free Operations: " + str(n))
    txtSumm.write("\nFour Additional Memory Metrics: ")
    txtSumm.write("\n------------------------------------------------------")
    txtSumm.write("\nAverage Number of Heap Elements Leaving: " + str(o))
    txtSumm.write("\nAvg % of Heap Elements in Memory: " + str(p))
    txtSumm.write("\n% of Time Memory is Below 50 % Usage: "+ str(q) )
    txtSumm.write("\n% of Time Memory is Above 50% Usage: " + str(r))
    txtSumm.write("\n\n")
    
    print("% Memory in Use: " + str(a))
    print("% Memory Free: " + str (round(b, 2)))
    print("% Internal Fragmentation: " + str(c))
    print("% External Fragmentation: " + str(d))
    print("Largest Free Space: " + str(e))
    print("Smallest Free Space: " + str(f))
    print("Numbr of Lost Objects:" + str(g))
    print("Total memory size of lost objects: " + str(h))
    print("% Memory of lost objects: " + str(i))
    print("Number of Allocation: " + str(j))
    print("Numbr of Operations: " +str(k))
    print("Avg Numb of Alloc Operations: " + str(l ))
    print("Number of Free Requests: " +str(m))
    print("Number of Free Operations: " + str(n))
    print("Four Additional Memory Metrics: ")
    print("------------------------------------------------------")
    print("Average Number of Heap Elements Leaving: " + str(o))
    print("Avg % of Heap Elements in Memory: " + str(p))
    print("% of Time Memory is Below 50 % Usage: "+ str(q) )
    print("% of Time Memory is Above 50% Usage: " + str(r))
    print("\n")
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

TotNumJobs = 2400 

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

temp_sml_jobs =number_sml_jobs
temp_med_jobs =number_med_jobs
temp_lrg_jobs =number_lrg_jobs

txtSumm.write("\n-------------------------------------------------------------")
txtSumm.write("\nMemory Management Metrics")    
txtSumm.write("\n-------------------------------------------------------------")
txtSumm.write("\nNumber of Small Jobs: " + str(temp_sml_jobs)+ " " +str(sml_job) + "%")
txtSumm.write("\nNumber of Medium Jobs: "+ str(temp_med_jobs) + " " +str(sml_job) + "%")
txtSumm.write("\nNumber of Large Jobs: "+ str(temp_lrg_jobs) + " " +str(sml_job) + "%")
txtSumm.write("\n")

while time < 12000:
 
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


#=========================================================================================
#               METRIC VARIABLES 
#=========================================================================================
althm =1 
AllAlgthm =[]
timeRunningFor = 50
TotalSizeMem = total_mem * memory_unit_sz
totMemAlloc = 0
memAlloc =0
PrcntMemUse = 0
FreeMem = 0 
Prcnt_FreeMem = 0

Num_LostObj =0
Tot_MemLostObj =0
Percnt_LostObj =0

Num_Alloc=0
Num_AllocOp =0
tempOp =0
Tot_AllocOp =0
Avg_AllocOp=0

IntrnalFrag = 0
PercntIntrnalFrag = 0

ExtrnalFrag =0
PercntExtFrag =0

NumFreeReq =0
NumFreeOp =0

HeapEleLeaving=0
HeapLeavAll =0

cntHeapMem=0
HeapMemAll =0

cntLess20Mem= 0
isLess20Mem= 0
Less20MemAll =0

cntGreater70=0
isGreater70Mem= 0
Greater70MemAll =0

lrgFree = 0
smllFree =0

Avg_PrcntMemUse =0
Avg_PrcntFreeMem =0
Avg_PrcntIntFrag =0 
Avg_PrcntExtFrag =0 
Avg_HeapLeaving =0
Avg_HeapMemUsage =0
Prcnt_20=0
Prcnt_70 =0

txtSumm.write("\nTotal Memory Defined: " + str(TotalSizeMem))
txtSumm.write("\nAmount of Memory Allocated: " + str(memAlloc) + "\n")

Percnt_LostObj =  (Tot_MemLostObj / TotalSizeMem) * 100
#=========================================================================================
temp1 =0
myMemoryUnit = Memory_Entire_Unit(memory_unit_sz, total_mem)

rand_job_input_file = open("output.txt", "r")
jobRequest = ""

while althm < 5:
    
    
    if althm == 1:
        txtSumm.write("\n====================================================" )
        txtSumm.write("\nFIRST FIT:" )
        txtSumm.write("\n====================================================" )
        txtLog.write("\n====================================================" )
        txtLog.write("\nFIRST FIT:" )
        txtLog.write("\n====================================================" )
    elif althm == 2:
        txtSumm.write("\n====================================================" )
        txtSumm.write("\nBEST FIT:" )
        txtSumm.write("\n====================================================" )
        txtLog.write("\n====================================================" )
        txtLog.write("\nBEST FIT:" )
        txtLog.write("\n====================================================" )
    elif althm == 3:
        txtSumm.write("\n====================================================" )
        txtSumm.write("\nNEXT FIT:" )
        txtSumm.write("\n====================================================" )
        txtLog.write("\n====================================================" )
        txtLog.write("\nNEXT FIT:" )
        txtLog.write("\n====================================================" )
    elif althm ==4 :
        txtSumm.write("\n====================================================" )
        txtSumm.write("\nWORSE FIT:" )
        txtSumm.write("\n====================================================" )
        txtLog.write("\n====================================================" )
        txtLog.write("\nWORSE FIT:" )
        txtLog.write("\n====================================================" )
    
    while cur_time < timeRunningFor:
        
        txtSumm.write("\n\nTime: " + str(cur_time))
        txtLog.write("\n\nTime: " + str(cur_time))
        print("Time: " + str(cur_time))
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
                txtSumm.write("\n\tJOB " + str(JobHolder[cur_job][0]) + " ARRIVES")
                # create the heap elements
                
                for heap in range(JobHolder[cur_job][6]):       
                    
                    heapRunTime = random.randint(1, JobHolder[cur_job][3])
                    heapType = JobHolder[cur_job][2]
                    heapSize = random.randint(20, 50)
                    heapJob = JobHolder[cur_job][0]
    
                    JobHeapList.append([heapJob, heap + 1 , JobHolder[cur_job][2], heapRunTime, heapSize, "NA"])
    
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
                    Num_Alloc +=1
                    Num_AllocOp +=1
                    totMemAlloc += JobHolder[cur_job][4]
                    memAlloc +=JobHolder[cur_job][4]
                    txtLog.write("\n\tJOB " + str(JobHolder[cur_job][0]) + " HAS BEEN ALLOCATED")
                    txtLog.write("\n\tLOCATION: " + str(start_loc))
                   
                    if JobHolder[cur_job][4] % memory_unit_sz !=0:
                        temp1 = abs( math.ceil(JobHolder[cur_job][4] / memory_unit_sz) - JobHolder[cur_job][4])
                        
                        IntrnalFrag += temp1 
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
                    Num_Alloc +=1 
                    Num_AllocOp +=1
                    Jobs_InProgress.append(JobHolder[cur_job])
                    memAlloc +=JobHolder[cur_job][5]
                    totMemAlloc += JobHolder[cur_job][5]
                    
                    if JobHolder[cur_job][4] % memory_unit_sz !=0:
                        temp1 = abs(math.ceil(JobHolder[cur_job][4] / memory_unit_sz) - JobHolder[cur_job][4])
                            
                        IntrnalFrag += temp1
    
    #=====================================================================================================
    
    # ALLOCATES THE HEAP ELEMENTS INTO THE MEMORY - SMALL, MEDIUM, LARGE
    
    #=====================================================================================================
    
        if Memory_IsFull == True:
            txtLog.write("\n\tMEMORY IS EITHER FULL, TOO SMALL, OR CANNOT ALLOCATE ANYMORE JOBS! ")
            txtSumm.write("\n\tMEMORY IS EITHER FULL, TOO SMALL, OR CANNOT ALLOCATE ANYMORE JOBS! ")
            break
        
        if len(JobHeapList) != 0 and Memory_IsFull == False:
    
            if JobHeapList[0][2] == "Small":
    
                while heap_alloc < 50 and len(JobHeapList) != 0:
    
                    start_loc = FFalloc(myMemoryUnit, JobHeapList[0], memory_unit_sz,4)
    
                    if Memory_IsFull == False:
    
                        Allocation(myMemoryUnit, JobHeapList[0], start_loc, memory_unit_sz, 4)
                        txtLog.write("\n\tJOB " + str(JobHeapList[0][0]) + " HEAP ELEMENT " + str(JobHeapList[0][1]) + " HAS ALLOCATED")
                        Jobs_InProgress.append(JobHeapList[0])
                        Num_Alloc +=1
                        Num_AllocOp +=1
                        memAlloc +=JobHeapList[0][4]
                        totMemAlloc += JobHeapList[0][4]
                        cntHeapMem += JobHeapList[0][4]
                        if JobHeapList[0][4] % memory_unit_sz !=0:
                            temp1 = abs(math.ceil(JobHeapList[0][4] / memory_unit_sz) - JobHeapList[0][4])
                                
                            IntrnalFrag += temp1
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
                        Num_Alloc +=1
                        Num_AllocOp +=1
                        memAlloc +=JobHeapList[0][4]
                        totMemAlloc += JobHeapList[0][4]
                        cntHeapMem += JobHeapList[0][4]
                        txtLog.write("\n\tJOB " + str(JobHeapList[0][0]) + " HEAP ELEMENT " + str(JobHeapList[0][1]) + " HAS ALLOCATED")
                        
                        if JobHolder[cur_job][4] % memory_unit_sz !=0:
                            temp1 = abs(math.ceil(JobHeapList[0][4] / memory_unit_sz) - JobHeapList[0][4])
                            IntrnalFrag += temp1
                            
                        JobHeapList.pop(0)
    
                    elif Memory_IsFull == True:
    
                        break
    
                    heap_alloc +=1
    
            elif JobHeapList[0][2] =="Large":
    
                while heap_alloc < 250 and len(JobHeapList) !=0:
    
                    start_loc = FFalloc(myMemoryUnit, JobHeapList[0], memory_unit_sz, 4)
    
                    if Memory_IsFull == False:
    
                        Allocation(myMemoryUnit, JobHeapList[0], start_loc, memory_unit_sz, 4)
                        txtLog.write("\n\tJOB " + str(JobHeapList[cur_job][0]) + " HEAP ELEMENT " + str(JobHeapList[cur_job][1]) + " HAS ALLOCATED")
                        Jobs_InProgress.append(JobHeapList[0])
                        Num_Alloc +=1
                        Num_AllocOp +=1
                        memAlloc +=JobHeapList[0][4]
                        totMemAlloc += JobHeapList[0][4]
                        cntHeapMem -= Jobs_InProgress[job][4]
                        
                        if JobHolder[cur_job][4] % memory_unit_sz !=0:
                            temp1 = abs(math.ceil(JobHolder[cur_job][4] / memory_unit_sz) - JobHolder[cur_job][4])
                                
                            IntrnalFrag += temp1
                        JobHeapList.pop(0)
    
                    elif Memory_IsFull == True:
    
                        break 
    
                    heap_alloc +=1
          
    
        heap_alloc = 0
    
        
        #DEALLOCATES JOBS ONCE RUNTIME IS DONE==========================
        lenProgress = len(Jobs_InProgress)
    
        while job < lenProgress:
    
            if int(Jobs_InProgress[job][3]) <= 1:
                NumFreeReq +=1
                txtSumm.write("\n\tJOB " + str(Jobs_InProgress[job][0]) + " DEPARTS")
                
                if option_lost_obj == "y":
                    
                    if Jobs_InProgress[job][0] % 100 !=0:
                    
                        DeAllocation(myMemoryUnit, total_mem, memory_unit_sz, Jobs_InProgress[job])
                        Num_AllocOp +=1
                        lenProgress -= 1
                        
                        
                        if Jobs_InProgress[job][5] =="NA":
                            txtLog.write("\n\tJOB " + str(Jobs_InProgress[cur_job][0]) + " HEAP ELEMENT " + str(Jobs_InProgress[cur_job][1]) + " HAS DEALLOCATED")
                            NumFreeOp +=1 
                            totMemAlloc -= Jobs_InProgress[job][4]
                            cntHeapMem -= Jobs_InProgress[job][4]
                            HeapEleLeaving+=1
                            
    
                        else:
                            txtLog.write("\n\tJOB " + str(Jobs_InProgress[cur_job][0]) + " HAS DEALLOCATED")
                            NumFreeOp +=2
                            totMemAlloc -=Jobs_InProgress[job][5]
                            totMemAlloc -= Jobs_InProgress[job][4]
                            
                    
                        Jobs_InProgress.pop(job)
                        job -= 1
                        
                    elif Jobs_InProgress[job][0] % 100 ==0 and len(Jobs_InProgress[job])==7:
                        Num_LostObj +=1
                        Tot_MemLostObj += Jobs_InProgress[job][4] + Jobs_InProgress[job][5] 
                        
                elif option_lost_obj == "n":
                    DeAllocation(myMemoryUnit, total_mem, memory_unit_sz, Jobs_InProgress[job])
                    Num_AllocOp +=1
                    lenProgress -= 1
                        
                    if Jobs_InProgress[job][5] =="NA":
                        txtLog.write("\n\tJOB " + str(Jobs_InProgress[cur_job][0]) + " HEAP ELEMENT " + str(Jobs_InProgress[cur_job][1]) + " HAS DEALLOCATED")
                        NumFreeOp +=1 
                        totMemAlloc -= Jobs_InProgress[job][4]
                        HeapEleLeaving+=1
                        cntHeapMem -= JobHeapList[job][4]
                            
                    else: 
                        NumFreeOp +=2
                        txtLog.write("\n\tJOB " + str(Jobs_InProgress[cur_job][0]) + " HAS DEALLOCATED")
                        totMemAlloc -= Jobs_InProgress[job][4]
                        totMemAlloc -= Jobs_InProgress[job][5]
                        
                    Jobs_InProgress.pop(job)
                    job -= 1
                    
            job += 1
    
        job = 0
        # DECREMENT THE REMAINING TIME FOR THE JOB WHEN ITS MEMORY==========================
        for cnt in range(len(Jobs_InProgress)):
            Jobs_InProgress[cnt][3] -= 1
    #========================================================================================  
            
        # METRIC CALCULATIONS
        
    #========================================================================================
        
        if totMemAlloc > TotalSizeMem:
            totMemAlloc = TotalSizeMem
            
        if totMemAlloc < 0:
            totMemAlloc = 0
        
        FreeMem = TotalSizeMem - totMemAlloc
        Prcnt_FreeMem = round((FreeMem / TotalSizeMem) * 100, 2)
        
        PrcntMemUse = round((totMemAlloc / TotalSizeMem ) * 100, 2)
        
        for i in range(len(myMemoryUnit.entireMem)):
            if myMemoryUnit.entireMem[i][0]=='':
                ExtrnalFrag +=1
            
            if myMemoryUnit.entireMem[i][0] !='':
                cntLess20Mem +=1
                cntGreater70 +=1
         
        if (cntLess20Mem / total_mem ) * 100 < 50 :
            isLess20Mem = "yes"
            
        if (cntGreater70 / total_mem ) * 100 > 50 :
            isGreater70Mem  = "yes"
        
    
        PercntExtFrag = round((ExtrnalFrag / TotalSizeMem) * 100, 2)
        PercntIntrnalFrag = round((IntrnalFrag / TotalSizeMem ) * 100, 2 )
    
        
        Percnt_LostObj = round( (Tot_MemLostObj / TotalSizeMem) * 100, 2)
        lrgFree= FindLrgFreeSpace(myMemoryUnit)
        smllFree= FindSmallFreeSpace(myMemoryUnit)
        
        if cur_time ==0:
            
            Avg_AllocOp = Num_Alloc / 1
        else:
            Avg_AllocOp = Num_Alloc / cur_time
        
        HeapMemAll = round ((abs(cntHeapMem / TotalSizeMem)) * 100 ,2 )
        
    
        if cur_time % 20 == 0: #and cur_time >=2000:
            txtSumm.write("\n\n")
            txtSumm.write("\n% Memory in Use: " + str(PrcntMemUse))
            txtSumm.write("\n% Memory Free: " + str (round(Prcnt_FreeMem, 2)))
            txtSumm.write("\n% Internal Fragmentation: " + str(PercntIntrnalFrag))
            txtSumm.write("\n% External Fragmentation: " + str(PercntExtFrag))
            txtSumm.write("\nLargest Free Space: " + str(lrgFree))
            txtSumm.write("\nSmallest Free Space: " + str(smllFree))
            txtSumm.write("\nNumbr of Lost Objects:" + str(Num_LostObj))
            txtSumm.write("\nTotal memory size of lost objects: " + str(Tot_MemLostObj))
            txtSumm.write("\n% Memory of lost objects: " + str(Percnt_LostObj))
            txtSumm.write("\nNumber of Allocation: " + str(Num_Alloc))
            txtSumm.write("\nNumbr of Operations: " +str(Num_AllocOp))
            txtSumm.write("\nAvg Numb of Alloc Operations: " + str(Avg_AllocOp ))
            txtSumm.write("\nNumber of Free Requests: " +str(NumFreeOp))
            txtSumm.write("\nNumber of Free Operations: " + str(NumFreeReq))
            txtSumm.write("\nFour Additional Memory Metrics: ")
            txtSumm.write("\n------------------------------------------------------")
            txtSumm.write("\nAverage Number of Heap Elements Leaving: " + str(HeapEleLeaving))
            txtSumm.write("\nAvg % of Heap Elements in Memory: " + str(HeapMemAll))
            txtSumm.write("\n% of Time Memory is Below 50 % Usage: "+ str(isLess20Mem) )
            txtSumm.write("\n% of Time Memory is Above 50% Usage: " + str(isGreater70Mem ))
            txtSumm.write("\n")
        
        if cur_time >= timeRunningFor -2:
            AllAlgthm.append([PrcntMemUse, Prcnt_FreeMem, PercntIntrnalFrag, PercntExtFrag, lrgFree, smllFree, Num_LostObj,Tot_MemLostObj, Percnt_LostObj,Num_Alloc, Num_AllocOp, Avg_AllocOp, NumFreeOp,NumFreeReq, HeapEleLeaving, HeapMemAll, isLess20Mem,isGreater70Mem])
            
        ExtrnalFrag =0    
        IntrnalFrag=0
        cntGreater70 =0
        cntLess20Mem =0    
        cntHeapMem =0 
        isLess20Mem = "no"
        isGreater70Mem  = "no"
        
        cur_time += 1
    
    cur_time =0
    JobHolder =[] 
    JobHeapList =[]
    Jobs_InProgress =[]
    
    althm +=1


txtSumm.write("\nFINAL SUMMARY" )
for i in range(len(AllAlgthm)):
    
    if i == 0:
        txtSumm.write("\n\nAlgorithm: First Fit" )
        print("\nAlgorithm: First Fit" )
    elif i == 1:
        txtSumm.write("\n\nAlgorithm: Next Fit" )
        print("\nAlgorithm: First Fit" )
    elif i == 2:
        txtSumm.write("\n\nAlgorithm: Best Fit" )
        print("\nAlgorithm: First Fit" )
    elif i ==3:
        txtSumm.write("\n\nAlgorithm: Worse Fit" )
        print("\nAlgorithm: First Fit" )
    
    printMetrics(AllAlgthm[i][0],AllAlgthm[i][1], AllAlgthm[i][2], AllAlgthm[i][3], AllAlgthm[i][4], AllAlgthm[i][5], AllAlgthm[i][6], AllAlgthm[i][7], AllAlgthm[i][8], AllAlgthm[i][9], AllAlgthm[i][10],AllAlgthm[i][11], AllAlgthm[i][12], AllAlgthm[i][13], AllAlgthm[i][14], AllAlgthm[i][15], AllAlgthm[i][16], AllAlgthm[i][17])
    




