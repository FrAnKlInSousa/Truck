import page_formulario


def login_admin():
    page_formulario.preenche_email("franklin.silva@truckpad.com.br")
    page_formulario.preenche_senha("teste123")
    page_formulario.click_entrar()
    assert page_formulario.obtem_titulo_pagina_inicial() == "Cargas em oferta"


def abre_form():
    page_formulario.btn_motoristas()
    assert page_formulario.btn_adicionar_motorista() == "Cadastrar motorista"


def preenche_documentos():
    page_formulario.fill_cpf("35267948802")
    page_formulario.fill_cnpj("92083772000152")
    page_formulario.fill_rg("458195996")
    page_formulario.fill_orgao_expedidor_rg("SSP")
    page_formulario.select_estado_expedidor_rg("SP")
    page_formulario.fill_data_expedicao_rg("13/04/1989")


def preenche_cnh():
    page_formulario.fill_cnh("123321123")
    page_formulario.fill_categoria_cnh("AB")
    page_formulario.fill_data_emissão_cnh("13/04/1989")
    page_formulario.fill_data_expiracao_cnh("14/04/1989")
    page_formulario.fill_orgao_expedidor_cnh("DETRAN")
    page_formulario.select_estado_expedidor_cnh("SP")
    page_formulario.select_cidade_emissao_cnh("SÃO PAULO")
    page_formulario.fill_data_primeira_cnh("15/04/1989")
    page_formulario.fill_cod_seguranca_cnh("12332876871") # deve ter exatamente 11 dígitos (apenas numérico)
    page_formulario.fill_serial_cnh("123321123")


def preenche_docs_restantes():
    page_formulario.fill_pis("123456654321")
    page_formulario.fill_rntrc("9898121212")
    page_formulario.select_tipo_rntrc("TAC Independente")
    page_formulario.fill_validade_rntrc("15/04/1989")
    page_formulario.fill_inss("987123789")
    page_formulario.fill_email_form("teste@teste.com.br")


def preenche_dados_pessoais():
    btn_contato1 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div > div > button'
    nome_contato1 = '.formGroup .ant-input[name="contacts.phone_personal[0].contact"]'
    tipo_tel_contato1 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div.ant-row-flex.ant-row-flex-end.rowPhones > div:nth-child(2) > div > select'
    ddd_contato1 = '.formGroup [name="contacts.phone_personal[0].area_code"]'
    tel_contato1 = '.formGroup [name="contacts.phone_personal[0].number"]'
    operadora_contato1 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div:nth-child(1) > div:nth-child(5) > div > select'
    whatsapp_contato1 = '.content-panel-custom [name="contacts.phone_personal[0].whatsapp"]'

    btn_contato2 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div.ant-row-flex.ant-row-flex-end.ant-row-flex-middle > div > div > button'
    nome_contato2 = '.formGroup .ant-input[name="contacts.phone_personal[1].contact"]'
    tipo_tel_contato2 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div:nth-child(2) > div:nth-child(2) > div > select'
    ddd_contato2 = '.formGroup [name="contacts.phone_personal[1].area_code"]'
    tel_contato2 = '.formGroup [name="contacts.phone_personal[1].number"]'
    operadora_contato2 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div:nth-child(2) > div:nth-child(5) > div > select'
    whatsapp_contato2 = '.content-panel-custom [name="contacts.phone_personal[1].whatsapp"]'

    page_formulario.fill_nome_contato_cp(btn_contato1, nome_contato1, "Contato teste")
    page_formulario.select_tipo_tel_cp(tipo_tel_contato1, "Fixo")
    page_formulario.fill_ddd_cp(ddd_contato1, "11")
    page_formulario.fill_tel_cp(tel_contato1, "22224444")
    page_formulario.select_operadora_cp(operadora_contato1, "TIM")
    page_formulario.set_whatsapp(whatsapp_contato1)

    page_formulario.fill_nome_contato_cp(btn_contato2, nome_contato2, "Contato teste2")
    page_formulario.select_tipo_tel_cp(tipo_tel_contato2, "Celular")
    page_formulario.fill_ddd_cp(ddd_contato2, "15")
    page_formulario.fill_tel_cp(tel_contato2, "922224444")
    page_formulario.select_operadora_cp(operadora_contato2, "Vivo")
    page_formulario.set_whatsapp(whatsapp_contato2)
