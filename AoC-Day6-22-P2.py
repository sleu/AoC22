parsed = []
test = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
with open('input6.txt') as i:
    datastream = i.read() #datastream is returned as a string

for letter in datastream:
    parsed.append(letter)
    if len(parsed) >= 14:
        check = parsed[-14:]
        if len(check) == len(set(check)):
            print(len(parsed))
            break