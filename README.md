# API Course — FastAPI User CRUD

A simple REST API built with [FastAPI](https://fastapi.tiangolo.com/) demonstrating basic CRUD (Create, Read, Update, Delete) operations on an in-memory user store.

## Features

- Health check endpoint
- Get a user by ID
- Create a new user
- Update an existing user (partial updates supported)
- Delete a user
- Search for a user by name

## Requirements

- Python 3.9+

## Setup

1. Clone the repository and navigate into it:

   ```bash
   git clone <your-repo-url>
   cd API_COURSE
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the API

```bash
uvicorn myapi:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Interactive API docs (Swagger UI) are available at `http://127.0.0.1:8000/docs`, and the ReDoc UI at `http://127.0.0.1:8000/redoc`.

## Endpoints

| Method | Path                        | Description                          |
|--------|-----------------------------|---------------------------------------|
| GET    | `/`                          | Health check                         |
| GET    | `/users/{user_id}`           | Get a user by ID (1–99)              |
| POST   | `/users/{user_id}`           | Create a new user                    |
| PUT    | `/users/{user_id}`           | Update an existing user (partial)    |
| DELETE | `/users/{user_id}`           | Delete a user                        |
| GET    | `/users/search/?name=...`    | Search for a user by exact name      |

### Example: Create a user

```bash
curl -X POST http://127.0.0.1:8000/users/2 \
  -H "Content-Type: application/json" \
  -d '{"name": "Bob", "age": 30, "role": "Tester"}'
```

### Example: Update a user

```bash
curl -X PUT http://127.0.0.1:8000/users/2 \
  -H "Content-Type: application/json" \
  -d '{"age": 31}'
```

### Example: Search by name

```bash
curl "http://127.0.0.1:8000/users/search/?name=Bob"
```

## Project Structure

```
.
├── myapi.py          # FastAPI application and routes
├── requirements.txt  # Python dependencies
└── README.md
```
