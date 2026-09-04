# QA Banking – Educational Banking Platform with Automated API Tests

This repository contains a **full-featured banking system** built on a microservice architecture (REST + gRPC), along with a comprehensive **suite of automated API tests** written in Python using `pytest`, `Allure`, `Pydantic`, `Faker`, `HTTPX`, and `gRPC`.

The project is designed for learning and practicing API automation.

---

## Repository Structure

- `services/` – Microservices (accounts, cards, documents, gateway, mock, operations, payments, users).  
- `protos/` – gRPC contracts (`.proto` files) and generated Python code.  
- `libs/` – Shared libraries for database, Kafka, Redis, S3, gRPC/HTTP clients, and utilities.  
- `migrations/` – SQL migrations for PostgreSQL.  
- `monitoring/` – Prometheus configuration.  
- `scripts/` – Helper scripts (migrations, protobuf generation, etc.).  
- `tests/` – **Automated test suite** (see details below).  
- `docker-compose.yaml` – Orchestrates the entire infrastructure.  
- `config.py` – Global application configuration.  
- `pytest.ini` – Pytest settings.  
- `requirements.txt` – Python dependencies (shared by the app and tests).

### `tests/` Folder Breakdown

- `assertions/` – Custom assertions for gRPC and HTTP responses.  
- `clients/` – API clients (gRPC gateway clients, HTTP gateway clients).  
- `fixtures/` – Pytest fixtures for data preparation and client creation.  
- `schema/` – Pydantic models for request/response validation.  
- `suites/` – Actual test cases (integration tests, grouped by service and protocol).  
- `tools/` – Utilities (Allure helpers, configuration, data factories, logging).  
- `types/` – Common type definitions (enums).  
- `conftest.py` – Global fixtures.

---

## Running the Banking System

The tests require the system to be up and running. All services are containerised with Docker Compose.

### Prerequisites

- Docker & Docker Compose  
- Python 3.12+ (for running tests locally)  
- Allure CLI (optional, for viewing reports)

### Clone & Start

```bash
git clone https://github.com/V1aj3ro/qa-banking.git
cd qa-banking
```
# Start all services in detached mode
```bash
docker build -f Dockerfile.base -t base-service .
docker compose up --build
````

Once started, services are available locally. Exact ports are defined in `docker-compose.yaml`.

---

## Running Automated Tests

Tests run separately but rely on the running system.

### Install Dependencies

Recommend using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest
```

### Run with Allure Results

```bash
pytest --alluredir=./allure-results
```

### Selective Execution

Use markers (defined in `pytest.ini`), for example:

```bash
pytest -m "regression"      # Regression tests
pytest -m "positive"      # Positive tests
pytest -m "negative"      # Negative tests
```

You can also run tests for a specific service or protocol:

```bash
pytest tests/suites/integration/http/gateway/accounts/
pytest tests/suites/integration/grpc/gateway/cards/
```

---

## 📊 Allure Reporting

After running tests with the `--alluredir` flag, generate and serve the report:

```bash
allure serve allure-results
```

This opens an interactive HTML report in your default browser.

---

## Coverage report

After running tests generate report to `tests/reports/coverage.html`:
```bash
swagger-coverage-tool save-report
```

## Reports example
### Coverage report
![Coverage report](/tests/reports/coverage-report.png)

![Coverage report](/tests/reports/coverage-report-2.png)

### Allure report overview
![Allure report overview](/tests/reports/allure-report-overview.png)

### Allure report behaviors
![Allure report behaviors](/tests/reports/allure-report-behaviors.png)



