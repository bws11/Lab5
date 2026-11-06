# count the number of avaliable proccesses

# 0 - Create a new process.
# 1 - Restart an existing process, giving it a new expiry time.
# A process automatically expires after expiry_time units.
# A restart event is ignored if the process has already expired (i.e., expiry time + 1).


def count_available(events: list, expiry_time: int) -> int:
    active_processes = []
    time = 0

    for i in range(len(events)):
        operation, process_id, time = events[i]

        if operation == 0:
            active_processes.append([process_id, time + expiry_time])

        # restart only if the process hasnt expired
        elif operation == 1:   
            for process in active_processes:
                if process[0] == process_id and time < process[1]:
                    process[1] = time + expiry_time


    # count only the processes still unexpired at the final time
    count = 0
    for process in active_processes:
        expires_at = process[1]

        if expires_at > time:
            count += 1
    
    return count







# [0 or 1, process_id, time of action]
events = [
    [0, 1, 1],
    [0, 2, 2],
    [1, 1, 3],
    [1, 2, 7]
]
expiry_time = 5

result = count_available(events, expiry_time)
print(result)