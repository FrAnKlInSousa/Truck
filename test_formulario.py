import formulario
import pytest


def test_login_admin():
    formulario.login_admin()


def test_abre_formulario():
    formulario.abre_form()


def test_preenche_documentos():
    formulario.preenche_documentos()


def test_preenche_cnh():
    formulario.preenche_cnh()


def test_preenche_outros_docs():
    formulario.preenche_docs_restantes()


def test_add_contatos_pessoais():
    formulario.preenche_dados_pessoais()


def test_add_contatos_ref():
    formulario.preenche_contatos_ref()