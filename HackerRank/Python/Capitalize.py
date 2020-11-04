def solve(s):
    part = s.split()
    new = []
    for parts in part:
        if parts[0].isalpha():
            new.append(parts.title())
        else:
            new.append(parts)
    output = ' '.join(new)
    s = s.title()
    return s
    


o = solve('md 3hakib')
print(o)