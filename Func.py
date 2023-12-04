def read_fasta():
    with open('fasta.fsa', 'r') as file:
        sequences = {}
        sequence_id = None
        sequence = ''
        seq_counter = 1

        for line in file:

            line = line.strip()
            if line.startswith('>'):
                if sequence_id is not None:
                    sequences[sequence_id] = sequence
                sequence_id = 'Seq' + str(seq_counter)
                seq_counter += 1
                sequence = ''
            else:
                sequence += line
        if sequence_id is not None:
            sequences[sequence_id] = sequence
        dna_sequence = []
        for key, value in sequences.items():
            dna_sequence.append(value)

        return dna_sequence


answers = []
dna_seq = read_fasta()
for i in dna_seq:
    answer = {}
    for j in range(1, len(i)):
        for k in range(len(i) - j, 0, -1):
            keyy = i[k::j]
            h = i.count(keyy)
            if keyy not in answer and h>1:
                answer[keyy] = h


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

while True:
    print('Введите последовательность, которую вы хотите найти')
    seq = str(input())
    for key, value in answer.items():
        if key == seq:
            z=answer[key]
            if z!=11 and z!=111 and z%10 == 1:
                print(z, 'раз она повторяется')
            elif z%10 == 2 and z!=12 and z!=112:
                print(z, 'раза она повторяется')
            elif z%10 == 3 and z!=13 and z!=113:
                print(z, 'раза она повторяется')
            elif z%10 == 4 and z!=14 and z!=114:
                print(z, 'разa она повторяется')
            else:
                print(z, 'раз она повторяется')
            continue
        if seq not in answer:
            print('Такой последовательности нет')
            break















