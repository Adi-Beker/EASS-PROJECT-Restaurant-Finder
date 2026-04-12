# Restaurant Finder – Project Plan

## 1. Project Overview
Restaurant Finder is a web application for discovering recommended restaurants and managing a personal list of restaurants the user has visited.

The project is planned as a multi-stage system:
- Stage A: backend development with FastAPI
- Stage B: frontend development with React
- Stage C: persistent storage and a more complete local system

The goal is to build a clean and understandable project that can grow gradually while keeping the system simple.

---

## 2. Project Idea
The system combines two simple goals:

- discovering recommended restaurants
- managing a personal visited restaurants list

The application allows users to:
- explore recommended restaurants
- search restaurants by name
- filter restaurants by country
- add restaurants to a personal visited list
- create visited restaurants manually
- update visited restaurant details
- delete restaurants from the visited list

This creates a simple but realistic product that combines discovery and personal management.

---

## 3. Main Entity
The main backend entity is **Restaurant**.

Each restaurant in the visited list includes the following fields:

- `id`
- `name`
- `city`
- `country`
- `cuisine`
- `price_level`
- `rating`
- `is_open`

These fields are enough to support useful restaurant management without unnecessary complexity.

---

## 4. Validation Rules
The backend validates incoming data before saving it.

Validation rules:
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

- backend API layer
- model/schema layer
- repository layer
- frontend UI layer

The backend handles API logic, the repository handles data access, and the frontend communicates only with the backend API.

This keeps the project clear and supports separation of responsibilities.

---

## 6. Development Stages

### Stage A – Backend
Stage A focuses on building the backend with FastAPI.

Completed goals:
- create a working FastAPI application
- implement restaurant CRUD operations
- validate input data
- return proper HTTP status codes
- write automated tests
- support Docker execution

At this stage, storage is in memory only.

### Stage B – Frontend
Stage B focuses on building a React frontend.

Completed or current goals:
- build a separate frontend application
- provide a Discover page for restaurant recommendations
- support search by restaurant name
- support filtering by country
- provide a My Visited page
- support create, update, and delete operations through the UI
- connect the frontend only to the backend API
- support Docker Compose for running frontend and backend together

### Stage C – Extended Version
Stage C focuses on improving the project into a more complete local system.

Planned goals:
- replace in-memory storage with persistent storage
- improve the UI and overall user experience
- improve documentation and project setup
- add one meaningful enhancement such as richer filtering or improved restaurant data management

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

These endpoints are enough for the current version of the project.

---

## 8. Frontend Features

### Discover Page
The Discover page allows users to:
- browse recommended restaurants
- search restaurants by name
- filter restaurants by country
- add a restaurant to the visited list

### My Visited Page
The My Visited page allows users to:
- view all visited restaurants
- create a visited restaurant manually
- update an existing visited restaurant
- delete a visited restaurant

### Navigation
The frontend includes a simple navigation bar with:
- Discover
- My Visited

---

## 9. Testing Plan
The backend includes automated tests for:
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

## 10. Technology Stack
Technologies used or planned:
- Python
- FastAPI
- Pydantic
- pytest
- React
- Vite
- Docker
- Docker Compose
- uv

Possible later addition:
- SQLite or another lightweight database

---

## 11. Project Structure
A possible project structure is:

```text
restaurant_finder/
|-- app/
|   |-- main.py
|   |-- models.py
|   |-- repository.py
|   `-- dependencies.py
|-- frontend/
|   |-- src/
|   |   |-- components/
|   |   |-- data/
|   |   |-- pages/
|   |   |-- api.js
|   |   |-- App.jsx
|   |   |-- App.css
|   |   `-- main.jsx
|   |-- package.json
|   `-- vite.config.js
|-- tests/
|   |-- conftest.py
|   `-- test_restaurants.py
|-- backend.Dockerfile
|-- frontend.Dockerfile
|-- docker-compose.yml
|-- README.md
|-- plan.md
|-- pyproject.toml
`-- uv.lock
