from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://tms.homolog.truckpad.com.br/entrar")

# metodos usados na tela de login


def preenche_email(email):
    driver.find_element_by_id('user_email').send_keys(email)


def preenche_senha(senha):
    driver.find_element_by_id('user_password').send_keys(senha)


def click_entrar():
    driver.find_element_by_css_selector('.form-group [name="commit"]').click()


def obtem_titulo_pagina_inicial():
    titulo = driver.find_element_by_css_selector(".page-title .pull-left").text
    return titulo

# metodos usados na tela de cargas


def btn_motoristas():
    try:
        wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '.collapse [href="https://tms2.homolog.truckpad.com.br/#/my-fleet"')))
    finally:
        driver.find_element_by_css_selector(
            '#menu-header-main [href="https://tms2.homolog.truckpad.com.br/#/my-fleet"]'
        ).click()

# metodos usados na tela de gerenciamento de frota


def btn_adicionar_motorista():
    driver.find_element_by_css_selector('#importAndAddDrivers [href="#/drivers/new"]').click()
    text_element = driver.find_element_by_css_selector('.ant-typography').text
    return text_element

# metodos para localizar campos e botoes do motorista


def fill_field(css_selector, dado):
    driver.find_element_by_css_selector(css_selector).send_keys(dado)


def fill_cpf(cpf):
    fill_field('.formGroup [name="documents.cpf.number"]', cpf)


def fill_cnpj(cnpj):
    fill_field('.formGroup [name="driver_office.documents.cnpj.number"]', cnpj)


def fill_rg(rg):
    fill_field('.formGroup [name="documents.rg.number"]', rg)


def fill_orgao_expedidor_rg(orgao):
    fill_field('.formGroup [name="documents.rg.dispatch_agency"]', orgao)


def select_estado_expedidor_rg(expedidor):
    combobox_element = driver.find_element_by_css_selector(
        '#form-driver > div:nth-child(1) > div > div > div > div > div > div:nth-child(2) > div:nth-child(1) > div > select'
    )
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(expedidor)


def fill_data_expedicao_rg(data):
    driver.find_element_by_css_selector('.ant-calendar-picker-input[name="documents.rg.issued_at"]').click()
    fill_field('.ant-calendar-input', data)
    driver.find_element_by_css_selector('.formGroup [name="documents.cnh.number"]').click()


# CNH


def fill_cnh(cnh):
    fill_field('.formGroup [name="documents.cnh.number"]', cnh)


def fill_categoria_cnh(categoria):
    fill_field('.formGroup [name="documents.cnh.category"]', categoria)


def fill_data_emissao_cnh(data):
    driver.find_element_by_css_selector(
        '.ant-calendar-picker-input.ant-input[name="documents.cnh.issue_date"]'
    ).click()
    fill_field('.ant-calendar-input[placeholder="Selecionar data"]', data)
    driver.find_element_by_css_selector('.formGroup [name="documents.cnh.dispatch_agency"]').click()


def fill_data_expiracao_cnh(data):
    driver.find_element_by_css_selector('.ant-calendar-picker-input[name="documents.cnh.expires_at"]').click()
    fill_field('.ant-calendar-input', data)
    driver.find_element_by_css_selector('.formGroup [name="documents.cnh.dispatch_agency"]').click()


def fill_orgao_expedidor_cnh(orgao):
    fill_field('.formGroup [name="documents.cnh.dispatch_agency"]', orgao)


def select_estado_expedidor_cnh(estado):
    combobox_element = driver.find_element_by_css_selector\
        ('#form-driver > div:nth-child(1) > div > div > div > div > div > div:nth-child(3) > div:nth-child(4) > div > select')
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(estado)


def select_cidade_emissao_cnh(cidade):
    try:
        # Espera que a lista de cidade seja carregada
        wait.until(expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR,
             '#form-driver > div:nth-child(1) > div > div > div > div > div > div:nth-child(3) > div:nth-child(5) > div > div > div > select'), "Selecione"))
    finally:
        # Para depois selecionar a cidade
        combobox_element = driver.find_element_by_css_selector(
            '#form-driver > div:nth-child(1) > div > div > div > div > div > div:nth-child(3) > div:nth-child(5) > div > div > div > select'
        )
        combobox = Select(combobox_element)
        combobox.select_by_visible_text(cidade)


def fill_data_primeira_cnh(data):
    driver.find_element_by_css_selector('.ant-calendar-picker-input[name="documents.cnh.first_issue_date"]').click()
    fill_field('.ant-calendar-input', data)
    driver.find_element_by_css_selector('.formGroup [name="documents.cnh.security_code"]').click()


def fill_cod_seguranca_cnh(codigo):
    fill_field('.formGroup [name="documents.cnh.security_code"]', codigo)


def fill_serial_cnh(serial):
    fill_field('.formGroup [name="documents.cnh.serial_number"]', serial)


# demais documentos


def fill_pis(pis):
    fill_field('.formGroup [name="documents.pis.number"]', pis)


def fill_rntrc(rntrc):
    fill_field('.formGroup [name="documents.rntrc.number"]', rntrc)
    # dúvida com o paulinha: essa classe no rntrc >> class="ant-calendar-picker-input ant-input"


def select_tipo_rntrc(rntrc):
    # combobox_element = driver.find_element_by_css_selector('.ant-select[name="documents.rntrc.category"]')
    combobox_element = driver.find_element_by_css_selector(
        '#form-driver > div:nth-child(1) > div > div > div > div > div > div:nth-child(4) > div:nth-child(3) > div > select'
    )
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(rntrc)


def fill_validade_rntrc(data):
    driver.find_element_by_css_selector('.ant-calendar-picker-input[name="documents.rntrc.expires_at"]').click()
    fill_field('.ant-calendar-input', data)
    driver.find_element_by_css_selector('.ant-input[name="documents.inss.number"]').click()


def fill_inss(inss):
    fill_field('.ant-input[name="documents.inss.number"]', inss)


# Contatos e-mail

def add_campo_email():
    driver.find_element_by_css_selector\
        ('#form-driver > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div > div > div > button').click()


def fill_email_form(email):
    add_campo_email()
    fill_field('.formGroup [name="contacts.email[0].address"]', email)


# contatos pessoais

def btn_adicionar_tel_cp(btn_css_selector):
    # '#form-driver > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div > div > button'
    driver.find_element_by_css_selector(btn_css_selector).click()


def fill_nome_contato_cp(btn_css_selector, css_selector, nome):
    btn_adicionar_tel_cp(btn_css_selector)
    fill_field(css_selector, nome)


def select_tipo_tel_cp(css_selector, tipo):
    combobox_element = driver.find_element_by_css_selector(css_selector)
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(tipo)


def fill_ddd_cp(css_selector, ddd):
    fill_field(css_selector, ddd)


def fill_tel_cp(css_selector, tel):
    fill_field(css_selector, tel)


def set_whatsapp(css_selector):
    driver.find_element_by_css_selector(css_selector).click()


def select_operadora_cp(css_selector, operadora):
    combobox_element = driver.find_element_by_css_selector(css_selector)
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(operadora)

# Contatos de referencia

def btn_adicionar_tel_ref(btn_css_selector):
    driver.find_element_by_css_selector(btn_css_selector).click()


def select_tipo_referencia(btn_css_selector, combo_css_selector, tipo_ref):
    btn_adicionar_tel_ref(btn_css_selector)
    combobox_element = driver.find_element_by_css_selector(combo_css_selector)
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(tipo_ref)


def select_tipo_tel_ref(tel_css_selector, tipo_tel):
    combobox_element = driver.find_element_by_css_selector(tel_css_selector)
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(tipo_tel)


def fill_ddd_ref(ddd_css_selector, ddd):
    driver.find_element_by_css_selector(ddd_css_selector).send_keys(ddd)


def fill_tel_ref(tel_css_selector, tel):
    driver.find_element_by_css_selector(tel_css_selector).send_keys(tel)


def select_operadora_ref(operadora_css_selector, operadora):
    combobox_element = driver.find_element_by_css_selector(operadora_css_selector)
    combobox = Select(combobox_element)
    combobox.select_by_visible_text(operadora)


def fill_nome_contato_ref(css_selector, nome):
    fill_field(css_selector, nome)


def fill_nome_empresa_ref(css_selector, empresa):
    fill_field(css_selector, empresa)