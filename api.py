from flask import Flask
import pandas as pd

app = Flask(__name__) # cria o site
tabela = pd.read_excel("Vendas - Dez.xlsx")

@app.route("/") # decorator -> diz em qual link a função vai rodar
def fat(): # função
    faturamento = float(tabela["Valor Final"].sum())
    return {"faturamento": faturamento}

@app.route("/vendas/produtos") 
def vendas_produtos(): 
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_vendas_produtos

@app.route("/vendas/produtos/<produto>") 
def fat_produto(produto): 
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    if produto in tabela_vendas_produtos.index:
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produto.to_dict()
        return dic_vendas_produto
    else:
        return {produto: "Inexistente"}
@app.route("/vendas/lojasVenda")
def lojas_venda():
    tabela_vendas_lojas = tabela[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
    dic_vendas_lojas = tabela_vendas_lojas.to_dict()
    return dic_vendas_lojas
@app.route("/vendas/<loja>")
def loja_venda(loja):
    tabela_venda_loja = tabela[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
    if loja in tabela_venda_loja.index:
        venda_loja = tabela_venda_loja.loc[loja]
        dic_venda_loja = venda_loja.to_dict()
        return dic_venda_loja
        
app.run() # no replit use app.run(host="0.0.0.0") # coloca o site no ar