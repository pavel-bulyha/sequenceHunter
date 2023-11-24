#-- reading FASTA --
def read_fasta(file_path):
    with open(file_path, 'r') as file:
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
                seq_counter +=1
                sequence = ''
            else:
                sequence += line
        if sequence_id is not None:
            sequences[sequence_id] = sequence
        return sequences