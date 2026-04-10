# Restaurant Finder – Project Plan

## 1. Introduction
This project proposes the development of a software system called **Restaurant Finder**.
The system is intended to support the management and exploration of restaurant information through a clean and extendable architecture.

The project is planned as a gradual multi-stage software solution.
It begins with a simple backend service, continues with a frontend interface, and later evolves into a more complete local software system with persistent storage and improved functionality.

The purpose of this document is to present the overall design, scope, architecture, technologies, and development plan of the project before implementation begins.

---

## 2. Project Purpose
The main purpose of the project is to build a small but realistic software solution that demonstrates modern software engineering principles taught in the course.

More specifically, the project aims to demonstrate:
- development of a RESTful backend using FastAPI
- clear separation between layers and responsibilities
- input validation using Pydantic
- automated testing of API behavior
- communication between frontend and backend
- gradual evolution of a software system without changing its core contract

The project is intentionally designed to remain focused and manageable while still reflecting real software development practices.

---

## 3. Project Idea
**Restaurant Finder** is a system for storing, managing, and browsing restaurant data.

Users will be able to:
- create new restaurants
- view all restaurants
- retrieve a specific restaurant by its identifier
- update restaurant details
- delete restaurants
- browse and filter restaurant information through a simple user interface

The selected idea is suitable for the course because it contains a clear main entity, supports standard CRUD operations, and can be expanded in later stages without requiring a redesign of the entire system.

---

## 4. Main Entity
The core entity of the project is **Restaurant**.

Each restaurant record will represent one restaurant in the system and will include a set of basic descriptive attributes.

### Planned fields
- `id`
- `name`
- `city`
- `country`
- `cuisine`
- `price_level`
- `rating`
- `is_open`

These fields were chosen because they are simple, meaningful, and sufficient for building a realistic yet manageable system.

---

## 5. Validation Rules
The backend will validate all incoming data before storing or updating records.

### Planned validation rules
- `name` must not be empty
- `city` must not be empty
- `country` must not be empty
- `cuisine` must not be empty
- `price_level` must be within a valid range such as 1 to 5
- `rating` must be within a valid range such as 1.0 to 5.0
- `is_open` must be a boolean value

### Possible normalization rules
- trimming unnecessary whitespace from text fields
- converting cuisine values to title case
- converting city and country values into a consistent format

These validation and normalization rules are intended to improve data quality and maintain consistency across the system.

---

## 6. Architectural Approach
The project will follow a **layered architecture** in order to maintain clarity, modularity, and future extensibility.

### Planned layers
- **API layer**  
  Responsible for receiving HTTP requests and returning HTTP responses

- **Schema and model layer**  
  Responsible for defining request and response structures and validating data

- **Repository layer**  
  Responsible for abstracting storage and data access operations

- **Frontend layer**  
  Responsible for providing a simple user interface through Streamlit

- **Persistence layer**  
  Planned for a later stage in order to support persistent storage

This layered approach ensures that internal implementation details can evolve over time without forcing major changes to the system interface.

---

## 7. Design Principle
A central design principle of the project is to keep the **API contract stable** across stages.

This means that even if the internal storage mechanism changes later from in-memory storage to a persistent database, the external API structure should remain as consistent as possible.

This decision supports:
- cleaner software evolution
- easier frontend integration
- simpler testing
- improved maintainability

---

## 8. Development Stages

## Stage A – Backend Foundation
The first stage focuses on building the backend of the system using FastAPI.

### Planned goals
- create a working FastAPI application
- implement core CRUD operations for restaurants
- validate all incoming requests
- return proper HTTP status codes
- write automated tests
- package the application for local execution
- maintain clean code organization

### Storage approach
At this stage, storage will be **in-memory only**.
This keeps the focus on API design, validation, testing, and software structure before adding database complexity.

---

## Stage B – Frontend Interface
The second stage focuses on building a simple user interface using Streamlit.

### Planned goals
- display all restaurants
- add new restaurants using a form
- show restaurant details
- update restaurant information
- delete restaurants
- support simple filtering such as by city or cuisine

The frontend will communicate only with the backend API and will not access storage directly.

This design preserves separation of concerns and reinforces the role of the API as the central system interface.

---

## Stage C – Extended Local System
The third stage focuses on evolving the project into a more complete local software system.

### Planned goals
- replace in-memory storage with persistent storage
- run the backend and frontend as separate cooperating services
- improve project documentation and setup instructions
- add one meaningful enhancement such as search or filtering
- preserve the overall system contract while improving internal implementation

This stage will transform the project from a simple prototype into a more realistic multi-component software solution.

---

## 9. Planned API Endpoints

### Diagnostics
- `GET /health`

### Restaurants
- `GET /restaurants`
- `POST /restaurants`
- `GET /restaurants/{restaurant_id}`
- `PUT /restaurants/{restaurant_id}`
- `DELETE /restaurants/{restaurant_id}`

### Possible future extensions
- `GET /restaurants/search`
- `GET /restaurants/filter`

The first version of the system will focus on the essential endpoints required for clean CRUD functionality.
Additional endpoints may be added later only if they contribute clearly to the project goals.

---

## 10. Backend Responsibilities
The backend will be responsible for:
- exposing the API endpoints
- validating incoming requests
- delegating data operations to the repository layer
- handling missing resources and invalid input
- returning consistent responses and HTTP status codes
- supporting automated tests

The backend is the main technical core of the project and will serve as the foundation for all later stages.

---

## 11. Frontend Responsibilities
The frontend will be developed using Streamlit and will serve as the user-facing interface of the project.

It will be responsible for:
- presenting restaurant data in a readable format
- sending user actions to the backend API
- supporting simple user interaction flows
- making the system easier to demonstrate and evaluate

The frontend is intentionally planned as simple and focused.
Its role is not to replace backend logic, but to provide a convenient way to interact with the system.

---

## 12. Data Source Strategy
The core version of the project will rely on the project’s own backend and repository layer.

The project may optionally include a CSV dataset of restaurants as **seed or demo data**.
Such a dataset can be useful for:
- initial loading
- testing
- demonstrations
- showing sample records in the user interface

However, the project is not designed to depend on the CSV as its main architectural component.

Similarly, an external public API may be considered in the future only as an optional enhancement.
The main requirement is to build and maintain the project’s own API and internal logic.

---

## 13. Testing Strategy
Automated tests will be included in order to verify the correctness and stability of the backend.

### Planned test coverage
- health endpoint returns valid response
- creating a restaurant with valid input succeeds
- invalid input produces validation errors
- listing restaurants returns expected results
- retrieving a restaurant by id works correctly
- updating a restaurant works correctly
- deleting a restaurant works correctly
- requesting a missing restaurant returns the correct error response

Testing is an essential part of the project because it ensures that the system remains reliable as new changes are introduced.

---

## 14. Technology Stack
The planned technologies for this project are:

- **Python**
- **FastAPI**
- **Pydantic**
- **pytest**
- **Streamlit**
- **Docker**
- **uv**
- **VS Code**

Possible later additions:
- **SQLite** or another lightweight relational database
- optional CSV file for seed data
- optional external restaurant data source for enrichment

The selected stack is consistent with the technologies discussed in the course and supports the intended project evolution.

---

## 15. Proposed Project Structure
A possible project structure is the following:

```text
restaurant_finder/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── repository.py
│   ├── dependencies.py
│   └── routes/
│       └── restaurants.py
│
├── tests/
│   ├── conftest.py
│   └── test_restaurants.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   └── restaurants.csv
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── plan.md