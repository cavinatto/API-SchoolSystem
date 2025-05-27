# 📝 API de Atividades

Este repositório contém a **API de Atividades**, desenvolvida com **Flask**, **SQLAlchemy** e **SQLite**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Atividades é um **microsserviço** que faz parte de um sistema maior de gestão escolar, sendo responsável exclusivamente pelo gerenciamento de **atividades associadas a professores**.

⚠️ **Esta API depende da sua API Principal de Gestão Escolar**, que deve estar em execução localmente ou em ambiente acessível. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se o **professor existe** (`GET /api/professores/<id>`)

---

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- Flask  
- SQLAlchemy  
- SQLite (como banco de dados local)  
- Requests (para consumo da API de professores)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone -b Atividades https://github.com/cavinatto/API-SchoolSystem.git
cd API_atividades
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5002`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /atividades` – Lista todas as atividades
- `GET /atividades/<id>` – Retorna detalhes de uma atividade
- `GET /atividades/<id_atividade>/professor/<id_professor>` – Retorna a atividade com verificação de associação do professor
- `POST /atividades` – Cria uma nova atividade

### Exemplo de corpo JSON para criação:

```json
{
  "id_atividade": 3,
  "id_professor": 1,
  "enunciado": "Explique o ciclo de vida de um software.",
  "resposta": "Requisitos > Projeto > Implementação > Testes > Deploy"
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://localhost:8000
```

A criação de uma atividade depende da verificação do id_professor nesse serviço.

---

## 📦 Estrutura do Projeto

```
atividade_service/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── controllers/
│   └── atividade_controller.py
│
├── models/
│   └── atividade_model.py
│
├── clients/
│   └── professor_service_client.py
│
├── instance/
│   └── atividades.db
```
