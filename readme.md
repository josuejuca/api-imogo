# FastAPI para Gerenciamento de Imóveis

## Instalação

1. Clone o repositório.
2. Crie um ambiente virtual e ative-o.
3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
4. Configure o arquivo `database.py` com as credenciais corretas do MySQL.

## Execução

1. Execute a aplicação:
    ```
    uvicorn main:app --reload
    ```
2. Acesse a documentação interativa:
    ```
    http://127.0.0.1:8000/docs
    ```

## Estrutura do Projeto

- `main.py`: Arquivo principal com a configuração da API.
- `models.py`: Definição dos modelos do banco de dados.
- `schemas.py`: Definição dos esquemas Pydantic.
- `crud.py`: Funções CRUD.
- `database.py`: Configuração do banco de dados.

# F

- Cadastro ( Criar cadastro do usuario no banco MySQL) 
- CEP 
- Upload de docs 
- api Serpro ( pensar como implementar ela )
- E-mails (fluxo)
- Cadastro do imovel
- Gestão pelo painel
- Integração 

# Modelagem do banco de dados MySQl

### usuario:
- id (pk)
- data de criação 
- status 
- tipo de usuario
- nome 
- email
- telefone 
- foto_perfil 
- origin
- cnh
- rg 
- data de nascimento 
- nome da mae 
- nome do pai 
- cpf
- foto_cnh
- foto_qrcode
- foto_pessoal 
- 
