import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtde_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Flavio', email='flavioonjin@gmail.com'),
            Usuario(nome="Renzo", email='renzo@python.pro.br')
        ],
        [
            Usuario(nome='Flavio', email='flavioonjin@gmail.com'),
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.qtde_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Flavio', email='flavioonjin@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert enviador.parametros_de_envio == (
        'renzo@python.pro.br',
        'flavioonjin@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
