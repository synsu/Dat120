def get_falling_distance(tid):
    g=9.81
    fart = g*tid
    distanse = 0.5*fart*tid
    return distanse


def get_speed(tid):
    g=9.81
    fart=g*tid
    return fart


tid=float(input("> "))
while tid>0:
    print ("fart " + str(get_speed(tid)))
    print("distanse " + str (get_falling_distance(tid)))
    tid=float(input("> "))

