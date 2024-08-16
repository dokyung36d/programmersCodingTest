def solution(today, terms, privacies):
    terms_dict = {}
    for term in terms:
        term_name, term_period = term.split()
        terms_dict[term_name] = int(term_period)
        
        
    today_list = list(map(int, today.split(".")))
    answer = []
    i = 0
        
    for privacy in privacies:
        i += 1
        startday, term = privacy.split(" ")
        expirationday_list = list(get_expiration_date(startday, terms_dict[term]))
        
        bigger_date = return_bigger_date(date0 = today_list, date1 = expirationday_list)
        
        if bigger_date == today_list:
            answer.append(i)
        
    return answer

def get_expiration_date(current_date, term_month : int):
    year, month, date = map(int, current_date.split("."))
    
    if date == 1 and month == 1:
        date = 28
        month = 12
        year -= 1
    elif date == 1 and month != 1:
        date = 28
        month -= 1
    else:
        date -= 1
    
    year_plus = term_month // 12
    month_plus = term_month % 12
        
    year += year_plus
    month += month_plus
    
    if month > 12:
        year += month // 12
        month = month % 12
    
    return (year, month, date)

def return_bigger_date(date0 : list, date1 : list):
    if date0[0] > date1[0]:
        return date0
    if date0[0] < date1[0]:
        return date1
    
    if date0[1] > date1[1]:
        return date0
    if date0[1] < date1[1]:
        return date1
    
    if date0[2] > date1[2]:
        return date0
    if date0[2] < date1[2]:
        return date1