#instalando o Bipython

pip install biopython


#lendo arquivo fasta como o banco
import Bio
from Bio import SeqIO


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import re
for i in SeqIO.parse('banco.fasta','fasta'):
 print (i.id)


 sequencias = list(SeqIO.parse("banco.fasta","fasta"))


 #tentei um Blast para fazer um busca no banco só de procariotas. porém deu erro de tamanho do documento

from Bio.Blast import NCBIWWW

from Bio import SeqIO



arquivo = SeqIO.read('banco.fasta', format='fasta')

print 'Iniciando busca no NCBIWWW'

resultado = NCBIWWW.qblast('blastn','nt',\
	arquivo.seq,format_type='Text')

print resultado.read()

print 'Busca concluida'