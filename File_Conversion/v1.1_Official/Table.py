import color

def table(s):
    print('+'+'-'*8+'+'+'-'*22+'+')
    print(f'| {color.magenta("Number"):<6} | {color.magenta("Module Name"):<29} |')
    print('+'+'-'*8+'+'+'-'*22+'+')
    for i in range(len(s)):
        print(f'|   {color.cyan(str(i+1))}    | {s[i]:<20} |')
        print('+'+'-'*8+'+'+'-'*22+'+')
    print()
