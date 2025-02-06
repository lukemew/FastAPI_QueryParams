---

# 🌍 API de Países e Capitais

Uma API simples desenvolvida em **FastAPI** para explorar informações sobre países, suas capitais, população e continentes. O objetivo deste projeto é praticar o uso de **Path Parameters** e **Query Parameters** em APIs RESTful.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.85.0-green)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)
[![Author](https://img.shields.io/badge/Author-lukemew-brightgreen)](https://github.com/lukemew)

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/lukemew/api-paises.git
   cd api-paises
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a API:
   ```bash
   uvicorn main:app --reload
   ```

4. Acesse a API:
   - **URL base**: `http://127.0.0.1:8000`
   - **Documentação interativa**: `http://127.0.0.1:8000/docs`

---

## 🛠️ Funcionalidades

### 1. Consultar informações de um país
- **Método**: `GET`
- **Endpoint**: `/country/{country_name}`
- **Exemplo**:
  ```bash
  GET /country/brazil
  ```
  **Resposta**:
  ```json
  {
    "country_name": "Brazil",
    "capital": "Brasília",
    "population": 213000000,
    "continent": "South America"
  }
  ```

### 2. Filtrar países por continente
- **Método**: `GET`
- **Endpoint**: `/countries/`
- **Query Parameter**: `continent` (opcional)
- **Exemplo**:
  ```bash
  GET /countries/?continent=south_america
  ```
  **Resposta**:
  ```json
  [
    {
      "country_name": "Brazil",
      "capital": "Brasília",
      "population": 213000000,
      "continent": "South America"
    },
    {
      "country_name": "Argentina",
      "capital": "Buenos Aires",
      "population": 45195777,
      "continent": "South America"
    }
  ]
  ```

### 3. Adicionar um novo país
- **Método**: `POST`
- **Endpoint**: `/country/{country_name}`
- **Exemplo**:
  ```bash
  POST /country/japan
  Content-Type: application/json

  {
    "capital": "Tokyo",
    "population": 125800000,
    "continent": "Asia"
  }
  ```
  **Resposta**:
  ```json
  {
    "message": "País adicionado com sucesso!",
    "country_name": "Japan"
  }
  ```

---

## 📂 Estrutura do Projeto

```
api-paises/
├── main.py               # Código principal da API
├── requirements.txt      # Dependências do projeto
├── README.md             # Este arquivo
```

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com ❤️ por [lukemew](https://github.com/lukemew).

---

### Intuito do Projeto

Este projeto foi criado para:
- Praticar o uso de **Path Parameters** e **Query Parameters** em APIs RESTful.
- Demonstrar como criar uma API simples com **FastAPI**.
- Servir como exemplo para quem está aprendendo a desenvolver APIs em Python.

---
