s = list(map(int, list(str(input()))))

red = s.count(0)
blue = len(s) - red
print(min(red, blue) * 2)
