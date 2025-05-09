import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
import vendas as vd

# Caminho dos arquivos
endereco = "C:\\Users\\joaov\\OneDrive\\Documentos\\pucrs_pos_fullstack\\Banco de Dados Relacional\\Dados\\Exemplo\\"

# Lê os dados do CSV de vendedores
vendedor = pd.read_csv(endereco + "vendedor.csv", sep=";", encoding="latin1")
tbVendedor = pd.DataFrame(vendedor)

# Conexão com o banco SQLite
engine = sa.create_engine("sqlite:///BD/venda.db")
Session = sa_orm.sessionmaker(bind=engine)
session = Session()

try:
    # Inserindo os dados na tabela Vendedores apenas se o ID ainda não existir
    for i in range(len(tbVendedor)):
        id_vendedor = int(tbVendedor["registro_vendedor"][i])
        vendedor_existente = session.get(vd.Vendedor, id_vendedor)

        if vendedor_existente:
            print(f"Vendedor com ID {id_vendedor} já existe. Ignorando inserção.")
            continue

        dadosVendedor = vd.Vendedor(
            id=id_vendedor,
            cpf=tbVendedor["cpf"][i],
            nome=tbVendedor["nome"][i],
            genero=tbVendedor["genero"][i],
            email=tbVendedor["email"][i],
        )
        session.add(dadosVendedor)

    session.commit()
    print("Dados de vendedores inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao inserir dados de vendedores: {e}")
    
# Inserindo os dados na tabela Fornecedores
try:
    fornecedor = pd.read_excel(endereco + "fornecedor.xlsx")
    tbFornecedor = pd.DataFrame(fornecedor)

    dadosFornecedor = tbFornecedor.to_dict(orient="records")

    metaData = sa.MetaData()
    tabelaFornecedores = sa.Table(vd.Fornecedor.__tablename__, metaData, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(tabelaFornecedores.insert(), dadosFornecedor)
        conn.commit()

    print("Dados de fornecedores inseridos com sucesso!")
except FileNotFoundError:
    print("Arquivo fornecedor.xlsx não encontrado. Verifique o caminho do arquivo.")
    
except Exception as e:
    print(f"Erro ao inserir dados de produtos: {e}")

# Inserindo os dados na tabela Produtos
try:
    produto = pd.read_excel(endereco + "produto.xlsx")
    tbProdutos = pd.DataFrame(produto)

    dadosProdutos = tbProdutos.to_dict(orient="records")

    metaData = sa.MetaData()
    tabelaProdutos = sa.Table(vd.Produto.__tablename__, metaData, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(tabelaProdutos.insert(), dadosProdutos)
        conn.commit()

    print("Dados de produtos inseridos com sucesso!")

except FileNotFoundError:
    print("Arquivo produtos.xlsx não encontrado. Verifique o caminho do arquivo.")

except Exception as e:
    print(f"Erro ao inserir dados de produtos: {e}")

finally:
    session.close()
    engine.dispose()
    print("Conexão fechada.")
