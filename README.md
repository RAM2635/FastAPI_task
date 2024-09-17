# FastAPI URL Shortening Service

This is a simple URL shortening service built using FastAPI. It provides endpoints to shorten a URL and retrieve the
original URL using the shortened version.

## Features

- Shorten a given URL and receive a shortened URL in response.
- Redirect to the original URL using the shortened URL.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install fastapi uvicorn
   ```

## Usage

1. Start the server:

   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8080
   ```

2. Access the API documentation at [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs).

### Endpoints

- **POST /**

    - Shorten a URL.
    - **Request Body:** JSON object containing the URL (`{"url": "http://example.com"}`)
    - **Response:** JSON object with the shortened URL (`{"shortened_url": "http://127.0.0.1:8080/abcd1234"}`)

- **GET /{short_url_id}**

    - Redirect to the original URL using the shortened URL identifier.
    - **Response:** Redirects to the original URL or returns a 404 error if not found.

## Notes

- This application uses an in-memory storage for URL mapping, which means all data will be lost when the server stops.
  For production use, consider integrating a persistent database.

## License

This project is open-source and available under the MIT License.


