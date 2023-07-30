from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api')

# funcionalidades
def crypto_data(coin):
    # Inserindo dados atuais da moeda
    link = f'https://api.coincap.io/v2/assets/{coin}'
    url = requests.get(link).json()

    data = url['data']
    
    nome = data['name']
    simbolo = data['symbol']
    rank = data['rank']
    preco = data['priceUsd']
    capitalizacao = data['marketCapUsd']
    fornecimento = data['supply']
    variacao_percentual_24h = data['changePercent24Hr']

    url_historico = requests.get(f"https://api.coincap.io/v2/assets/{coin}/history?interval=d1&limit=5").json()['data']
    list_historico = []
    for past_price in url_historico[:5]:
        list_historico.append(past_price['priceUsd'])
    
    resposta = {
        "nome": nome,
        "simbolo": simbolo,
        "rank": rank,
        "preco": preco, 
        "capitalização": capitalizacao,
        "fornecimento": fornecimento,
        "percentualVariado24h": variacao_percentual_24h,
        "historico": list_historico
    }

    return jsonify(resposta)

crypto_data("bitcoin")
crypto_data("ethereum")
crypto_data("polygon")
# rodar api
app.run()
