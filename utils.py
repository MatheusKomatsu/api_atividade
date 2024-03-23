from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa1 = Pessoas(nome='Rafael', idade=29)
    pessoa2 = Pessoas(nome='Matheus', idade=21)
    pessoa3 = Pessoas(nome='Gabriel', idade=19)
    pessoa1.save()
    pessoa2.save()
    pessoa3.save()
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

def insere_usuario(login,senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('Matheus', '1234')
    insere_usuario('Gabriel', '4321')
    consulta_usuarios()
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoas()
    # consulta_pessoas()
    # exclui_pessoa()
    # consulta_pessoas()