from typing import TextIO,Dict
from io import StringIO

def count_birds(observations_file: TextIO) -> Dict[str, int]:
    """Return a set of the bird species listed in observations_file,which
       has one bird species per line.

       >>> infile = StringIO('bird 1\\nbird  2\\nbird 1\\n')
       >>> count_birds(infile)
       {'bird 1': 2,'bird 2': 1}
    """
    bird_to_observations = {}
    for line in observations_file:
        bird = line.strip()
        bird_to_observations[bird] = bird_to_observations.get(bird, 0) + 1

    return bird_to_observations