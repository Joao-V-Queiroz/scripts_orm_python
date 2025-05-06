import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

engine = sa.create_engine("sqlite:///BD//venda.db")  # Conexão com o banco de dados
base = sa_orm.declarative_base() # Base de dados

# Tabela cliente
class Cliente(base): 
	__tablename__ = "clientes" # Nome da tabela
	
	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID do cliente
	cpf = sa.Column(sa.CHAR(14), unique=True) # CPF do cliente
	nome = sa.Column(sa.VARCHAR(100), nullable=False) # Nome do cliente
	email = sa.Column(sa.VARCHAR(100), nullable=False, unique=True) # Email do cliente
	genero = sa.Column(sa.CHAR(1)) # Gênero do cliente
	salario = sa.Column(sa.DECIMAL(10, 2)) # Salário do cliente
	dia_mes_aniversario = sa.Column(sa.CHAR(5)) # Dia e mês de aniversário do cliente
	bairro = sa.Column(sa.VARCHAR(50)) # Bairro do cliente
	cidade = sa.Column(sa.VARCHAR(50)) # Cidade do cliente
	uf = sa.Column(sa.CHAR(2)) # UF do cliente

#tabela Fornecedor
class Fornecedor(base):
	__tablename__ = "fornecedores" 

	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID do fornecedor
	nome_fantasia = sa.Column(sa.VARCHAR(50), nullable=False) # Nome fantasia do fornecedor
	razao_social = sa.Column(sa.VARCHAR(100), nullable=False) # Razão social do fornecedor
	cidade = sa.Column(sa.VARCHAR(50), nullable=False) # Cidade do fornecedor
	uf = sa.Column(sa.CHAR(2), nullable=False) # UF do fornecedor

#tabela Produto
class Produto(base):
	__tablename__ = "produtos"

	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID do produto
	id_fornecedor = sa.Column(sa.INTEGER, sa.ForeignKey("fornecedores.id", ondelete="NO ACTION", onupdate="CASCADE")) # ID do fornecedor do produto
	codBarras = sa.Column(sa.CHAR(13), unique=True) # Código de barras do produto	
	descricao = sa.Column(sa.VARCHAR(100), nullable=False) # Descrição do produto
	genero = sa.Column(sa.CHAR(1), nullable=False) # Gênero do produto

#tabela Vendedor 
class Vendedor(base):
	__tablename__ = "vendedores"

	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID do vendedor
	cpf = sa.Column(sa.VARCHAR(14), unique=True, nullable=False) # CPF do vendedor
	nome = sa.Column(sa.VARCHAR(100), nullable=False) # Nome do vendedor
	email = sa.Column(sa.VARCHAR(50), nullable=False, unique=True) # Email do vendedor
	genero = sa.Column(sa.CHAR(1)) # Gênero do vendedor

#tabela Venda
class Venda(base):
	__tablename__ = "vendas"

	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID da venda
	id_cliente = sa.Column(sa.INTEGER, sa.ForeignKey("clientes.id", ondelete="NO ACTION", onupdate="CASCADE")) # ID do cliente da venda
	id_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey("vendedores.id", ondelete="NO ACTION", onupdate="CASCADE")) # ID do vendedor da venda
	id_produto = sa.Column(sa.INTEGER, sa.ForeignKey("produtos.id", ondelete="NO ACTION", onupdate="CASCADE")) # ID do produto da venda

try: 
	base.metadata.create_all(engine) # Criação das tabelas no banco de dados
	print("Tabelas criadas com sucesso.")
except sa.exc.OperationalError:
	print("Erro ao criar as tabelas no banco de dados. Verifique se o banco de dados está acessível.")
