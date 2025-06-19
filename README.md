# LandCheck
This document describes the RESTful API endpoints for the Real Estate Reels Application built with FastAPI. It includes functionality for managing reels, properties, agents, bookings, users, and onboarding data.

---

## Base URL

```
http://localhost:8000/api
```

---

## Endpoints

### 🎞️ Reels

- **GET **`` - Get all reels
- **POST **`` - Create a new reel
- **GET **`` - Get reel by ID
- **POST **`` - Like a reel
- **POST **`` - Dislike a reel
- **POST **`` - Share a reel

**Request Body (Create):**

```json
{
  "title": "Villa Tour",
  "description": "Check out this villa",
  "video_url": "http://example.com/video.mp4",
  "property_id": "6657a1cf7b3f4e0123456789",
  "location": "Chennai, India"
}
```

---

### 🏠 Properties

- **GET **`` - List all properties
- **POST **`` - Create new property
- **GET **`` - Get properties near a location
  - Parameters: `latitude`, `longitude`, `max_distance`
- **GET **`` - Search properties by query text
- **GET **`` - Get property by ID
- **GET **`` - Get all bookings for property

**Request Body (Create):**

```json
{
  "name": "Seaside Villa",
  "type": "villa",
  "location": {"type": "Point", "coordinates": [80.27, 13.08]},
  "address": "Marina Beach Road",
  "city": "Chennai",
  "country": "India",
  "image_url": "http://example.com/image.jpg",
  "agent_id": "123abc"
}
```

---

### 👥 Agents

- **POST **`` - Create agent
- **GET **`` - Get agent by ID
- **GET **`` - Get listings for agent
- **GET **`` - Get sold listings by agent
- **GET **`` - Get bookings handled by agent

---

### 📅 Bookings

- **POST **`` - Create booking
- **GET **`` - Get booking by ID
- **PUT **`` - Update booking status

**Request Body (Create):**

```json
{
  "property_id": "123abc",
  "agent_id": "456def",
  "user_id": "789ghi",
  "date": "2025-07-10T10:30:00"
}
```

**Request Body (Status Update):**

```json
{
  "status": "confirmed"
}
```

---

### 🧑‍💼 Users

- **POST **`` - Create user
- **GET **`` - Get user by ID
- **GET **`` - Get user by email

**Request Body (Create):**

```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "phone": "9876543210"
}
```

---

### 📚 Onboarding

- **POST **`` - Save onboarding preferences
  - **Header Required**: `user-id: <user_id>`

**Request Body:**

```json
{
  "preferred_locations": ["Chennai", "Bangalore"],
  "property_types": ["villa"],
  "budget_range": [5000000, 10000000],
  "important_amenities": ["parking", "gym"],
  "lifestyle_preferences": ["quiet area"]
}
```

---

