from __future__ import annotations

from app.models import Restaurant, RestaurantCreate


class RestaurantRepository:
    def __init__(self) -> None:
        self._restaurants: list[Restaurant] = []
        self._next_id = 1

    def list(self) -> list[Restaurant]:
        return self._restaurants.copy()

    def get(self, restaurant_id: int) -> Restaurant | None:
        for restaurant in self._restaurants:
            if restaurant.id == restaurant_id:
                return restaurant
        return None

    def _is_duplicate(
        self,
        name: str,
        city: str,
        country: str,
        exclude_id: int | None = None,
    ) -> bool:
        normalized_name = name.strip().casefold()
        normalized_city = city.strip().casefold()
        normalized_country = country.strip().casefold()

        for restaurant in self._restaurants:
            if exclude_id is not None and restaurant.id == exclude_id:
                continue

            if (
                restaurant.name.strip().casefold() == normalized_name
                and restaurant.city.strip().casefold() == normalized_city
                and restaurant.country.strip().casefold() == normalized_country
            ):
                return True

        return False

    def create(self, payload: RestaurantCreate) -> Restaurant:
        if self._is_duplicate(payload.name, payload.city, payload.country):
            raise ValueError("Restaurant already exists in your visited list")

        restaurant = Restaurant(
            id=self._next_id,
            name=payload.name,
            city=payload.city,
            country=payload.country,
            cuisine=payload.cuisine,
            price_level=payload.price_level,
            rating=payload.rating,
            is_open=payload.is_open,
        )
        self._restaurants.append(restaurant)
        self._next_id += 1
        return restaurant

    def update(self, restaurant_id: int, payload: RestaurantCreate) -> Restaurant | None:
        for index, restaurant in enumerate(self._restaurants):
            if restaurant.id == restaurant_id:
                if self._is_duplicate(
                    payload.name,
                    payload.city,
                    payload.country,
                    exclude_id=restaurant_id,
                ):
                    raise ValueError("Restaurant already exists in your visited list")

                updated_restaurant = Restaurant(
                    id=restaurant_id,
                    name=payload.name,
                    city=payload.city,
                    country=payload.country,
                    cuisine=payload.cuisine,
                    price_level=payload.price_level,
                    rating=payload.rating,
                    is_open=payload.is_open,
                )
                self._restaurants[index] = updated_restaurant
                return updated_restaurant
        return None

    def delete(self, restaurant_id: int) -> bool:
        for index, restaurant in enumerate(self._restaurants):
            if restaurant.id == restaurant_id:
                del self._restaurants[index]
                return True
        return False

    def clear(self) -> None:
        self._restaurants.clear()
        self._next_id = 1