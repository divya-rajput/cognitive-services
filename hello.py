import sys

ans = 'World'

if len(sys.argv) > 1:
    ans = sys.argv[1]
    ans = ans.title()
print(f'Hello, {ans}!')