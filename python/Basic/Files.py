
def person_lister(f):
    def inner(people):
        return map(f,people)
        
    return inner

@person_lister
def name_format(person):
    
    return (('Mr ' if person[3] == 'M' else 'Ms ')+ person[0]+' '+person[1])

if __name__ == '__main__':
    line =[]
    with open(r'C:\Users\kristhim\GitRepo\prog_ln\python\files\data','r') as f:
        for data in f:
            line.append(data.split())
        print('\n'.join(name_format(line)))