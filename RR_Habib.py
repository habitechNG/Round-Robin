import statistics
class RoundRobin:

    def __init__(self, processes):
        self.processes = processes
        self.execution_details = []
        self.mean_time_slice = self.calculate_mean_burst_time()
        self.median_time_slice = self.calculate_median_burst_time()
        self.mode_time_slice = self.calculate_mode_burst_time()
        self.harm_time_slice = self.calculate_harmonic_mean_burst_time()
        self.geom_time_slice = self.calculate_geometric_mean_burst_time()

    def calculate_mean_burst_time(self):
        total_burst_time = sum(process[1] for process in self.processes)
        return total_burst_time / len(self.processes)

    def calculate_median_burst_time(self):
        burst_times = [process[1] for process in self.processes]
        return statistics.median(burst_times)

    def calculate_mode_burst_time(self):
        burst_times = [process[1] for process in self.processes]
        return statistics.mode(burst_times)
    
    def calculate_harmonic_mean_burst_time(self):
        burst_times = [process[1] for process in self.processes]
        return statistics.harmonic_mean(burst_times)

    def calculate_geometric_mean_burst_time(self):
        burst_times = [process[1] for process in self.processes]
        return statistics.geometric_mean(burst_times)

    def run_round_robin(self, time_slice):
        n = len(self.processes)
        remaining_burst_time = [process[1] for process in self.processes]
        completion_time = [0] * n
        turn_around_time = [0] * n
        waiting_time = [0] * n
        executed_processes = []
        context_switch_count = 0

        time = 0
        while any(remaining_burst_time):
            for i in range(n):
                if remaining_burst_time[i] > 0:
                    executed_processes.append(i + 1)
                    start_time = time
                    if remaining_burst_time[i] > time_slice:
                        time += time_slice
                        remaining_burst_time[i] -= time_slice
                        context_switch_count += 1
                    else:
                        time += remaining_burst_time[i]
                        completion_time[i] = time
                        remaining_burst_time[i] = 0
                        
##                    end_time = time
##                    self.execution_details.append({
##                        'process_id': i + 1,
##                        'start_time': start_time,
##                        'end_time': end_time
##                                })
                    

        for i in range(n):
            turn_around_time[i] = completion_time[i]
            waiting_time[i] = turn_around_time[i] - self.processes[i][1]

        avg_turnaround_time = sum(turn_around_time) / n
        avg_waiting_time = sum(waiting_time) / n
        throughput = n / time

        self.print_results(executed_processes, turn_around_time, waiting_time, context_switch_count, avg_turnaround_time, avg_waiting_time, throughput)

    def print_results(self, executed_processes, turn_around_time, waiting_time, context_switch_count, avg_turnaround_time, avg_waiting_time, throughput):
        print("Processes:", self.processes)
        print("Process Execution Order:", executed_processes)
        print("Process Turnaround Times:", turn_around_time)
        print("Process Waiting Times:", waiting_time)
        print("Total Context Switch Count:", context_switch_count)
        print("Average Turnaround Time:", avg_turnaround_time)
        print("Average Waiting Time:", avg_waiting_time)
        print("Throughput:", throughput)
##        print("Process ID\tStart Time\tEnd Time")
        for details in self.execution_details:
            print(f"{details['process_id']}\t\t{details['start_time']}\t\t{details['end_time']}")


if __name__ == "__main__":
    processes = [
        #[process_id, burst_time]
        [1, 10],
        [2, 6],
        [3, 8],
        [4, 4],
        [5,15],
        [6,10]
    ]

    rr_scheduler = RoundRobin(processes)
    
    print("Traditional Round Robin:")
    time_slice=3
    rr_scheduler.run_round_robin(time_slice)
    print("Time Quantum = ", time_slice)
    
    print("\nRound Robin with Mean Burst Time:")
    rr_scheduler.run_round_robin(time_slice=rr_scheduler.mean_time_slice)
    print("Mean Quantum Time:", rr_scheduler.mean_time_slice)
    
    print("\nRound Robin with Median Burst Time:")
    rr_scheduler.run_round_robin(time_slice=rr_scheduler.median_time_slice)
    print("Median Quantum Time:", rr_scheduler.median_time_slice)
    
    print("\nRound Robin with Mode Burst Time:")
    rr_scheduler.run_round_robin(time_slice=rr_scheduler.mode_time_slice)
    print("Mode Quantum Time:", rr_scheduler.mode_time_slice)
    
    print("\nRound Robin with Harmonic Mean Burst Time:")
    rr_scheduler.run_round_robin(time_slice=rr_scheduler.harm_time_slice)
    print("Harmonic Mean Quantum Time:", rr_scheduler.harm_time_slice)
    
    print("\nRound Robin with Geometric Mean Burst Time:")
    rr_scheduler.run_round_robin(time_slice=rr_scheduler.geom_time_slice)
    print("Geometric Mean Quantum Time:", rr_scheduler.geom_time_slice)
