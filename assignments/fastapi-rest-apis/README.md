# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a REST API using FastAPI, define request and response models with Pydantic, and implement routes that handle GET and POST requests.

## 📝 Tasks

### 🛠️ Create the API structure

#### Description
Create a FastAPI application with a root endpoint and a welcome endpoint.

#### Requirements
Completed program should:

- Define a FastAPI app instance.
- Add a root (`/`) GET endpoint that returns a welcome message.
- Add a `/hello` GET endpoint that returns a JSON greeting.

### 🛠️ Add data input using POST

#### Description
Add a POST endpoint that accepts JSON input for a new item and returns the created item data.

#### Requirements
Completed program should:

- Define a Pydantic model named `Item` with `name`, `description`, and `price` fields.
- Create a POST endpoint at `/items/` that accepts an `Item` body.
- Return the submitted item data in the response.

### 🛠️ Validate input and use query parameters

#### Description
Add validation and use query parameters for filtering or additional response data.

#### Requirements
Completed program should:

- Use the `Item` model to validate incoming JSON data.
- Add a GET endpoint at `/items/{item_id}` that accepts an `item_id` path parameter.
- Optionally accept a query parameter `discount` and return it in the response when provided.
- Return a JSON object with `item_id`, item details, and any applied discount.
