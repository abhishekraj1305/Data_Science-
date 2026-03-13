print("===== HYPER COMPLEX BRANCH MATRIX =====")

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
e = int(input("E: "))
f = int(input("F: "))

if a > 0:
    print("L1 -> A positive")

    if b > 0:
        print("L2 -> B positive")

        if c > 0:
            print("L3 -> C positive")

            if d > 0:
                print("L4 -> D positive")

                if e > 0:
                    print("L5 -> E positive")

                    if f > 0:
                        print("L6 -> F positive")

                        if a > b:
                            print("L7 -> A > B")

                            if b > c:
                                print("L8 -> B > C")

                                if c > d:
                                    print("L9 -> C > D")

                                    if d > e:
                                        print("L10 -> D > E")

                                        if e > f:
                                            print("L11 -> Strict descending order")
                                        elif e == f:
                                            print("L11 -> E equals F")
                                        else:
                                            print("L11 -> E < F")

                                    elif d == e:
                                        print("L10 -> D equals E")

                                        if (a + b) > (c + f):
                                            print("L11 -> Left sum dominant")
                                        elif (a + b) == (c + f):
                                            print("L11 -> Balanced sums")
                                        else:
                                            print("L11 -> Right sum dominant")

                                    else:
                                        print("L10 -> D < E")

                                        if (d * f) % 2 == 0:
                                            print("L11 -> Product even")
                                        elif (d * f) % 3 == 0:
                                            print("L11 -> Product divisible by 3")
                                        else:
                                            print("L11 -> Product complex")

                                elif c == d:
                                    print("L9 -> C equals D")

                                    if (a * e) > (b * f):
                                        print("L10 -> Cross dominance")

                                        if a % 2 == 0:
                                            print("L11 -> A even")
                                        elif a % 3 == 0:
                                            print("L11 -> A divisible by 3")
                                        else:
                                            print("L11 -> A prime-like behavior")

                                    elif (a * e) == (b * f):
                                        print("L10 -> Cross balance")

                                        if e > 10:
                                            print("L11 -> E > 10")
                                        else:
                                            print("L11 -> E <= 10")

                                    else:
                                        print("L10 -> Reverse dominance")

                                else:
                                    print("L9 -> C < D")

                                    if (a + c + e) > (b + d + f):
                                        print("L10 -> Triple sum left")

                                        if f % 2 == 0:
                                            print("L11 -> F even")
                                        elif f % 5 == 0:
                                            print("L11 -> F multiple of 5")
                                        else:
                                            print("L11 -> F irregular")

                                    elif (a + c + e) == (b + d + f):
                                        print("L10 -> Triple sums equal")
                                    else:
                                        print("L10 -> Triple sum right")

                            elif b == c:
                                print("L8 -> B equals C")

                                if (a - d) > (e - f):
                                    print("L9 -> Difference pattern")

                                    if abs(a - f) > 20:
                                        print("L10 -> Wide gap")
                                    elif abs(a - f) == 20:
                                        print("L10 -> Exact gap")
                                    else:
                                        print("L10 -> Narrow gap")

                                elif (a - d) == (e - f):
                                    print("L9 -> Balanced differences")
                                else:
                                    print("L9 -> Reverse difference pattern")

                            else:
                                print("L8 -> B < C")

                                if (a % 2 == 0 and c % 2 == 0):
                                    print("L9 -> Both even")

                                    if (d + e + f) > 100:
                                        print("L10 -> Heavy load")
                                    elif (d + e + f) == 100:
                                        print("L10 -> Perfect 100")
                                    else:
                                        print("L10 -> Under 100")

                                elif (a % 2 == 1 and c % 2 == 1):
                                    print("L9 -> Both odd")
                                else:
                                    print("L9 -> Mixed parity")

                        elif a == b:
                            print("L7 -> A equals B")

                            if (c > d):
                                print("L8 -> C > D")

                                if (e > f):
                                    print("L9 -> E > F")

                                    if (a + c) > (d + f):
                                        print("L10 -> Upper diagonal dominance")
                                    elif (a + c) == (d + f):
                                        print("L10 -> Perfect diagonal symmetry")
                                    else:
                                        print("L10 -> Lower diagonal dominance")

                                elif (e == f):
                                    print("L9 -> E equals F")
                                else:
                                    print("L9 -> E < F")

                            elif (c == d):
                                print("L8 -> C equals D")

                                if (a * f) > 500:
                                    print("L9 -> High multiplication zone")
                                elif (a * f) == 500:
                                    print("L9 -> Exact 500")
                                else:
                                    print("L9 -> Under 500")

                            else:
                                print("L8 -> C < D")

                        else:
                            print("L7 -> A < B")

                            if (a + f) > (b + e):
                                print("L8 -> Edge shift")

                                if (c * d) > 1000:
                                    print("L9 -> High product")
                                elif (c * d) == 1000:
                                    print("L9 -> Exact product")
                                else:
                                    print("L9 -> Low product")

                            elif (a + f) == (b + e):
                                print("L8 -> Edge balance")
                            else:
                                print("L8 -> Edge reversal")

                    elif f == 0:
                        print("L6 -> F zero")
                    else:
                        print("L6 -> F negative")

                elif e == 0:
                    print("L5 -> E zero")
                else:
                    print("L5 -> E negative")

            elif d == 0:
                print("L4 -> D zero")
            else:
                print("L4 -> D negative")

        elif c == 0:
            print("L3 -> C zero")
        else:
            print("L3 -> C negative")

    elif b == 0:
        print("L2 -> B zero")
    else:
        print("L2 -> B negative")

elif a == 0:
    print("L1 -> A zero")
else:
    print("L1 -> A negative")

print("===== END OF HYPER MATRIX =====")