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
    page_formulario.fill_data_emissao_cnh("13/04/1989")
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


def preenche_contatos_ref():
    btn_add_tel_ref1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div > div > div > button'
    tipo_ref1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div.ant-row.rowPhones > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
    tipo_tel1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div.ant-row.rowPhones > div:nth-child(2) > div > select'
    ddd1 = '.formGroup [name="contacts.phone_reference[0].area_code"]'
    tel1 = '.formGroup [name="contacts.phone_reference[0].number"]'
    operadora1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div.ant-row.rowPhones > div:nth-child(5) > div > select'
    contato1 = '.formGroup [name="contacts.phone_reference[0].contact"]'
    empresa1 = '.formGroup [name="contacts.phone_reference[0].company"]'


    btn_add_tels_ref = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div.ant-row-flex.ant-row-flex-end.ant-row-flex-middle > div > div > button'
    tipo_ref2 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
    tipo_tel2 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div:nth-child(2) > div > select'
    ddd2 = '.formGroup [name="contacts.phone_reference[1].area_code"]'
    tel2 = '.formGroup [name="contacts.phone_reference[1].number"]'
    operadora2 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div:nth-child(5) > div > select'
    contato2 = '.formGroup [name="contacts.phone_reference[1].contact"]'
    empresa2 = '.formGroup [name="contacts.phone_reference[1].company"]'

    tipo_ref3 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(3) > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
    tipo_tel3 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(3) > div:nth-child(2) > div > select'
    ddd3 = '.formGroup [name="contacts.phone_reference[2].area_code"]'
    tel3 = '.formGroup [name="contacts.phone_reference[2].number"]'
    operadora3 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(3) > div:nth-child(5) > div > select'
    contato3 = '.formGroup [name="contacts.phone_reference[2].contact"]'
    empresa3 = '.formGroup [name="contacts.phone_reference[2].company"]'

    tipo_ref4 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(4) > div.ant-col.ant-col-xs-24.ant-col-sm-24.ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
    tipo_tel4 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(4) > div:nth-child(2) > div > select'
    ddd4 = '.formGroup [name="contacts.phone_reference[3].area_code"]'
    tel4 = '.formGroup [name="contacts.phone_reference[3].number"]'
    operadora4 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(4) > div:nth-child(5) > div > select'
    contato4 = '.formGroup [name="contacts.phone_reference[3].contact"]'
    empresa4 = '.formGroup [name="contacts.phone_reference[3].company"]'

    page_formulario.select_tipo_referencia(btn_add_tel_ref1, tipo_ref1, 'Pessoal')
    page_formulario.select_tipo_tel_ref(tipo_tel1, 'Celular')
    page_formulario.fill_ddd_ref(ddd1, '15')
    page_formulario.fill_tel_ref(tel1, '912345555')
    page_formulario.select_operadora_ref(operadora1, 'TIM')
    page_formulario.fill_nome_contato_ref(contato1, 'Franklin Silva e Silva')
    page_formulario.fill_nome_empresa_ref(empresa1, 'TruckPad')

    page_formulario.select_tipo_referencia(btn_add_tels_ref, tipo_ref2, 'Pessoal')
    page_formulario.select_tipo_tel_ref(tipo_tel2, 'Fixo')
    page_formulario.fill_ddd_ref(ddd2, '11')
    page_formulario.fill_tel_ref(tel2, '29217290')
    page_formulario.select_operadora_ref(operadora2, 'Oi')
    page_formulario.fill_nome_contato_ref(contato2, 'Franklin Sousa')
    page_formulario.fill_nome_empresa_ref(empresa2, 'TruckPad')

    page_formulario.select_tipo_referencia(btn_add_tels_ref, tipo_ref3, 'Comercial')
    page_formulario.select_tipo_tel_ref(tipo_tel3, 'Celular')
    page_formulario.fill_ddd_ref(ddd3, '11')
    page_formulario.fill_tel_ref(tel3, '929217290')
    page_formulario.select_operadora_ref(operadora3, 'Oi')
    page_formulario.fill_nome_contato_ref(contato3, 'Franklin')
    page_formulario.fill_nome_empresa_ref(empresa3, 'TruckPad')

    page_formulario.select_tipo_referencia(btn_add_tels_ref, tipo_ref4, 'Comercial')
    page_formulario.select_tipo_tel_ref(tipo_tel4, 'Fixo')
    page_formulario.fill_ddd_ref(ddd4, '11')
    page_formulario.fill_tel_ref(tel4, '29217291')
    page_formulario.select_operadora_ref(operadora4, 'Oi')
    page_formulario.fill_nome_contato_ref(contato4, 'Aline Ueda')
    page_formulario.fill_nome_empresa_ref(empresa4, 'TruckPad')


# Dados para pagamentos

def preenche_dados_pagamento():
    btn_add_pagamento1 = '#form-driver > div:nth-child(3) > div > div > div > div > div > div > div > div > div > button'
    # btn_add_outros_pagamentos = '#form-driver > div:nth-child(3) > div > div > div > div > div > div > div.ant-row-flex.ant-row-flex-end > div > div > button'
    nome1 = '.formGroup [name="info_bank[0].name"]'
    cpf1 = '.formGroup [name="info_bank[0].cpf"]'
    banco1 = '.formGroup [name="info_bank[0].bank"]'
    agencia1 = '.formGroup [name="info_bank[0].agency"]'
    conta1 = '.formGroup [name="info_bank[0].account"]'
    tipo_conta1 = '#form-driver > div:nth-child(3) > div > div > div > div > div > div > div.ant-row > div.ant-row > div:nth-child(6) > div > select'

    page_formulario.fill_nome_pagamento(btn_add_pagamento1, nome1, 'Franklin Sousa')
    page_formulario.fill_cpf_pagamento(cpf1, '35267948802')
    page_formulario.fill_banco_pagamento(banco1, '123')
    page_formulario.fill_agencia_pagamento(agencia1, '1234')
    page_formulario.fill_conta_pagamento(conta1, '32133211')
    page_formulario.select_tipo_conta_pagamento(tipo_conta1, 'Corrente')