#-- reading FASTA --
def read_fasta(file_path):

    with open(file_path, 'r') as file:
        sequences = {}
        sequence_id = None
        sequence = ''

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence_id is not None:
                    sequences[sequence_id] = sequence
                sequence_id = line[1:]
                sequence = ''
            else:
                sequence += line

        if sequence_id is not None:
            sequences[sequence_id] = sequence
        return sequences

answers = []
dna_seq = read_fasta()
for i in dna_seq:
    answer = {}
    for j in range(1, len(i)):
        for k in range(len(i) - j, 0, -1):
            h = i.count(i[k::j])
            if i[k::j] not in answer and h>1:
                answer[i[k::j]] = h

    sorted_answer = sorted(answer.items(), key=lambda x:x[1])
    answers.append(sorted_answer)

num = 1
for dict in answers:
    print("Seq" + str(num) + ":")
    num+=1

for key, value in sorted_answer:
    a= str(key)
    b= str(value)
    print(a, ' ', b)

