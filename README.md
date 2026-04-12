# Restaurant Finder

## Description
Restaurant Finder is a full-stack web application for discovering recommended restaurants and managing a personal list of restaurants the user has visited.

The project started as a FastAPI backend and was later extended with a React frontend that communicates only with the backend API.

## Current Stage
This repository currently includes:
- **Stage A**: FastAPI backend
- **Stage B**: React frontend

Stage A includes:
- FastAPI backend
- full restaurant CRUD operations
- input validation with Pydantic
- dependency injection
- automated tests with pytest
- Docker support

Stage B includes:
- React frontend with Vite
- Discover page for browsing recommended restaurants
- My Visited page for managing restaurants the user has visited
- search and filtering in the discovery section
- create, update, and delete operations through the UI
- Docker Compose support for running frontend and backend together

## Prerequisites
Before running the project, make sure the following tools are installed:

- Python 3.13
- `uv`
- Node.js and npm
- Docker Desktop, if you want to run the project in containers

## Features

### Backend
- FastAPI backend
- CRUD operations for restaurants
- input validation with Pydantic
- in-memory repository
- dependency injection
- Swagger/OpenAPI documentation
- automated tests with pytest

### Frontend
- React frontend with Vite
- navigation bar
- Discover page
- My Visited page
- search by restaurant name
- filter by country
- add a restaurant to My Visited
- create visited restaurants manually
- update visited restaurants
- delete visited restaurants

### Run Support
- Docker support
- Docker Compose support for frontend and backend together

## Technologies
- Python
- FastAPI
- Pydantic
- pytest
- React
- Vite
- JavaScript
- Docker
- Docker Compose
- uv

## Run the Backend Locally
From the project root:

```bash
uv run uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

## Backend API Documentation
FastAPI provides interactive Swagger/OpenAPI documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

## Run Backend Tests
Run all backend tests with:

```bash
uv run pytest tests -v
```

## Run the Frontend Locally
From the `frontend` folder:

```bash
npm install
npm run dev
```

The frontend will run at:

```text
http://127.0.0.1:5173
```

## Run with Docker Compose
From the project root:

```bash
docker compose up --build
```

After the containers start:

Frontend:

```text
http://127.0.0.1:5173
```

Backend:

```text
http://127.0.0.1:8000
```

Backend API Docs:

```text
http://127.0.0.1:8000/docs
```

## Available Backend Endpoints

### Health Check
- `GET /health`

### Restaurants
- `GET /restaurants`
- `POST /restaurants`
- `GET /restaurants/{restaurant_id}`
- `PUT /restaurants/{restaurant_id}`
- `DELETE /restaurants/{restaurant_id}`

## Example Request Body
Example JSON for creating a restaurant:

```json
{
  "name": "La Piazza",
  "city": "tel aviv",
  "country": "israel",
  "cuisine": "italian",
  "price_level": 3,
  "rating": 4.5,
  "is_open": true
}
```

## Project Structure
```text
EASS-PROJECT-Restaurant-Finder/
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- models.py
|   |-- repository.py
|   `-- dependencies.py
|-- frontend/
|   |-- public/
|   |-- src/
|   |   |-- components/
|   |   |-- data/
|   |   |-- pages/
|   |   |-- api.js
|   |   |-- App.css
|   |   |-- App.jsx
|   |   `-- main.jsx
|   |-- .gitignore
|   |-- eslint.config.js
|   |-- index.html
|   |-- package-lock.json
|   |-- package.json
|   `-- vite.config.js
|-- tests/
|   |-- __init__.py
|   |-- conftest.py
|   `-- test_restaurants.py
|-- .dockerignore
|-- .gitignore
|-- backend.Dockerfile
|-- docker-compose.yml
|-- frontend.Dockerfile
|-- plan.md
|-- pyproject.toml
|-- README.md
|-- restaurant_requests.http
`-- uv.lock
```

## REST Client Requests
The file `restaurant_requests.http` contains sample HTTP requests for manually testing the backend API endpoints.
It can be used with the REST Client extension in VS Code.

## Current Status
The project currently supports:
- backend CRUD operations for restaurants
- validation and automated backend tests
- a React frontend for restaurant discovery
- a personal visited restaurants list
- local frontend and backend development
- Docker Compose execution for the full system

At this stage:
- visited restaurants are stored in memory
- there is no persistent database yet
- authentication is not included
- advanced live external integrations are not included

## Author
Adi Beker