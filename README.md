# Sistema de Gerenciamento de Tarefas

![Badge](https://img.shields.io/badge/status-active-brightgreen)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

**Under Development**

Este projeto é um sistema de gerenciamento de tarefas (To-Do List) desenvolvido com Flask, uma biblioteca web leve para Python. O sistema permite que os usuários criem, leiam, atualizem e excluam tarefas, com uma interface web para interagir com o sistema. O projeto também inclui autenticação de usuários, uma funcionalidade crucial para gerenciar e proteger dados pessoais.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
- [Configuração](#configuração)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Instalação

### Pré-requisitos

- [Python 3.9+](https://www.python.org/downloads/)
- [Conda](https://docs.conda.io/en/latest/miniconda.html) (ou [pip](https://pip.pypa.io/en/stable/))

### Configuração do Ambiente

1. **Clone o Repositório**

   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um Ambiente Virtual**

   Usando `conda`:

   ```sh
   conda create --name task_manager python=3.9
   conda activate task_manager
   ```

   Ou usando `venv`:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. **Instale as Dependências**

   ```sh
   pip install -r requirements.txt
   ```

   Se estiver usando `conda`, você pode instalar pacotes individualmente se necessário.

## Uso

1. **Inicie o Servidor**

   Com o ambiente ativado, execute:

   ```sh
   flask run
   ```

   Ou, se estiver usando um script de execução:

   ```sh
   python run.py
   ```

2. **Acesse a Aplicação**

   Abra seu navegador e vá para [http://127.0.0.1:5000](http://127.0.0.1:5000) para acessar a interface web.

3. **Funcionalidades**

   - **Página Inicial**: Visualize suas tarefas.
   - **Registrar**: Crie uma nova conta de usuário.
   - **Login**: Faça login para acessar suas tarefas.
   - **Gerenciar Tarefas**: Adicione, edite ou exclua tarefas.

## Configuração

### Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto para armazenar variáveis de ambiente sensíveis, como a chave secreta e URL do banco de dados.

Exemplo:

```env
SECRET_KEY=sua-chave-secreta
DATABASE_URL=sqlite:///site.db
```

### Configuração do Banco de Dados

O banco de dados será criado automaticamente na primeira execução. Se necessário, você pode configurar a URL do banco de dados no arquivo `config.py`.

## Contribuição

1. **Faça um Fork do Repositório**

   Clique no botão "Fork" no canto superior direito do repositório.

2. **Clone o Fork**

   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

3. **Crie uma Nova Branch**

   ```sh
   git checkout -b minha-nova-funcionalidade
   ```

4. **Faça suas Alterações e Commits**

   ```sh
   git add .
   git commit -m "Adiciona nova funcionalidade"
   ```

5. **Envie suas Alterações para o GitHub**

   ```sh
   git push origin minha-nova-funcionalidade
   ```

6. **Crie um Pull Request**

   Vá até o repositório original e clique em "New Pull Request".

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
