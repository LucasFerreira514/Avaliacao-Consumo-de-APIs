import requests

# Substitua ':moedas' pelas moedas desejadas
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # Levanta uma exceção para respostas de erro
    cotacoes = resposta.json()
    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_bitcoin = cotacoes['BTCBRL']['bid']

    print('=' * 50)
    print('Cotações de Moedas para Real Brasileiro'.center(50))
    print('-' * 50)
    print(f'Dólar Americano: R${float(cotacao_dolar):.2f}')
    print(f'Euro: R${float(cotacao_euro):.2f}')
    print(f'BitCoin: R${float(cotacao_bitcoin):.2f}')
    print('=' * 50)
except requests.exceptions.HTTPError as errh:
    print(f'Erro HTTP: {errh}')
except requests.exceptions.ConnectionError as errc:
    print(f'Erro de Conexão: {errc}')
except requests.exceptions.Timeout as errt:
    print(f'Tempo de resposta excedido: {errt}')
except requests.exceptions.RequestException as err:
    print(f'Erro na requisição: {err}')
