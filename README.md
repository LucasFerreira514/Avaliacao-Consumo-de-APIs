# Cotações de Moedas para Real Brasileiro

Este é um pequeno script em Python que busca as cotações de moedas em relação ao Real Brasileiro (BRL). Ele utiliza a API da AwesomeAPI para obter os dados. Você pode personalizar as moedas desejadas substituindo `:moedas` no URL.

## Como Usar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório para o seu ambiente local.
3. Execute o script `cotacoes.py`.

## Exemplo de Uso

```python
import requests

# Substitua ':moedas' pelas moedas desejadas
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'

resposta = requests.get(url)
cotacoes = resposta.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_bitcoin = cotacoes['BTCBRL']['bid']

print('Cotações de Moedas para Real Brasileiro'.center(50))
print(f'Dólar Americano: R${float(cotacao_dolar):.2f}')
print(f'Euro: R${float(cotacao_euro):.2f}')
print(f'BitCoin: R${float(cotacao_bitcoin):.2f}')
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções neste projeto. Basta abrir uma **issue** ou enviar um **pull request**.