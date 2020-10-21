#函数直角九九
def DNA(x: str) -> str:
    """ 
        'A'<->'T'
        'C'<->'G'
    """
    s = ""
    for i in x:
        if i == 'A':
            s += 'T'
        if i == 'T':
            s += 'A'
        if i == 'G':
            s += 'C'
        if i == 'C':
            s += 'G'
    return s

#字典函数
def dna(x : str) -> str:
    s = ""
    a = {'A': 'T','T': 'A','C': 'G','G': 'C'}
    for i in x:
        s += a[i]
    return s

if __name__ == '__main__':
    print(DNA('ATGC'))
    print(dna('ATCG'))