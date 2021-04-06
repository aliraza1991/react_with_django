start, end = 12, 10

s = """<a value = "GoodVal">
<b value = "BadVal" size = "10">
<c height = "auto">
<d size = "3">
<e strength = "200%">
<f a1 = "1" a2 = "2" a3 = "3">
</f>
</e>
</d>
</c>
</b>
</a>
a.b.c.d.e.f~a1
a.b.f~a1
a.b~size
a.b.c.d.e.f~a2
a.b.c.d.e.f~a3
a.c~height
a.b.d.e~strength
a.b.c.d.e~strength
d~sze
a.b.c.d~size
"""


def get_last_list(start, end, string=''):
    match_value = []
    lines = string.split('\n')
    for i in range(int(start), int(end)+int(start)):
        line = '~'.join(lines[i].split('.')).split('~')
        match_value.append(line)
    return match_value


last_list_method = get_last_list(start, end, s)


def get_start_list(start, end, string=''):
    lines = string.split('\n')
    values = []
    for j in range(0, int(start)):
        values.append(lines[j])
    return values


start_list_method = get_start_list(start, end, s)


def tag(obj):
    i = 1
    t = ''
    if obj[i] == '/':
        i = 2
    while obj[i] != '>' and obj[i] != ' ':
        t += obj[i]
        i += 1
    return t


def final_func(start, start_list_method):
    list_empty = []
    for end in start_list_method:
        tags = tag(end)
        if end[1] != '/':
            list_empty.append(tags)
        else:
            list_empty.pop()
        if tags == start[-2:-1][0]:
            list_empty.append(start[-1])
            if len(start) == len(list_empty):
                bol = False
                ss = ''
                try:
                    x = end.index(start[-1])
                    while True:
                        if bol and end[x] != '"':
                            ss += end[x]
                        if end[x] == '"' and bol == False:
                            bol = True
                        elif end[x] == '"' and bol == True:
                            return ss
                        x += 1
                except:
                    return 'Not Found'
            else:
                return 'Not found'
    return "Not found"


def main(start_list_method, last_list_method):
    for start in last_list_method:
        y = final_func(start, start_list_method)
        print(y)


if __name__ == '__main__':
    main(start_list_method, last_list_method)
