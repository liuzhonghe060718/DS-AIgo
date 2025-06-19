while True:
    try:
        s=input()
    except EOFError:
        break
    print('YES'if s==s[::-1] else 'NO')