# 📈 Coletor de Dados de Ações (Python + Selenium)

Este projeto é uma automação em Python que coleta dados de ações da bolsa brasileira diretamente do site [Investidor10](https://investidor10.com.br), utilizando Selenium para web scraping e salvando os resultados em um arquivo `.csv`.

## 🚀 Funcionalidades

- Acessa automaticamente páginas de ações como `ALUP11`, `BBAS3`, `WEGE3`, entre outras.
- Extrai informações como:
  - Ação
  - Cotação
  - Variação nos últimos 12 meses (%)
  - P/L (Preço/Lucro)
  - P/VP (Preço/Valor Patrimonial)
  - DY% (Dividend Yield)
  - Margem líquida (%)
  - Lucro líquido últimos 12 meses
  - Lucros líquidos de 2021 a 2024
- Salva todos os dados organizados em um arquivo `dados_acoes.csv`.

## 💡 Motivação

A ideia desse projeto surgiu de um pedido do meu pai. Ele precisava coletar diversas informações financeiras do site *Investidor10* e organizá-las em uma tabela — tarefa que ele vinha fazendo manualmente, o que consumia bastante tempo.

Ele tentou usar várias inteligências artificiais (como o ChatGPT, Gemini e Claude) pra automatizar o processo, mas nenhuma conseguiu montar a tabela completa com todos os dados que ele precisava. Foi aí que ele me lançou o desafio: *“Então vê se você consegue fazer isso melhor!”*

Topado o desafio, encarei o problema de frente. Como o site bloqueia bots comuns, optei por usar o Selenium para simular um usuário real navegando nas páginas. E deu certo! Consegui extrair todas as informações desejadas e automatizar completamente o processo, entregando uma solução funcional, rápida e personalizada — e, de quebra, fiz meu pai economizar um bom tempo no dia a dia. 🚀

## 🛠️ Tecnologias Utilizadas

- Python 3
- Selenium
- WebDriver Manager
- Biblioteca `csv`
- Tkinter (interface futura)

## 🧪 Como Usar

1. Instale as dependências:
```bash
pip install selenium webdriver-manager
