
name = ["may", "kein", "kain", "radi"]
yearning =[5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    answer = []
    dictionary = dict(zip(name, yearning))
    for p in photo:
        score = 0
        for person in p:
            if person in name: 
                score += dictionary[person]
                #print(i,score)
                #print("="*20)
        
        answer.append(score)
        #print("="*50)

    return answer
    
print(solution(name, yearning, photo))