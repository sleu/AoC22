parsed_a = []
parsed_b = []
with open('input6.txt') as i:
    datastream = i.read() #datastream is returned as a string

for letter in datastream:
    parsed_a.append(letter)
    if len(parsed_a) >= 4:
        check = parsed_a[-4:]
        if len(check) == len(set(check)):
            print("Answer A: %d" % len(parsed_a))
            break

for letter in datastream:
    parsed_b.append(letter)
    if len(parsed_b) >= 14:
        check = parsed_b[-14:]
        if len(check) == len(set(check)):
            print("Answer B: %d" % len(parsed_b))
            break