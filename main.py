#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

#Quero mostrar só nome
print(poyatos.nome)

