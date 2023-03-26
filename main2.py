def combinatons(money):
    for g in range(money):
        for f in range(money//2):
            for e in range(money//5):
                for d in range(money//10):
                    for c in range(money//20):
                        for b in range(money//50):
                            for a in range(money//100):
                                if 100*a+50*b+20*c+10*d+5*e+2*f+g == money:
                                    print(f'100X{a}+50X{b}+20X{c}+10X{d}+5X{e}+2X{f}+{g}')
                                    