def solution(arr, query):
    for i in range(len(query)):
        # query의 인덱스가 짝수번째인지 홀수번째인지!!
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else: arr = arr[query[i]:]
    
    return arr

arr = [1,2,3,4,5,6,7,8,9]
query = [3,5,1]

print(solution(arr, query))