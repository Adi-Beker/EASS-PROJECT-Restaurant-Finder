const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

async function buildError(response, fallbackMessage) {
  try {
    const data = await response.json();
    return new Error(data.detail || fallbackMessage);
  } catch {
    return new Error(fallbackMessage);
  }
}

export async function getVisitedRestaurants() {
  const response = await fetch(`${API_BASE_URL}/restaurants`);
  if (!response.ok) {
    throw await buildError(response, "Failed to fetch visited restaurants");
  }
  return response.json();
}

export async function createVisitedRestaurant(restaurantData) {
  const response = await fetch(`${API_BASE_URL}/restaurants`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(restaurantData),
  });

  if (!response.ok) {
    throw await buildError(response, "Failed to create restaurant");
  }

  return response.json();
}

export async function updateVisitedRestaurant(id, restaurantData) {
  const response = await fetch(`${API_BASE_URL}/restaurants/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(restaurantData),
  });

  if (!response.ok) {
    throw await buildError(response, "Failed to update restaurant");
  }

  return response.json();
}

export async function deleteVisitedRestaurant(id) {
  const response = await fetch(`${API_BASE_URL}/restaurants/${id}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw await buildError(response, "Failed to delete restaurant");
  }

  return true;
}