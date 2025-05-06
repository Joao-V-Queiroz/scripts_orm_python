import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
import vendas as vd

endereco = "C:\\Users\\joaov\\OneDrive\\Documentos\\pucrs_pos_fullstack\\Banco de Dados Relacional\\Dados\\Exemplo\\"
vendedor = pd.read_csv(endereco + "vendedor.csv", sep=";", encoding="latin1")  # Lê o arquivo CSV

tbVendedor = pd.DataFrame(vendedor)  # Cria um DataFrame a partir do arquivo CSV
engine = sa.create_engine("sqlite:///BD//venda.db")  # Conexão com o banco de dados
Session = sa_orm.sessionmaker(bind=engine)
session = Session()  # Cria uma sessão para o banco de dados

try:
    for i in range(len(tbVendedor)):  # Para cada linha do DataFrame
        dadosVendedor = vd.Vendedor(
            id=int(tbVendedor["registro_vendedor"][i]),
            cpf=tbVendedor["cpf"][i],
            nome=tbVendedor["nome"][i],
            genero=tbVendedor["genero"][i],
            email=tbVendedor["email"][i],
        )
        session.add(dadosVendedor)  # Adiciona os dados à sessão

    session.commit()  # Comita todos os dados de uma vez
    print("Dados inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao inserir dados: {e}")

finally:
    session.close()
    engine.dispose()
    print("Conexão fechada.")
