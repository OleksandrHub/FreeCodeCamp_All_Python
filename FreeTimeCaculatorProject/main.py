def day_info(day, new_time):
    result = ''
    days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
    new_time['count_day'] += new_time['count_am_pm'] // 2
    if not day is None:
        day = days[(days.index(day.lower()) + new_time['count_day']) % 7]
        result += f', {day.capitalize()}'
    if new_time['count_day'] == 1:
        result += ' (next day)'
    if new_time['count_day'] > 1:
        result += f' ({new_time["count_day"]} days later)'
    return result

def PM_AM(am_pm, new_time):
    if am_pm == 'PM' and new_time['count_am_pm'] > 0:
        new_time['count_day'] += 1
    if new_time['count_am_pm'] % 2 != 0:
        am_pm = "PM" if am_pm == "AM" else "AM"
    new_time['time'] += " " + am_pm
    return new_time

def info_time(times):
    h1, m1, h2, m2 = list(map(int, times.split(":")))    
    h = h1 + h2 + (m1 + m2) // 60
    m = (m1 + m2) % 60
    time = {
        "time":"", 
        "count_am_pm":h//12, 
        "count_day":0
    }
    h %= 12
    time["time"] = (str(h) if h != 0 else "12") + ":" + (str(m) if m > 9 else "0"+str(m))
    return time

def add_time(start, duration, day = None):
    start, am_pm = start.split()
    new_time = info_time(start + ':' + duration)
    new_time = PM_AM(am_pm, new_time)    
    result = new_time['time'] + day_info(day, new_time)
    #print(new_time)
    print(result)
    return result


add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
