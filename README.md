# FastAPI Basics

## What is FastAPI?

FastAPI is a modern Python web framework used to build APIs quickly and efficiently. It provides automatic API documentation, request validation, type hints, and supports asynchronous programming.

## Main Technologies Behind FastAPI

### 1. Pydantic

FastAPI uses **Pydantic** for data validation and serialization.

For example, when an API expects:

```python
class User(BaseModel):
    name: str
    age: int
```

Pydantic automatically checks whether the incoming data follows this structure.

It helps with:

* Request data validation
* Response validation
* Data parsing
* Type checking

### 2. Starlette

FastAPI is built on top of **Starlette**.

Starlette provides the web-related functionality such as:

* Routing
* HTTP requests and responses
* Middleware
* WebSockets
* Background tasks

So, FastAPI mainly adds developer-friendly features such as validation, type hints, and automatic API documentation on top of Starlette.

### 3. ASGI

**ASGI (Asynchronous Server Gateway Interface)** is a standard that allows Python web servers to communicate with asynchronous web applications.

FastAPI is an **ASGI-compatible framework**.

The basic flow is:

Client → Uvicorn → FastAPI → Starlette/Pydantic → Response

### 4. Uvicorn

**Uvicorn is an ASGI web server.**

FastAPI itself is the application/framework, but it needs a server to receive HTTP requests and run the application.

We use Uvicorn for this:

```bash
uvicorn main:app --reload
```

Here:

* `main` → `main.py` file
* `app` → FastAPI object inside `main.py`
* `--reload` → automatically restarts the server when code changes during development

Uvicorn handles the communication between the client and our FastAPI application.

## FastAPI Architecture

```text
Client
   ↓
Uvicorn
   ↓
ASGI
   ↓
FastAPI
   ↓
Starlette
   ↓
Pydantic
   ↓
Response
```

### Why use Uvicorn?

FastAPI is an ASGI application, so it needs an ASGI server to run.

Uvicorn is lightweight, fast, and supports asynchronous Python applications, making it a common choice for running FastAPI applications.

## Running the Application

```bash
uvicorn main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## Current Learning

This folder contains my FastAPI basics and will be expanded as I learn:

* FastAPI fundamentals
* Routing
* HTTP methods
* Path and query parameters
* Pydantic models
* Request and response handling
* REST APIs
* Database integration
* Authentication
* JWT
* Testing
* Docker
