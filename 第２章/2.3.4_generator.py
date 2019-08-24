def linestyle_generator():
    linestyle = ['-', '--', '-.', ':']
    lineID = 0
    while True:
        yield linestyle[lineID]
        lineID = (lineID + 1) % len(linestyle)


LS = linestyle_generator()  # make a generator : "LS"
for i in range(5):
    print(next(LS))
