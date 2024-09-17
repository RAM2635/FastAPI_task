from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel, HttpUrl
import uuid

# Initialize FastAPI application
app = FastAPI()

# Temporary in-memory storage for mapping shortened and original URLs
url_mapping = {}


# Data model for the request containing the URL, with built-in validation using HttpUrl
class URLRequest(BaseModel):
    url: HttpUrl  # Field to ensure the provided URL is valid


# Endpoint for shortening URLs
@app.post("/", status_code=201)
async def shorten_url(request: URLRequest):
    """
    Accepts an original URL and returns a shortened version.

    Parameters:
    - request (URLRequest): Object containing the original URL to be shortened.

    Returns:
    - JSON with a 'shortened_url' field containing the shortened URL link.
    """
    # Generate a unique identifier for the shortened URL (first 8 characters of a UUID)
    short_url_id = str(uuid.uuid4())[:8]

    # Store the original URL in memory
    url_mapping[short_url_id] = request.url

    # Formulate the shortened URL and return it to the client
    return JSONResponse({"shortened_url": f"http://127.0.0.1:8080/{short_url_id}"}, status_code=201)


# Endpoint for retrieving the original URL using the shortened identifier
@app.get("/{short_url_id}")
async def get_original_url(short_url_id: str):
    """
    Retrieves the original URL using the given shortened URL identifier.

    Parameters:
    - short_url_id (str): Unique identifier of the shortened URL.

    Returns:
    - RedirectResponse to the original URL if found.
    - 404 error if the identifier is not found in the storage.
    """
    # Look up the original URL using the identifier
    original_url = url_mapping.get(short_url_id)

    # If the original URL is found, redirect to it
    if original_url:
        return RedirectResponse(original_url, status_code=307)

    # If the identifier is not found, return a 404 error
    raise HTTPException(status_code=404, detail="Shortened URL not found")


# Main entry point for the application
if __name__ == "__main__":
    import uvicorn

    # Run the application on a local server with the specified host and port
    uvicorn.run(app, host="127.0.0.1", port=8080)
