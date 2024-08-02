#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Process:
    def __init__(self, pid, arrival_time, burst_time, priority): 
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority= priority
        self.waiting_time = 0
        self.turnaround_time = 0


# In[5]:


def preemptive_priority_scheduling(processes):
    time = 0
    completed_processes = 0
    n = len(processes)
    execution_order = []
    processes.sort(key=lambda x: (x.arrival_time, x.priority))

    while completed_processes < n:
        available_processes = [p for p in processes if p.arrival_time <= time and p.remaining_time > 0]
        
        if available_processes:
            current_process = min(available_processes, key=lambda x: x.priority)
            execution_order.append(current_process.pid)
            time += 1
            current_process.remaining_time -= 1
            
            if current_process.remaining_time == 0:
                current_process.turnaround_time = time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes += 1
        else:
            time += 1

    return processes, execution_order

    


# In[6]:


def calculate_average_times(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    n = len(processes)
    for process in processes:
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time
        
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    
    return avg_waiting_time, avg_turnaround_time


# In[9]:


def main():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        priority = int(input(f"Enter Priority for process {pid} (lower value means higher priority): "))
        processes.append(Process(pid, arrival_time, burst_time, priority))
    
    scheduled_processes, execution_order = preemptive_priority_scheduling(processes)
    avg_waiting_time, avg_turnaround_time = calculate_average_times(scheduled_processes) 
    
    print("\nProcess ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in scheduled_processes:
        print(f"{process.pid}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
              
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"\nExecution order: {execution_order}")

if __name__ == "__main__":
    main()


# In[ ]:




