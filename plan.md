# Restaurant Finder – Project Plan

## 1. Project Overview
Restaurant Finder is a simple software project for managing restaurant data.

The project is planned as a multi-stage system:
- Stage A: backend development with FastAPI
- Stage B: frontend development with Streamlit
- Stage C: persistent storage and a more complete local system

The goal is to build a clean and understandable project that can grow gradually while keeping the system simple.

---

## 2. Project Idea
The system focuses on one main entity: **Restaurant**.

It will allow users to:
- create restaurants
- view all restaurants
- get a restaurant by id
- update restaurant details
- delete restaurants

In later stages, the system will also support a simple frontend for browsing and managing restaurant data.

---

## 3. Main Entity
Each restaurant will include the following fields:

- `id`
- `name`
- `city`
- `country`
- `cuisine`
- `price_level`
- `rating`
- `is_open`

These fields are enough to build a realistic project without adding unnecessary complexity.

---

## 4. Validation Rules
The backend will validate incoming data before saving it.

Planned validation rules:
- `name` must not be empty
- `city` must not be empty
- `country` must not be empty
- `cuisine` must not be empty
- `price_level` must be between 1 and 5
- `rating` must be between 1.0 and 5.0
- `is_open` must be a boolean value

Basic normalization may also be applied, such as:
- trimming extra spaces
- formatting city, country, and cuisine fields consistently

---

## 5. Design Approach
The project follows a simple layered structure:

- API layer
- model/schema layer
- repository layer
- frontend layer in a later stage

The backend will handle API logic, the repository will handle data access, and the frontend will communicate only with the backend.

This keeps the project clear and supports separation of responsibilities.

---

## 6. Development Stages

### Stage A – Backend
Stage A focuses on building the backend with FastAPI.

Planned goals:
- create a working FastAPI application
- implement restaurant CRUD operations
- validate input data
- return proper HTTP status codes
- write automated tests
- support Docker execution

At this stage, storage will be in memory only.

### Stage B – Frontend
Stage B focuses on building a simple Streamlit interface.

Planned goals:
- display restaurants
- add a restaurant
- update restaurant data
- delete a restaurant
- show backend status
- support simple filtering if needed

The frontend will communicate only with the backend API.

### Stage C – Extended Version
Stage C focuses on improving the project into a more complete local system.

Planned goals:
- replace in-memory storage with persistent storage
- improve documentation and setup
- run the system as a more complete local solution
- add one meaningful improvement such as simple search or filtering

---

## 7. Planned API Endpoints

### Health
- `GET /health`

### Restaurants
- `GET /restaurants`
- `POST /restaurants`
- `GET /restaurants/{restaurant_id}`
- `PUT /restaurants/{restaurant_id}`
- `DELETE /restaurants/{restaurant_id}`

These endpoints are enough for the first version of the project.

---

## 8. Testing Plan
The project will include automated tests for:
- health endpoint
- create restaurant
- list restaurants
- get restaurant by id
- update restaurant
- delete restaurant
- validation errors
- missing restaurant handling

The purpose of testing is to keep the backend stable and reliable.

---

## 9. Technology Stack
Planned technologies:
- Python
- FastAPI
- Pydantic
- pytest
- Streamlit
- Docker
- uv

Possible later addition:
- SQLite or another lightweight database

---

## 10. Project Structure
The project starts with a backend in Stage A and expands in later stages.

A possible project structure is:

```text
restaurant_finder/
|-- app/
|   |-- main.py
|   |-- models.py
|   |-- repository.py
|   `-- dependencies.py
|-- tests/
|   |-- conftest.py
|   `-- test_restaurants.py
|-- frontend/
|   `-- streamlit_app.py
|-- Dockerfile
|-- README.md
|-- plan.md
|-- pyproject.toml
`-- uv.lock
```

In Stage A, the main focus is the backend and tests.
The `frontend/` folder is planned for Stage B and may be added later when the Streamlit interface is implemented.

---

## 11. Scope Boundaries
To keep the project simple and realistic, the following are out of scope for the first version:
- mobile application
- CLI client
- reservation system
- payment system
- delivery system
- authentication
- advanced map integration
- external API integration as a core dependency

This keeps the project aligned with the course level and with KISS principles.

---

## 12. Summary
Restaurant Finder is a simple student-level software project based on one clear entity and standard CRUD operations.

The project starts with a clean backend, continues with a simple frontend, and later evolves into a more complete local system.

The main focus is to keep the project clear, modular, and easy to understand while following good software design practices.