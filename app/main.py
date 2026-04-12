from __future__ import annotations

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import RepositoryDep
from app.models import Restaurant, RestaurantCreate

app = FastAPI(title="Restaurant Finder", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok", "app": "Restaurant Finder"}


@app.get("/restaurants", response_model=list[Restaurant])
def list_restaurants(repository: RepositoryDep) -> list[Restaurant]:
    """Return all restaurants."""
    return repository.list()


@app.post("/restaurants", response_model=Restaurant, status_code=status.HTTP_201_CREATED)
def create_restaurant(
    payload: RestaurantCreate,
    repository: RepositoryDep,
) -> Restaurant:
    """Create a new restaurant."""
    try:
        return repository.create(payload)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error


@app.get("/restaurants/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: int, repository: RepositoryDep) -> Restaurant:
    """Return a restaurant by ID."""
    restaurant = repository.get(restaurant_id)
    if restaurant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found",
        )
    return restaurant


@app.put("/restaurants/{restaurant_id}", response_model=Restaurant)
def update_restaurant(
    restaurant_id: int,
    payload: RestaurantCreate,
    repository: RepositoryDep,
) -> Restaurant:
    """Update an existing restaurant."""
    try:
        updated_restaurant = repository.update(restaurant_id, payload)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error

    if updated_restaurant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found",
        )
    return updated_restaurant


@app.delete("/restaurants/{restaurant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_restaurant(restaurant_id: int, repository: RepositoryDep) -> None:
    """Delete a restaurant by ID."""
    deleted = repository.delete(restaurant_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found",
        )