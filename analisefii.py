import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analisar_fundo(ticker):
    # 1. Coleta de dados (Yahoo Finance)
    print(f"A descarregar dados de {ticker}...")
    dados = yf.download(ticker, start="2024-01-01")

    # 2. Cálculo de Médias Móveis (SMA)
    dados['SMA_20'] = dados['Close'].rolling(window=20).mean()
    dados['SMA_50'] = dados['Close'].rolling(window=50).mean()

    # 3. Visualização
    plt.figure(figsize=(12, 6))
    sns.set_theme(style="darkgrid")
    
    plt.plot(dados['Close'], label='Preço de Fecho', color='black', alpha=0.6)
    plt.plot(dados['SMA_20'], label='Média 20 dias (Curta)', color='blue')
    plt.plot(dados['SMA_50'], label='Média 50 dias (Longa)', color='red')
    
    plt.title(f'Análise de Tendência - {ticker}')
    plt.legend()
    plt.savefig('grafico_mxrf11.png')

# Executar para o MXRF11
analisar_fundo("MXRF11.SA")
