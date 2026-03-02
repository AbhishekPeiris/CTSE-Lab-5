# Microservices Lab - SE4010 (Option C)

A simple microservices system with 4 services using polyglot architecture (Option C).

## Architecture

```
Client (Postman)
      ↓
┌─────────────────────────┐
│   API Gateway :8080     │
│  /items /orders /payments│
└────┬──────┬──────┬──────┘
     ↓      ↓      ↓
  Item   Order  Payment
  :8081  :8082  :8083
```

## Technology Stack (Option C)

| Service | Technology | Port |
|---------|-----------|------|
| Item Service | FastAPI (Python) | 8081 |
| Order Service | Django REST (Python) | 8082 |
| Payment Service | .NET Core (C#) | 8083 |
| API Gateway | Express Gateway (Node.js) | 8080 |

## Quick Start

### 1. Build and Run
```bash
docker-compose build
docker-compose up
```

### 2. Check Services
```bash
docker ps
```

## API Endpoints (via Gateway - port 8080)

### Item Service
- `GET http://localhost:8080/items` - Get all items
- `POST http://localhost:8080/items` - Add item
- `GET http://localhost:8080/items/{id}` - Get item by ID

### Order Service
- `GET http://localhost:8080/orders` - Get all orders
- `POST http://localhost:8080/orders` - Place order
- `GET http://localhost:8080/orders/{id}` - Get order by ID

### Payment Service
- `GET http://localhost:8080/payments` - Get all payments
- `POST http://localhost:8080/payments/process` - Process payment
- `GET http://localhost:8080/payments/{id}` - Get payment by ID

## Sample Requests (Postman)

### Add Item
```
POST http://localhost:8080/items
Content-Type: application/json

{"name": "Headphones"}
```

### Place Order
```
POST http://localhost:8080/orders
Content-Type: application/json

{"item": "Laptop", "quantity": 2, "customerId": "C001"}
```

### Process Payment
```
POST http://localhost:8080/payments/process
Content-Type: application/json

{"orderId": 1, "amount": 1299.99, "method": "CARD"}
```

## Stop Services
```bash
docker-compose down
```
