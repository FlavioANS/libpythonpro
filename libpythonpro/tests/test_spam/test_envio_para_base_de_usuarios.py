import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.qtde_email_enviados
