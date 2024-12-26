# FastAPI Peptide Prices API

This project is a FastAPI application that provides an API for retrieving peptide prices. It includes a router for handling peptide price-related endpoints and serves static files.

## Project Structure

```
fastapi-app
├── app
│   ├── main.py                # Entry point of the FastAPI application
│   ├── routers
│   │   └── peptide_prices.py   # Router for peptide price-related endpoints
│   └── static                 # Directory for static files (CSS, JS, images)
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

4. Access the API at `http://127.0.0.1:8000/`.

## Usage

- The root endpoint returns a welcome message.
- Additional endpoints for peptide prices will be defined in the `peptide_prices.py` router.

## License

This project is licensed under the MIT License.