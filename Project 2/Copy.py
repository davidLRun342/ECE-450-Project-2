import random

class Memory_Entire_Unit:
    
    
    def __init__(self, memBlock_sz, memTotal):
        
        self.memBlock_sz= memBlock_sz
        self.memTotal = memTotal
        self.entireMem =[[''] * memBlock_sz for i in range(memTotal)] 
        
 
#=============================================================================================
#  
#PART 2 B.) NEW FUNCTIONS ADDED:
#           -Allocation, DeAllocation, 
#           -First Fit Algorithm 
#           -Print contents in Memory  
          
#============================================================================================= 
        
def printMemory(size, mem, blckSize):
    
    block =0
    cell =0
    
    print("===================================================")
    for block in range(len(size)):
        
        for cell in range(blckSize):
            
            if mem.entireMem[block][cell] !='':
                
                print (mem.entireMem[block][cell][0], end =" ")
                
            elif mem.entireMem[block][cell] == '':
                print('-', end = " ")
       
        print("\n")
  

def FFalloc(allMem, Job, blckSize, segment):
    
    cnt_block =0 
    loc_start =0
  

    tempSize = round(Job[segment] / blckSize)
            
    for loc in range(len(allMem.entireMem)):
                
        if allMem.entireMem[loc][0] == '':
            cnt_block +=1
                    
        if cnt_block >= tempSize:
            loc_start = loc - tempSize + 1
            cnt_block =0
            return loc_start
            break
        
    
    return False




def Allocation(myMemory, Job, loc, blckSize, segment ):
    
    cell =0
    block =0 
    cnt_cell =0
   
    block = loc
    
#ALLOCATES THE INCOMING JOB BASED ON THE RETURN LOCATION IN MEMORY
      
    while cnt_cell < Job[segment]: 
            
        if cell >= blckSize:
            
            cell =0
            block += 1
        
        if block < len(myMemory.entireMem) and cell < blckSize:
            
            myMemory.entireMem[block][cell] = Job
            cell+=1    
        
        cnt_cell+=1 



def DeAllocation( myMemory, total_mem, blckSize, Jobs_InProgress):
   
    block =0
    cell =0  
    
    for block in range(total_mem):
       
        for cell in range(blckSize):
            
            if myMemory.entireMem[block][cell] != '':
               
                if myMemory.entireMem[block][cell][0] == Jobs_InProgress[0]:
                    
                    myMemory.entireMem[block][cell] = ''
    
#=============================================================================================
#  
#PART 2 A.) -REQUEST USER INPUT FOR MEMORY BLOCK SIZE, ENTIRE MEMORY SIZE, OPTIONS FOR HEAP MEMORY
#                      
#============================================================================================= 
                    
                
rand_job_input_file  = open("output.txt", "r")

# ASK USER TO ENTER MEMORY UNIT SIZE
#=====================================================================================
while(True):
    
    memory_unit_sz = input("Please enter the size of the Memory Block that is a multiple of 8: ")
    memory_unit_sz = int(memory_unit_sz)
    
    if(memory_unit_sz % 8 == 0 and memory_unit_sz >0):
        break
    elif (memory_unit_sz < 0):
        print("Please enter a positive integer")
        
    else:
        print("Please enter a valid number!")
# ASK THE USER TO ENTER THE TOTAL SIZE OF MEMORY
#=========================================================================================
while (True):
    total_mem = input("Please enter the Total Size of the Memory: ")
    total_mem = int(total_mem)
    
    if(total_mem > 0):
        break
    
    print("Please enter a valid size! ")
        
#ASK THE USER TO ENTER IF THEY WOULD LIKE TO SIMULATE LOSTED OBJECTS
#=========================================================================================      
while(True):
    option_lost_obj = input("Would you like to simulate losted objects ? y or n")
    
    if(option_lost_obj =='y' or option_lost_obj == 'n'):
        break
    
    print("Please type in a valid key entry! y or n")
    
print('\n')


#=============================================================================================
#                           ********NEW*************
#            PART 2 b.) -FIRST FIT, MEMORY ALLOCATION, DEALLOCATION 
#                       -INCOMING JOBS ENTERING MEMORY MANAGEMENT UNIT(RAM)                      
#=============================================================================================                

myMemoryUnit = Memory_Entire_Unit(memory_unit_sz, total_mem)

Job1 =[1, 3, "Small", 5, 25, 30, 100]
Job2 = [2, 8, "Large", 10, 90, 40, 30]
Job3 =[3, 10, "Medium", 6, 30, 30, 500]
Job4 =[4, 12, "Small", 10, 20, 20, 600]
Job5 = [5, 17,"Small", 9, 25, 25, 700]
Job6 = [6, 20,"Medium", 9, 101, 25, 700]
Job7 = [7, 25,"Large", 9, 131, 25, 700]
Job8 = [8, 31,"Large", 9, 111, 25, 700]
Job9 = [9, 45,"Large", 9, 141, 25, 700]
Job10 = [10, 51,"Small", 9, 16, 25, 700]

JobHolder = [Job1 ]

'''Job2, Job3, Job4, Job5, Job6, Job7, Job8, Job9, Job10] '''

'''[ Job2, Job3, Job4, Job5]'''

Jobs_InProgress =[]
JobHeapList=[]

cur_time = 0
start_loc =0
job =0

lenProgress = 0
lenJobElement =0 

heapRunTime =0
heapSize = 0
heapJob =0
heapType =0 

heap_alloc =0 

while cur_time < 20: 
    
#CHECKS ALL THE JOBS IN JOB HOLDER LIST============================================
    for cur_job in range(len(JobHolder)):
   
        # CHECK IF JOBS HAS ARRIVED TO THE MEMORY
        if cur_time == JobHolder[cur_job][1]:
            
          #create the heap elements
          for heap in range(JobHolder[cur_job][6]):
              heapRunTime = random.randint(1,JobHolder[cur_job][3])
              heapType= JobHolder[cur_job][2]
              heapSize = random.randint(20,50)
              heapJob = str(JobHolder[cur_job][0]) +' '+ str(heap + 1) + ' HE'
              
              JobHeapList.append([heapJob, "NA", JobHolder[cur_job][2], heapRunTime, heapSize ]) 
              
          #allocate Code portion
         
              
          start_loc = FFalloc(myMemoryUnit,JobHolder[cur_job], memory_unit_sz,4)
          print(start_loc)
          
         
             
          Allocation(myMemoryUnit, JobHolder[cur_job], start_loc, memory_unit_sz,4)
          Jobs_InProgress.append(JobHolder[cur_job])
              
         
          
          # allocate Stack portion
          start_loc = FFalloc(myMemoryUnit,JobHolder[cur_job],  memory_unit_sz,5) 
          
          if start_loc != False:
              Allocation(myMemoryUnit, JobHolder[cur_job], start_loc, memory_unit_sz, 5)
          
    '''    
    for heap in range(len(JobHeapList)):
        print(JobHeapList[heap])
    '''    
# ALLOCATES THE HEAP ELEMENTS INTO THE MEMORY 
  

    if len(JobHeapList) != 0:
        
        if JobHeapList[0][2] == "Small":
            
            while heap_alloc < 50 and len(JobHeapList) != 0:
                
                start_loc = FFalloc(myMemoryUnit, JobHeapList[0], memory_unit_sz,4)
                
                if start_loc != False:
                    Allocation(myMemoryUnit, JobHeapList[0], start_loc, memory_unit_sz, 4)
                    Jobs_InProgress.append(JobHeapList[0])                
                    JobHeapList.pop(0)
                    
                elif start_loc == False: 
                    break
                
                heap_alloc +=1
            
        elif JobHeapList[0][2] == "Medium" :
            
            while  heap_alloc < 100:
                print("THIS ELEMENT BELONGS TO MEDIUM JOB")
                heap_alloc +=1
            
        elif JobHeapList[0][2] =="Large":
            
            while heap_alloc < 250:
                print("THIS ELEMENT BELONGS TO LARGE JOB")
                heap_alloc +=1
       
      
    heap_alloc = 0
    print("Time: " + str(cur_time))
    print("My Memory Contents After Allocation: ")
    printMemory(myMemoryUnit.entireMem, myMemoryUnit, memory_unit_sz)
    
#DEALLOCATES JOBS ONCE RUNTIME IS DONE==========================    
    lenProgress = len(Jobs_InProgress) 
        
    while job < lenProgress:
    
        if int(Jobs_InProgress[job][3]) <= 1:
            
            DeAllocation(myMemoryUnit, total_mem, memory_unit_sz, Jobs_InProgress[job])
            lenProgress -=1
            Jobs_InProgress.pop(job)
            job-=1
       
        job+=1
        
    job = 0    
    
#DECREMENT THE REMAINING TIME FOR THE JOB WHEN ITS MEMORY========================== 
    for cnt in range(len(Jobs_InProgress)):
        
        Jobs_InProgress[cnt][3] -=1 
    
    
#CHECK IF MEMORY IS FULL - BREAKS OUT LOOP IF FULL=================================
    
    #print("Time: " + str(cur_time))
    #print("My Memory Contents: ")
    #printMemory(myMemoryUnit.entireMem, myMemoryUnit, memory_unit_sz)  
    print("\n")
    
    cur_time+=1
    