def jingleBells(octave=4):
    notes = [
        'E', 'E', 'Eh',  # jin-gle bells
        'E', 'E', 'Eh',  # jin-gle bells
        'E', 'G', 'C', 're', 'De',  # jin-gle all the way
        'Ew',  # way
        'F', 'F', 'F', 're', 'Fe',  # oh what fun
        'F', 'E', 'E', 'Ee', 'Ee',  # it is to ride
        'E', 'D', 'D', 'E',  # in a one-horse
        'Dh', 'Gh',  # open sleigh. Oh!
        'E', 'E', 'Eh',  # jin-gle bells
        'E', 'E', 'Eh',  # jin-gle bells
        'E', 'G', 'C', 're', 'De',  # jin-gle all the way
        'Ew',  # way
        'F', 'F', 'F', 'F',  # oh what fun
        'F', 'E', 'E', 'Ee', 'Ee',  # it is to ride
        'G', 'G', 'F', 'D',  # in a one-horse open
        'Cw'  # sleigh
    ]

    nextNotes = list(map(lambda note: note + str(octave), notes))

    return nextNotes
