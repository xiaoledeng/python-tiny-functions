def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

import pprint
a=range(100)
pprint.pprint(list(chunks(a, 10)))

#https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks