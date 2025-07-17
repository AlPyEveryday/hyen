def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage += usage * change[i]/100
        print(usage)
        total_usage += usage
        print(total_usage)
        print("="*50)
        if total_usage > storage:
            return i
    
    return -1

solution(1000, 2000, [-10, 25, -33])