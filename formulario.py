from page_formulario import PageForm


class Form(PageForm):
    def __init__(self):
        self.page = PageForm.__init__(self)

    def login_admin(self):
        self.page.preenche_email("franklin.silva@truckpad.com.br")
        self.page.preenche_senha("teste123")
        self.page.click_entrar()
        assert self.page.obtem_titulo_pagina_inicial() == "Cargas em oferta"

    def abre_form(self):
        self.page.btn_motoristas()
        assert self.page.btn_adicionar_motorista() == "Cadastrar motorista"

    def preenche_documentos(self):
        self.page.fill_cpf("35267948802")
        self.page.fill_cnpj("92083772000152")
        self.page.fill_rg("458195996")
        self.page.fill_orgao_expedidor_rg("SSP")
        self.page.select_estado_expedidor_rg("SP")
        self.page.fill_data_expedicao_rg("13/04/1989")

    def preenche_cnh(self):
        self.page.fill_cnh("123321123")
        self.page.fill_categoria_cnh("AB")
        self.page.fill_data_emissao_cnh("13/04/1989")
        self.page.fill_data_expiracao_cnh("14/04/1989")
        self.page.fill_orgao_expedidor_cnh("DETRAN")
        self.page.select_estado_expedidor_cnh("SP")
        self.page.select_cidade_emissao_cnh("SÃO PAULO")
        self.page.fill_data_primeira_cnh("15/04/1989")
        # fill_cod_seguranca_cnh deve ter exatamente 11 dígitos (apenas numérico)
        self.page.fill_cod_seguranca_cnh("12332876871")
        self.page.fill_serial_cnh("123321123")

    def preenche_docs_restantes(self):
        self.page.fill_pis("123456654321")
        self.page.fill_rntrc("9898121212")
        self.page.select_tipo_rntrc("TAC Independente")
        self.page.fill_validade_rntrc("15/04/1989")
        self.page.fill_inss("987123789")
        self.page.fill_email_form("teste@teste.com.br")

    def preenche_contatos_pessoais(self):
        self.page.btn_contato1 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) ' \
                                 '> div > div > div > div > div > div > div > button'
        self.page.nome_contato1 = '.formGroup .ant-input[name="contacts.phone_personal[0].contact"]'
        self.page.tipo_tel_contato1 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > ' \
                                      'div > div > div > div.ant-row-flex.ant-row-flex-end.rowPhones ' \
                                      '> div:nth-child(2) > div > select'
        self.page.ddd_contato1 = '.formGroup [name="contacts.phone_personal[0].area_code"]'
        self.page.tel_contato1 = '.formGroup [name="contacts.phone_personal[0].number"]'
        self.page.operadora_contato1 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div ' \
                                       '> div > div > div > div:nth-child(1) > div:nth-child(5) > div > select'
        self.page.whatsapp_contato1 = '.content-panel-custom [name="contacts.phone_personal[0].whatsapp"]'

        self.page.btn_contato2 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > ' \
                                 'div > div.ant-row-flex.ant-row-flex-end.ant-row-flex-middle > div > div > button'
        self.page.nome_contato2 = '.formGroup .ant-input[name="contacts.phone_personal[1].contact"]'
        self.page.tipo_tel_contato2 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > ' \
                                      'div > div > div > div > div:nth-child(2) > div:nth-child(2) > div > select'
        self.page.ddd_contato2 = '.formGroup [name="contacts.phone_personal[1].area_code"]'
        self.page.tel_contato2 = '.formGroup [name="contacts.phone_personal[1].number"]'
        self.page.operadora_contato2 = '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div ' \
                                       '> div > div > div > div:nth-child(2) > div:nth-child(5) > div > select'
        self.page.whatsapp_contato2 = '.content-panel-custom [name="contacts.phone_personal[1].whatsapp"]'

        self.page.fill_nome_contato_cp(self.page.btn_contato1, self.page.nome_contato1, "Contato teste")
        self.page.select_tipo_tel_cp(self.page.tipo_tel_contato1, "Fixo")
        self.page.fill_ddd_cp(self.page.ddd_contato1, "11")
        self.page.fill_tel_cp(self.page.tel_contato1, "22224444")
        self.page.select_operadora_cp(self.page.operadora_contato1, "TIM")
        self.page.set_whatsapp(self.page.whatsapp_contato1)

        self.page.fill_nome_contato_cp(self.page.btn_contato2, self.page.nome_contato2, "Contato teste2")
        self.page.select_tipo_tel_cp(self.page.tipo_tel_contato2, "Celular")
        self.page.fill_ddd_cp(self.page.ddd_contato2, "15")
        self.page.fill_tel_cp(self.page.tel_contato2, "922224444")
        self.page.select_operadora_cp(self.page.operadora_contato2, "Vivo")
        self.page.set_whatsapp(self.page.whatsapp_contato2)

    def preenche_contatos_ref(self):
        self.page.btn_add_tel_ref1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) ' \
                                     '> div > div > div > div > div > div > button'
        self.page.tipo_ref1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div >' \
                              ' div > div.ant-row.rowPhones > div.ant-col.ant-col-xs-24.ant-col-sm-24.' \
                              'ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
        self.page.tipo_tel1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > ' \
                              'div > div > div.ant-row.rowPhones > div:nth-child(2) > div > select'
        self.page.ddd1 = '.formGroup [name="contacts.phone_reference[0].area_code"]'
        self.page.tel1 = '.formGroup [name="contacts.phone_reference[0].number"]'
        self.page.operadora1 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div >' \
                               ' div > div.ant-row.rowPhones > div:nth-child(5) > div > select'
        self.page.contato1 = '.formGroup [name="contacts.phone_reference[0].contact"]'
        self.page.empresa1 = '.formGroup [name="contacts.phone_reference[0].company"]'

        self.page.btn_add_tels_ref = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > ' \
                                     'div > div > div > div.ant-row-flex.ant-row-flex-end.' \
                                     'ant-row-flex-middle > div > div > button'
        self.page.tipo_ref2 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > ' \
                              'div > div > div:nth-child(2) > div.ant-col.ant-col-xs-24.ant-col-sm-24.' \
                              'ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
        self.page.tipo_tel2 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > ' \
                              'div > div > div:nth-child(2) > div:nth-child(2) > div > select'
        self.page.ddd2 = '.formGroup [name="contacts.phone_reference[1].area_code"]'
        self.page.tel2 = '.formGroup [name="contacts.phone_reference[1].number"]'
        self.page.operadora2 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div ' \
                               '> div > div > div:nth-child(2) > div:nth-child(5) > div > select'
        self.page.contato2 = '.formGroup [name="contacts.phone_reference[1].contact"]'
        self.page.empresa2 = '.formGroup [name="contacts.phone_reference[1].company"]'

        self.page.tipo_ref3 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > ' \
                              'div > div > div:nth-child(3) > div.ant-col.ant-col-xs-24.' \
                              'ant-col-sm-24.ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
        self.page.tipo_tel3 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > ' \
                              'div > div > div:nth-child(3) > div:nth-child(2) > div > select'
        self.page.ddd3 = '.formGroup [name="contacts.phone_reference[2].area_code"]'
        self.page.tel3 = '.formGroup [name="contacts.phone_reference[2].number"]'
        self.page.operadora3 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > ' \
                               'div > div > div > div:nth-child(3) > div:nth-child(5) > div > select'
        self.page.contato3 = '.formGroup [name="contacts.phone_reference[2].contact"]'
        self.page.empresa3 = '.formGroup [name="contacts.phone_reference[2].company"]'

        self.page.tipo_ref4 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div > div > ' \
                              'div > div:nth-child(4) > div.ant-col.ant-col-xs-24.ant-col-sm-24' \
                              '.ant-col-md-12.ant-col-lg-6.ant-col-xl-4 > div > select'
        self.page.tipo_tel4 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div ' \
                              '> div > div > div:nth-child(4) > div:nth-child(2) > div > select'
        self.page.ddd4 = '.formGroup [name="contacts.phone_reference[3].area_code"]'
        self.page.tel4 = '.formGroup [name="contacts.phone_reference[3].number"]'
        self.page.operadora4 = '#form-driver > div:nth-child(2) > div > div:nth-child(3) > div ' \
                               '> div > div > div:nth-child(4) > div:nth-child(5) > div > select'
        self.page.contato4 = '.formGroup [name="contacts.phone_reference[3].contact"]'
        self.page.empresa4 = '.formGroup [name="contacts.phone_reference[3].company"]'

        self.page.select_tipo_referencia(self.page.btn_add_tel_ref1, self.page.tipo_ref1, 'Pessoal')
        self.page.select_tipo_tel_ref(self.page.tipo_tel1, 'Celular')
        self.page.fill_ddd_ref(self.page.ddd1, '15')
        self.page.fill_tel_ref(self.page.tel1, '912345555')
        self.page.select_operadora_ref(self.page.operadora1, 'TIM')
        self.page.fill_nome_contato_ref(self.page.contato1, 'Franklin Silva e Silva')
        self.page.fill_nome_empresa_ref(self.page.empresa1, 'TruckPad')

        self.page.select_tipo_referencia(self.page.btn_add_tels_ref, self.page.tipo_ref2, 'Pessoal')
        self.page.select_tipo_tel_ref(self.page.tipo_tel2, 'Fixo')
        self.page.fill_ddd_ref(self.page.ddd2, '11')
        self.page.fill_tel_ref(self.page.tel2, '29217290')
        self.page.select_operadora_ref(self.page.operadora2, 'Oi')
        self.page.fill_nome_contato_ref(self.page.contato2, 'Franklin Sousa')
        self.page.fill_nome_empresa_ref(self.page.empresa2, 'TruckPad')

        self.page.select_tipo_referencia(self.page.btn_add_tels_ref, self.page.tipo_ref3, 'Comercial')
        self.page.select_tipo_tel_ref(self.page.tipo_tel3, 'Celular')
        self.page.fill_ddd_ref(self.page.ddd3, '11')
        self.page.fill_tel_ref(self.page.tel3, '929217290')
        self.page.select_operadora_ref(self.page.operadora3, 'Oi')
        self.page.fill_nome_contato_ref(self.page.contato3, 'Franklin')
        self.page.fill_nome_empresa_ref(self.page.empresa3, 'TruckPad')

        self.page.select_tipo_referencia(self.page.btn_add_tels_ref, self.page.tipo_ref4, 'Comercial')
        self.page.select_tipo_tel_ref(self.page.tipo_tel4, 'Fixo')
        self.page.fill_ddd_ref(self.page.ddd4, '11')
        self.page.fill_tel_ref(self.page.tel4, '29217291')
        self.page.select_operadora_ref(self.page.operadora4, 'Oi')
        self.page.fill_nome_contato_ref(self.page.contato4, 'Aline Ueda')
        self.page.fill_nome_empresa_ref(self.page.empresa4, 'TruckPad')

    # Dados para pagamentos

    def preenche_dados_pagamento(self):
        self.page.btn_add_pagamento1 = '#form-driver > div:nth-child(3) > ' \
                                       'div > div > div > div > div > div > div > div > div > button'
        # self.page.btn_add_outros_pagamentos = '#form-driver > div:nth-child(3) > div > div >
        # div > div > div > div > div.ant-row-flex.ant-row-flex-end > div > div > button'
        self.page.nome1 = '.formGroup [name="info_bank[0].name"]'
        self.page.cpf1 = '.formGroup [name="info_bank[0].cpf"]'
        self.page.banco1 = '.formGroup [name="info_bank[0].bank"]'
        self.page.agencia1 = '.formGroup [name="info_bank[0].agency"]'
        self.page.conta1 = '.formGroup [name="info_bank[0].account"]'
        self.page.tipo_conta1 = '#form-driver > div:nth-child(3) > div > div > div > div > ' \
                                'div > div > div.ant-row > div.ant-row > div:nth-child(6) > div > select'

        self.page.fill_nome_pagamento(self.page.btn_add_pagamento1, self.page.nome1, 'Franklin Sousa')
        self.page.fill_cpf_pagamento(self.page.cpf1, '35267948802')
        self.page.fill_banco_pagamento(self.page.banco1, '123')
        self.page.fill_agencia_pagamento(self.page.agencia1, '1234')
        self.page.fill_conta_pagamento(self.page.conta1, '32133211')
        self.page.select_tipo_conta_pagamento(self.page.tipo_conta1, 'Corrente')

    # Dados pessoais

    def preenche_dados_pessoais(self):
        self.page.fill_nome_dp('Franklin Sousa')
        self.page.select_estado_civil_dp('Viúvo')
        self.page.fill_data_nasc_dp("13/04/1989")
        self.page.select_estado_nasc_dp('SP')
        self.page.select_cidade_nasc_dp('SÃO PAULO')
        self.page.fill_nome_mae_dp('Rafaela Nascimento')
        self.page.fill_nome_pai_dp('Milton Nascimento')
        self.page.fill_num_dependentes_dp('0')
        self.page.select_sexo_dp('Masculino')

    # Escolaridade

    def seleciona_escolaridade(self):
        self.page.select_escolaridade('Ensino médio completo')

    # Endereço

    def preenche_endereco(self):
        self.page.fill_cep_end('03918000')
        self.page.select_estado_end('SP')
        self.page.select_cidade_end('SÃO PAULO')
        self.page.fill_bairro_end('Vila Bancária')
        self.page.fill_logradouro_end('Rua 13 de Maio')
        self.page.fill_numero_end('4321')
        self.page.fill_complemento_end('Bloco B')
        self.page.fill_tempo_moradia_end("13/04/1989")
        self.page.select_moradia_propria('Sim')
