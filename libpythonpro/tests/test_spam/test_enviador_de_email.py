import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['renzo@python.pro.br', 'foo@bar,com,br']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von osumm aberta.'
        )
    assert destinatario in resultado
