from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PageForm:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("https://tms.homolog.truckpad.com.br/entrar")

# metodos usados na tela de login

    def preenche_email(self, email):
        self.driver.find_element_by_id('user_email').send_keys(email)

    def preenche_senha(self, senha):
        self.driver.find_element_by_id('user_password').send_keys(senha)

    def click_entrar(self):
        self.driver.find_element_by_css_selector('.form-group [name="commit"]').click()

    def obtem_titulo_pagina_inicial(self):
        titulo = self.driver.find_element_by_css_selector(".page-title .pull-left").text
        return titulo

    # metodos usados na tela de cargas

    def btn_motoristas(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, '.collapse [href="https://tms2.homolog.truckpad.com.br/#/my-fleet"')))
        finally:
            self.driver.find_element_by_css_selector(
                '#menu-header-main [href="https://tms2.homolog.truckpad.com.br/#/my-fleet"]'
            ).click()

    # metodos usados na tela de gerenciamento de frota

    def btn_adicionar_motorista(self):
        self.driver.find_element_by_css_selector('#importAndAddDrivers [href="#/drivers/new"]').click()
        text_element = self.driver.find_element_by_css_selector('.ant-typography').text
        return text_element

    # metodos para localizar campos e botoes do motorista

    def fill_field(self, css_selector, dado):
        self.driver.find_element_by_css_selector(css_selector).send_keys(dado)

    def fill_cpf(self, cpf):
        self.fill_field('.formGroup [name="documents.cpf.number"]', cpf)

    def fill_cnpj(self, cnpj):
        self.fill_field('.formGroup [name="driver_office.documents.cnpj.number"]', cnpj)

    def fill_rg(self, rg):
        self.fill_field('.formGroup [name="documents.rg.number"]', rg)

    def fill_orgao_expedidor_rg(self, orgao):
        self.fill_field('.formGroup [name="documents.rg.dispatch_agency"]', orgao)

    def select_estado_expedidor_rg(self, expedidor):
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(1) > div > div > div > div > '
            'div > div:nth-child(2) > div:nth-child(1) > div > select'
        )
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(expedidor)

    def fill_data_expedicao_rg(self, data):
        self.driver.find_element_by_css_selector('.ant-calendar-picker-input[name="documents.rg.issued_at"]').click()
        self.fill_field('.ant-calendar-input', data)
        self.driver.find_element_by_css_selector('.formGroup [name="documents.cnh.number"]').click()

    # CNH

    def fill_cnh(self, cnh):
        self.fill_field('.formGroup [name="documents.cnh.number"]', cnh)

    def fill_categoria_cnh(self, categoria):
        self.fill_field('.formGroup [name="documents.cnh.category"]', categoria)

    def fill_data_emissao_cnh(self, data):
        self.driver.find_element_by_css_selector(
            '.ant-calendar-picker-input.ant-input[name="documents.cnh.issue_date"]'
        ).click()
        self.fill_field('.ant-calendar-input[placeholder="Selecionar data"]', data)
        self.driver.find_element_by_css_selector('.formGroup [name="documents.cnh.dispatch_agency"]').click()

    def fill_data_expiracao_cnh(self, data):
        self.driver.find_element_by_css_selector('.ant-calendar-picker-input[name="documents.cnh.expires_at"]').click()
        self.fill_field('.ant-calendar-input', data)
        self.driver.find_element_by_css_selector('.formGroup [name="documents.cnh.dispatch_agency"]').click()

    def fill_orgao_expedidor_cnh(self, orgao):
        self.fill_field('.formGroup [name="documents.cnh.dispatch_agency"]', orgao)

    def select_estado_expedidor_cnh(self, estado):
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(1) > div > div > div > div > '
            'div > div:nth-child(3) > div:nth-child(4) > div > select')
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(estado)

    def select_cidade_emissao_cnh(self, cidade):
        try:
            # Espera que a lista de cidade seja carregada
            self.wait.until(expected_conditions.text_to_be_present_in_element(
                (By.CSS_SELECTOR,
                 '#form-driver > div:nth-child(1) > div > div > div > div > div > '
                 'div:nth-child(3) > div:nth-child(5) > div > div > div > select'), "Selecione"))
        finally:
            # Para depois selecionar a cidade
            combobox_element = self.driver.find_element_by_css_selector(
                '#form-driver > div:nth-child(1) > div > div > div > div > div > '
                'div:nth-child(3) > div:nth-child(5) > div > div > div > select'
            )
            combobox = Select(combobox_element)
            combobox.select_by_visible_text(cidade)

    def fill_data_primeira_cnh(self, data):
        self.driver.find_element_by_css_selector(
            '.ant-calendar-picker-input[name="documents.cnh.first_issue_date"]').click()
        self.fill_field('.ant-calendar-input', data)
        self.driver.find_element_by_css_selector('.formGroup [name="documents.cnh.security_code"]').click()

    def fill_cod_seguranca_cnh(self, codigo):
        self.fill_field('.formGroup [name="documents.cnh.security_code"]', codigo)

    def fill_serial_cnh(self, serial):
        self.fill_field('.formGroup [name="documents.cnh.serial_number"]', serial)

    # demais documentos

    def fill_pis(self, pis):
        self.fill_field('.formGroup [name="documents.pis.number"]', pis)

    def fill_rntrc(self, rntrc):
        self.fill_field('.formGroup [name="documents.rntrc.number"]', rntrc)
        # dúvida com o paulinha: essa classe no rntrc >> class="ant-calendar-picker-input ant-input"

    def select_tipo_rntrc(self, rntrc):
        # combobox_element = driver.find_element_by_css_selector('.ant-select[name="documents.rntrc.category"]')
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(1) > div > div > div > div > '
            'div > div:nth-child(4) > div:nth-child(3) > div > select'
        )
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(rntrc)

    def fill_validade_rntrc(self, data):
        self.driver.find_element_by_css_selector(
            '.ant-calendar-picker-input[name="documents.rntrc.expires_at"]').click()
        self.fill_field('.ant-calendar-input', data)
        self.driver.find_element_by_css_selector(
            '.ant-input[name="documents.inss.number"]').click()

    def fill_inss(self, inss):
        self.fill_field('.ant-input[name="documents.inss.number"]', inss)

    # Contatos e-mail

    def add_campo_email(self):
        self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(2) > div > div:nth-child(1) > '
            'div > div > div > div > div > div > div > button').click()

    def fill_email_form(self, email):
        self.add_campo_email()
        self.fill_field('.formGroup [name="contacts.email[0].address"]', email)

    # contatos pessoais

    def btn_adicionar_tel_cp(self, btn_css_selector):
        # '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div > div > button'
        self.driver.find_element_by_css_selector(btn_css_selector).click()

    def fill_nome_contato_cp(self, btn_css_selector, css_selector, nome):
        self.btn_adicionar_tel_cp(btn_css_selector)
        self.fill_field(css_selector, nome)

    def select_tipo_tel_cp(self, css_selector, tipo):
        combobox_element = self.driver.find_element_by_css_selector(css_selector)
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(tipo)

    def fill_ddd_cp(self, css_selector, ddd):
        self.fill_field(css_selector, ddd)

    def fill_tel_cp(self, css_selector, tel):
        self.fill_field(css_selector, tel)

    def set_whatsapp(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).click()

    def select_operadora_cp(self, css_selector, operadora):
        combobox_element = self.driver.find_element_by_css_selector(css_selector)
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(operadora)

    # Contatos de referencia

    def btn_adicionar_tel_ref(self, btn_css_selector):
        self.driver.find_element_by_css_selector(btn_css_selector).click()

    def select_tipo_referencia(self, btn_css_selector, combo_css_selector, tipo_ref):
        self.btn_adicionar_tel_ref(btn_css_selector)
        combobox_element = self.driver.find_element_by_css_selector(combo_css_selector)
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(tipo_ref)

    def select_tipo_tel_ref(self, tel_css_selector, tipo_tel):
        combobox_element = self.driver.find_element_by_css_selector(tel_css_selector)
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(tipo_tel)

    def fill_ddd_ref(self, ddd_css_selector, ddd):
        self.driver.find_element_by_css_selector(ddd_css_selector).send_keys(ddd)

    def fill_tel_ref(self, tel_css_selector, tel):
        self.driver.find_element_by_css_selector(tel_css_selector).send_keys(tel)

    def select_operadora_ref(self, operadora_css_selector, operadora):
        combobox_element = self.driver.find_element_by_css_selector(operadora_css_selector)
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(operadora)

    def fill_nome_contato_ref(self, css_selector, nome):
        self.fill_field(css_selector, nome)

    def fill_nome_empresa_ref(self, css_selector, empresa):
        self.fill_field(css_selector, empresa)

    # Dados para pagamentos

    def btn_add_pagamento(self, btn_css_selector):
        self.driver.find_element_by_css_selector(btn_css_selector).click()

    def fill_nome_pagamento(self, btn_css_selector, nome_css_selector, nome):
        self.btn_add_pagamento(btn_css_selector)
        self.fill_field(nome_css_selector, nome)

    def fill_cpf_pagamento(self, cpf_css_selector, cpf):
        self.fill_field(cpf_css_selector, cpf)

    def fill_banco_pagamento(self, banco_css_selector, banco):
        self.fill_field(banco_css_selector, banco)

    def fill_agencia_pagamento(self, agencia_css_selector, agencia):
        self.fill_field(agencia_css_selector, agencia)

    def fill_conta_pagamento(self, conta_css_selector, conta):
        self.fill_field(conta_css_selector, conta)

    def select_tipo_conta_pagamento(self, tipo_conta_css_selector, tipo):
        combobox_element = self.driver.find_element_by_css_selector(tipo_conta_css_selector)
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(tipo)

    # Dados pessoais

    def fill_nome_dp(self, nome):
        self.driver.find_element_by_css_selector('.formGroup [name="name"]').send_keys(nome)

    def select_estado_civil_dp(self, situacao):
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(4) > div > div > div > div > div > div > div:nth-child(2) > div > select')
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(situacao)

    def fill_data_nasc_dp(self, data):
        self.driver.find_element_by_css_selector('.formGroup [name="personal_info.birth_date"]').click()
        self.fill_field('.ant-calendar-input[placeholder="Selecionar data"]', data)
        self.driver.find_element_by_css_selector('.formGroup [name="name"]').click()

    def select_estado_nasc_dp(self, estado):
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(4) > div > div > div > div > div > div > div:nth-child(4) > div > select')
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(estado)

    def select_cidade_nasc_dp(self, cidade):
        try:
            self.wait.until(expected_conditions.text_to_be_present_in_element(
                (By.CSS_SELECTOR,
                 '#form-driver > div:nth-child(4) > div > div > div > div > '
                 'div > div > div:nth-child(5) > div > div > div > select'),
                "Selecione"))
        finally:
            combobox_element = self.driver.find_element_by_css_selector(
                '#form-driver > div:nth-child(4) > div > div > div > div '
                '> div > div > div:nth-child(5) > div > div > div > select')
            combobox = Select(combobox_element)
            combobox.select_by_visible_text(cidade)

    def fill_nome_mae_dp(self, mae):
        self.fill_field('.formGroup [name="personal_info.mother_name"]', mae)

    def fill_nome_pai_dp(self, pai):
        self.fill_field('.formGroup [name="personal_info.father_name"]', pai)

    def fill_num_dependentes_dp(self, num):
        self.fill_field('.formGroup [name="personal_info.number_of_dependents"]', num)

    def select_sexo_dp(self, sexo):
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(4) > div > div > div > div > div > div > div:nth-child(9) > div > select')
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(sexo)

    # Escolaridade

    def select_escolaridade(self, escolaridade):
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(5) > div > div > div > div > div > div > div > div > select')
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(escolaridade)

    # Dados de Endereço

    def fill_cep_end(self, cep):
        self.fill_field('.formGroup [name="addresses[0].postal_code"]', cep)

    def select_estado_end(self, estado):
        combobox_element = self.driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(6) > div > div > div > div > div > div > div:nth-child(2) > div > select')
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(estado)

    def select_cidade_end(self, cidade):
        try:
            self.wait.until(expected_conditions.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#form-driver > div:nth-child(6) > div > div > div > '
                                  'div > div > div > div:nth-child(3) > div > div > div > select'),
                "Selecione"))
        finally:
            combobox_element = self.driver.find_element_by_css_selector(
                '#form-driver > div:nth-child(6) > div > div > div > div > '
                'div > div > div:nth-child(3) > div > div > div > select')
            combobox = Select(combobox_element)
            combobox.select_by_visible_text(cidade)

    def fill_bairro_end(self, bairro):
        self.fill_field('.formGroup [name="addresses[0].neighborhood"]', bairro)

    def fill_logradouro_end(self, logradouro):
        self.fill_field('.formGroup [name="addresses[0].street_name"]', logradouro)

    def fill_numero_end(self, num):
        self.fill_field('.formGroup [name="addresses[0].street_number"]', num)

    def fill_complemento_end(self, complemento):
        self.fill_field('.formGroup [name="addresses[0].complement"]', complemento)

    def fill_tempo_moradia_end(self, data):
        self.driver.find_element_by_css_selector('.formGroup [name="addresses[0].residence_time"]').click()
        self.fill_field('.ant-calendar-input', data)
        self.driver.find_element_by_css_selector('.formGroup [name="addresses[0].complement"]').click()

    def select_moradia_propria(self, resposta):
        combobox_element = self.driver.find_element_by_css_selector('.formGroup [name="addresses[0].own_residence"]')
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(resposta)

    # Gerenciadora de risco
