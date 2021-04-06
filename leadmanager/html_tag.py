start, end = input("Enter two number:- ").split(',')

s = """<tag1 value = "HelloWorld" name = "ali raza">
<tag2 name = "Name1" >
</tag2 >
</tag1 >
tag1.tag2~name
tag1~name
tag1~value"""


def get_last_list(start, end, string=''):
    match_value = []
    lines = string.split('\n')
    for i in range(int(start), int(end)+int(start)):
        line = '~'.join(lines[i].split('.')).split('~')
        match_value.append(line)
    return match_value


last_list_method = get_last_list(start, end, s)
print(last_list_method)


def get_start_list(start, end, string=''):
    lines = string.split('\n')
    values = []
    for j in range(0, int(start)):
        values.append(lines[j])
    return values


start_list_method = get_start_list(start, end, s)
print(start_list_method)


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
