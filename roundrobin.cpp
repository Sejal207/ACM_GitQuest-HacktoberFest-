#include <iostream>
#include <queue>
using namespace std;

struct Process {
    int id;
    int burstTime;
    int remainingTime;
    int arrivalTime;
    int completionTime;
    int responseTime;
    bool isFirstExecution;
};

int main() {
    int n, quantum;
    cout << "Enter the number of processes: ";
    cin >> n;

    Process processes[100]; // Assuming a maximum of 100 processes
    queue<int> q;
    int waitingTime[100], turnaroundTime[100];
    bool inQueue[100] = {false};  // Track whether a process is already in the queue
    int ganttChart[200]; // Assuming a maximum of 200 entries in the Gantt chart
    int ganttIndex = 0;  // Index for the Gantt chart

    // Input process burst time and arrival time
    for (int i = 0; i < n; i++) {
        processes[i].id = i + 1;
        cout << "Enter arrival time and burst time for process " << i + 1 << ": ";
        cin >> processes[i].arrivalTime >> processes[i].burstTime;
        processes[i].remainingTime = processes[i].burstTime;
        processes[i].completionTime = 0;
        processes[i].responseTime = -1;
        processes[i].isFirstExecution = false;
        waitingTime[i] = 0;
        turnaroundTime[i] = 0;
    }

    cout << "Enter time quantum: ";
    cin >> quantum;

    int time = 0;
    int completed = 0;

    // Add the processes that have arrived at time 0 to the queue
    for (int i = 0; i < n; i++) {
        if (processes[i].arrivalTime <= time && !inQueue[i]) {
            q.push(i);
            inQueue[i] = true;
        }
    }

    // Round Robin scheduling
    while (completed < n) {
        // Display the ready queue sequence
        cout << "\nTime " << time << " -> Ready Queue: ";
        queue<int> tempQueue = q;
        while (!tempQueue.empty()) {
            int proc = tempQueue.front();
            tempQueue.pop();
            cout << "P" << processes[proc].id << " ";
        }
        cout << "\n";

        if (!q.empty()) {
            int i = q.front();
            q.pop();

            // Record the process in the Gantt chart
            ganttChart[ganttIndex++] = processes[i].id;

            // Set response time if this is the first execution of the process
            if (!processes[i].isFirstExecution) {
                processes[i].responseTime = time - processes[i].arrivalTime;
                processes[i].isFirstExecution = true;
            }

            if (processes[i].remainingTime > quantum) {
                time += quantum;
                processes[i].remainingTime -= quantum;
            } else {
                time += processes[i].remainingTime;
                processes[i].remainingTime = 0;
                completed++;

                // Calculate completion, turnaround, and waiting times
                processes[i].completionTime = time;
                turnaroundTime[i] = processes[i].completionTime - processes[i].arrivalTime;
                waitingTime[i] = turnaroundTime[i] - processes[i].burstTime;
            }

            // Add new processes that have arrived by the current time
            for (int j = 0; j < n; j++) {
                if (processes[j].arrivalTime <= time && processes[j].remainingTime > 0 && !inQueue[j]) {
                    q.push(j);
                    inQueue[j] = true;
                }
            }

            // If the process is not yet completed, put it back in the queue
            if (processes[i].remainingTime > 0) {
                q.push(i);
            }
        } else {
            // If no process in the queue, increase the time
            time++;
        }
    }

    // Display Gantt Chart with Time Labels Below
    cout << "\nGantt Chart:\n";
    for (int i = 0; i < ganttIndex; i++) {
        cout << "|  P" << ganttChart[i] << "  ";
    }
    cout << "|\n";

    // Display the time below the Gantt chart
    cout << "0";
    for (int i = 0; i < ganttIndex; i++) {
        cout << "      " << (i + 1) * quantum; // Simple increment based on quantum
    }
    cout << "\n";

    // Calculate total waiting time and turnaround time
    double totalWT = 0, totalTAT = 0;
    cout << "\nPid\tAT\tBT\tCT\tTAT\tWT\tRT\n";
    for (int i = 0; i < n; i++) {
        totalWT += waitingTime[i];
        totalTAT += turnaroundTime[i];
        cout << "P" << processes[i].id << "\t" 
             << processes[i].arrivalTime << "\t" 
             << processes[i].burstTime << "\t" 
             << processes[i].completionTime << "\t" 
             << turnaroundTime[i] << "\t" 
             << waitingTime[i] << "\t" 
             << processes[i].responseTime << "\n";
    }

    // Calculate and display average waiting time and turnaround time
    cout << "\nAverage Waiting Time: " << totalWT / n << endl;
    cout << "Average Turnaround Time: " << totalTAT / n << endl;

    return 0;
}