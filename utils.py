from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=29)
    pessoa.save()
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print(i.nome)

def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    consulta_pessoas()
    altera_pessoas()
    consulta_pessoas()
    exclui_pessoa()
    consulta_pessoas()