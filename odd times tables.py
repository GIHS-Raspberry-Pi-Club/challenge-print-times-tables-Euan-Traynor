#By Euan

def oddTimesTables():
    for chips in range(1,13,):
        for fish in range(1,13):
            print(fish%chips, end=" ")
        print()

oddTimesTables()
