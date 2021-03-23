from Bio import SeqIO
from Bio.Blast import NCBIWWW
import time
from Bio.Blast.Applications import *

blastn = "/usr/local/ncbi/blast/bin/blastn"

comando_blastn = NcbiblastnCommandline(
    cmd=blastn,
    query="banco.fasta",
    subject='banco.fasta',
    outfmt=0,
    out="saida.txt"
)

print(f'Comando: {comando_blastn}')

# Executando
start_time = time.time()
stdout, stderr = comando_blastn()
print(f"Programa executtado em: {time.time() - start_time}s.")