def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

import pprint
a=range(100)
pprint.pprint(list(chunks(a, 10)))