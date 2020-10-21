from typing import TextIO, List, Any
from io import StringIO

def count_birds(observations_file: TextIO) -> List[List [Any]] :
    """在观察文件中列出一组鸟类，每行一种鸟类
    >>> infile = StringIo('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
    [['bird 1',2],['bird2',1]]
    """
    bird_counts = []
    for line in observations_file:
        bird = line.strip()
        found = False
        #在列bird_counts中查找bird

        for entry in bird_counts:
            if entry[0] == bird:
                entry[1] = entry[1] + 1
                found = True
        if not found:
            bird_counts.append([bird, 1])
        return bird_counts

if __name__ == '__main__':
    with open('observations.txt') as observations_file:
        bird_counts = count_birds(observations_file)
        #打印每个bird以及它被观察到的次数
        for entry in bird_counts:
            print(entry[0], entry[1])