import csv
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

acoes = [
    "ALUP11", "BBAS3", "BBSE3", "BPAC11", "CMIG4", "CPFE3", "CPLE6", "CSMG3",
    "CURY3", "DIRR3", "EMBR3", "EQTL3", "GEPA4", "ITSA4", "ITUB4",
    "MDNE3", "SAPR11", "SBSP3", "STBP3", "TAEE11", "TGMA3", "TIMS3",
    "VULC3", "WEGE3", "LAVV3", "PLPL3", "ABCB4"
]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

dados_gerais = []

for acao in acoes:
    url = f'https://investidor10.com.br/acoes/{acao.lower()}/'
    print(f'\n🔎 Acessando: {url}')

    try:
        driver.get(url)
        time.sleep(2)  

       
        cotacao = driver.find_element(By.CLASS_NAME, 'value').text
        variacao = driver.find_element(By.CSS_SELECTOR, '._card.pl ._card-body > div > span').text
        pl = driver.find_element(By.CSS_SELECTOR, '._card.val ._card-body > span').text
        vp = driver.find_element(By.CSS_SELECTOR, '._card.vp ._card-body > span').text
        dy = driver.find_element(By.CSS_SELECTOR, '._card.dy ._card-body > span').text
        margem_liq = driver.find_element(By.CSS_SELECTOR, '#table-balance-results tr:nth-of-type(13) td:nth-of-type(2)').text
        lucro_12m = driver.find_element(By.CSS_SELECTOR, '#table-balance-results tr:nth-of-type(5) td:nth-of-type(2) .simple-value').text
        lucro_liq24 = driver.find_element(By.CSS_SELECTOR, '#table-balance-results tr:nth-of-type(5) td:nth-of-type(3) .simple-value').text
        lucro_liq23 = driver.find_element(By.CSS_SELECTOR, '#table-balance-results tr:nth-of-type(5) td:nth-of-type(5) .simple-value').text
        lucro_liq22 = driver.find_element(By.CSS_SELECTOR, '#table-balance-results tr:nth-of-type(5) td:nth-of-type(8) .simple-value').text
        lucro_liq21 = driver.find_element(By.CSS_SELECTOR, '#table-balance-results tr:nth-of-type(5) td:nth-of-type(11) .simple-value').text

        dados_gerais.append({
            'Ação': acao,
            'Cotação': cotacao,
            'Variação': variacao,
            'P/L': pl,
            'VP': vp,
            'DY': dy,
            'Margem Líquida': margem_liq,
            'lucro 12 Meses': lucro_12m,
            'Lucro Líquido 2024': lucro_liq24,
            'Lucro Líquido 2023': lucro_liq23,
            'Lucro Líquido 2022': lucro_liq22,
            'Lucro Líquido 2021': lucro_liq21,
        })
        print(f'✅ {acao}: Dados coletados com sucesso.')

    except Exception as e:
        print(f'❌ {acao}: Erro ao buscar dados - {e}')

driver.quit()

with open('dados_acoes.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    campos = dados_gerais[0].keys() 
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(dados_gerais)

print('\n📁 Arquivo "dados_acoes.csv" gerado com sucesso!')
