def strcounter(s): # 0(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)
strcounter('abckfaa')

#jhdbfjdfkjdsnal