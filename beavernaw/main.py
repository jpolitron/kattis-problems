import math
D,V = map(int,input().split())
while(D!= 0 and V != 0):
    total = math.pi * pow(D/2,2) * D
    wood = total - V
    cones = math.pi * pow(D/2,2) * (D/3)
    shape = wood - cones
    cylinder = shape * 1.5
    r = pow(cylinder / 2*math.pi, 1.0/3)
    #cout.prescision(9)
    print(r*2)
