import copy

inp = """0;9;35,12,3;26
1;8;7,29,3;1
2;96;22,36,32;39
3;88;10,9,31;76
4;51;14,33,17;66
5;77;4,18,34;30
6;68;16,34,26;10
7;3;23,27,32;96
8;32;1,33,9;60
9;26;39,15,20;18
10;98;33,36,29;51
11;52;14,21,22;8
12;77;3,31,13;85
13;30;4,9,34;35
14;88;22,6,40;97
15;34;12,10,21;65
16;67;24,33,8;58
17;6;6,1,24;55
18;53;7,38,6;91
19;37;38,26,11;69
20;68;14,5,6;94
21;24;12,13,30;19
22;97;36,8,9;35
23;2;3,8,36;8
24;9;16,38,4;89
25;91;1,14,24;40
26;86;31,19,3;55
27;55;9,7,29;47
28;79;37,33,34;53
29;23;6,7,21;54
30;45;11,32,10;2
31;23;26,37,12;24
32;42;16,37,14;94
33;56;19,13,39;23
34;70;31,11,7;33
35;54;23,10,2;34
36;76;37,12,6;60
37;67;16,25,11;57
38;3;14,27,32;72
39;33;37,4,13;90"""

strings = inp.split('\n')
items = []
for s in strings:
    ss = s.split(';')
    unc = ss[2].split(',')
    items.append({'id': int(ss[0]), 'weight': int(ss[1]), 'unc': unc, 'value': int(ss[3])})

items_count = len(items)

items_state = [-1 for _ in range(items_count)]
max_value_state = []
max_value = 0


def is_ok(current_items):
    # Collecting containers items indexes
    in2 = []
    in1 = []
    for i in range(items_count):
        if current_items[i] == 1:
            in1.append(i)
        elif current_items[i] == 2:
            in2.append(i)

    # Checking for overweight
    w1 = 0
    for index in in1:
        w1 += items[index]['weight']
    if w1 > 100:
        return False
    w2 = 0
    for index in in2:
        w2 += items[index]['weight']
    if w2 > 100:
        return False

    # Checking for compatibility
    for index in in1:
        if any(i in items[index]['unc'] for i in in1):
            return False
    for index in in2:
        if any(i in items[index]['unc'] for i in in2):
            return False

    return True


def compute_value(current_items):
    if not is_ok(current_items):
        return
    value = 0
    for i in range(items_count):
        if current_items[i] == 1 or current_items[i] == 2:
            value += items[i]['value']

    # Checking for overwriting current max value
    global max_value
    global max_value_state
    if value > max_value:
        max_value = value
        print(current_items, value)
        max_value_state = current_items


def putter(k=0):
    if k == 40:
        compute_value(items_state)
        return False
    else:
        if items_state[k] != -1:
            return putter(k + 1)
        else:
            items_state[k] = 0
            if is_ok(items_state):
                if putter(k+1):
                    return False

            items_state[k] = 1
            if is_ok(items_state):
                if putter(k+1):
                    return False

            items_state[k] = 2
            if is_ok(items_state):
                if putter(k+1):
                    return False

            compute_value(items_state)
            items_state[k] = -1
            return False


putter()
print(max_value)
print(max_value_state)
