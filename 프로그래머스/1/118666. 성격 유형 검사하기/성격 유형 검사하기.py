def solution(survey, choices):
    result = ""
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

    for s in range(len(survey)):
        if choices[s]==1:
            dic[survey[s][0]] += 3
        elif choices[s]==2:
            dic[survey[s][0]] += 2
        elif choices[s]==3:
            dic[survey[s][0]] += 1
        elif choices[s] == 4:
            continue
        elif choices[s]==5:
            dic[survey[s][1]] += 1
        elif choices[s]==6:
            dic[survey[s][1]] += 2
        elif choices[s]==7:
            dic[survey[s][1]] += 3


    if dic['R']>dic['T']:
        result = 'R'
    elif dic['R']==dic['T']:    
            result = 'R'
    else:
        result = 'T'
    if dic['C']>dic['F']:
        result += 'C'
    elif dic['C']==dic['F']:    
        result += 'C'
    else:
        result += 'F'
    if dic['J']>dic['M']:
        result += 'J'
    elif dic['J']==dic['M']:    
            result += 'J'
    else:
        result += 'M'
    if dic['A']>dic['N']:
        result += 'A'
    elif dic['A']==dic['N']:    
            result += 'A'
    else:
        result += 'N'
    return result