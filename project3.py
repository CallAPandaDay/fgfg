def intime(case_count):
    num = case_count
    for i in range(0, 15):
        num = num * 0.54
    print(num < 500)

intime(1000000)

def maxcc(growth_rate):
    num = growth_rate
    result = 500
    for i in range(0, 15):
        result = result / growth_rate
    print(int(result))

maxcc(0.54)