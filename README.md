# Greenhouse Backend API

This is a FastAPI-based backend for managing greenhouse IoT devices and plants. It provides endpoints for updating plant and device events, logging data, and interacting with the database.

## Features
- **Plant Event Management**: Update plant-related events such as luminosity, humidity, valve state, and LED intensity.
- **Device Event Management**: Update IoT device-related events such as pump state.
- **Logging**: Automatically create log entries whenever a plant or device event is updated.
- **Database Integration**: Uses PostgreSQL as the database with SQLAlchemy for ORM.
- **Deployment Ready**: Includes a `Procfile` for deployment on Railway.

---

## Requirements
- Python 3.10 or higher
- PostgreSQL database
- Virtual environment for dependency management

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd greenhouse_backGUI_v1
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
* On Windows 
```bash
.\venv\Scripts\Activate.ps1
```

* On macOS/Linux
```bash
source venv/bin/activate
```

### 4. Install Dependecies
```bash
pip install -r requirements.txt
```

## Configuration
`.env` File
Create a `.env` file in the root directory based on the provided `.env.example` file. This file contains the environment variables required for the application to connect to the database and run properly.

### Example `.env` File: 

```bash
user=your_supabase_user
password=your_supabase_password
host=your_supabase_host
port=your_supabase_port
dbname=your_supabase_dbname
app_port=your_app_port
```

Remember that:
* `password`: Your database password.
* `host`: The host address of your database.
* `port`: The port number for your database.
* `dbname`: The name of your database.
* `app_port`: The port on which the FastAPI app will run locally.

## Running the Application Locally

### 1. Activate the Virtual Environment

* On Windows (Where this was developped)
```bash
.\venv\Scripts\Activate.ps1
```

### 2. Run the Application
Use the following command to start the FastAPI application:
```bash
uvicorn main:app --reload  
 ```

Or simply run main.py and it will automatically run on `app_port` from the `.env`
### 3. Access the API
Once the application is running, you can access the API documentation at:

* Swagger UI: http://127.0.0.1:your_app_port/docs
* ReDoc: http://127.0.0.1:your_app_port/redoc

## Deployment on Railway
This project is configured for deployment on Railway. The `Procfile` is included to specify the startup command.

Procfile 
```bash
web: uvicorn main:app --host 0.0.0.0 --port $app_port 
```
Steps to Deploy: 
1. **Push Your Code to GitHub**  
    Ensure your code is pushed to a GitHub repository.

2. **Connect to Railway**  
    Log in to [Railway](https://railway.app/) and connect your GitHub repository.

3. **Set Environment Variables**  
    In the Railway dashboard, configure the environment variables based on your `.env` file.

4. **Deploy the Application**  
    Once the environment variables are set, deploy the application directly from the Railway dashboard.

## Project Structure

```bash
greenhouse_backGUI_v1/
├── models/
│   ├── schema.py          # SQLAlchemy models for database tables
│   ├── plantModels.py     # Pydantic models for plant-related requests
│   ├── iotDevModels.py    # Pydantic models for IoT device-related requests
├── routers/
│   ├── events.py          # FastAPI routes for plant and device events
├── services/
│   ├── event_service.py   # Service for updating plant and device events
│   ├── log_service.py     # Service for creating log entries
├── utils/
│   ├── db.py              # Database connection and session management
│   ├── request_validation.py # Utility functions for request validation
├── .env.example         # Example environment variables file
├── main.py              # Entry point for the FastAPI application
├── requirements.txt       # Python dependencies
├── Procfile               # Configuration for deployment on Railway
└── README.md              # Project documentation
```
## Endpoints

### Plant Events
- **PUT** `/events/plant/luminosity`: Update the luminosity event for a plant.
- **PUT** `/events/plant/humidity`: Update the humidity event for a plant.
- **PUT** `/events/plant/valve`: Update the valve state event for a plant.
- **PUT** `/events/plant/led`: Update the LED intensity event for a plant.

### Device Events
- **PUT** `/events/device/pump`: Update the pump state event for an IoT device.

## Explanation of Key Files
`requirements.txt`

This file lists all the Python dependencies required for the project. Install them using:

```bash
pip install -r requirements.txt
```
### Key Dependencies

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **Psycopg2**: PostgreSQL database adapter.
- **Uvicorn**: ASGI server for running the FastAPI app.
- **Python-Dotenv**: For loading environment variables from a `.env` file.

---
`.env.example`
This file provides a template for the environment variables required by the application. Copy it to `.env` and fill in the appropriate values.

## Logging

Whenever a plant or device event is updated, a new log entry is automatically created in the `Log` table. The log includes:

* Timestamps for creation and storage.
* The last recorded temperature.
* Current state and event values for the plant and associated IoT device.

## System Communication Diagram

![GreenhouseDiagram](https://www.plantuml.com/plantuml/png/bLLDRziu4BthLmpQg-CYFXfmqBGssYpIHRjozsGW695ZYuX4QicH7E-lNv2IhAyupjuCSzwyz-PBdnsZvJBFu9ibqgaf7QqL7YpcaNjMka2BESJqJqbQq0zo3Wzqdwc3paap2D9CDcB56VKoG7noJ1qEsfHHObxWmxtW4jbOzm4-Fgf3ob-oaY80W08jAw4Ar0pdgASYGystrm8M4Ma9YNbfM6BIxXf74tE9OV3Soz-FUJ3R9qdLyCyVlxRRfyIQPxADceqyK2ib56f2zgUHz4VyvCXMPCEhHCO4VJb_FSfa0lXcSOyQMyHP7Ges5duxpwqD4vYAxCZgREHj2T_BN4d5fnamvGLPvDBIRATHIyYyQd0r8le4NTPnasQJhYmXDXbfeoHKc5NaPb2O8rbutAnTa_-8J1QACY-YQBLwq8eLPkfVP6NqQkKh6ymFAWGtTtLTO0b_-Jbp3C9eJSAZGdpzV7DpDq8kuLuyQtFCI1ve31fMzN-nZA0NQKZBA6hcnXFqfkLrcdw09sgn5nc6YAd_LpX6nPt8kiIqMgsH4ROMjSkLStNB3jQKHJDZC0cewpOOI1ZO2eYzDNapT72xqqV5AR3AoJ7cnJJ5uagAnIH5w4EjD4J7R2mUwYlHQy-uUEFC3fhCmb8OsP7AYsFh-IXiEIZTRNkJpVbNENRyhf4EALtZ9hZiDdQ0MyBNYURQcgHA2PhlT3oI0IWbIKXEKAVujFuo7rJnR-NAy_O6qVuKmMlxqOvXqBit5ge9zgrrPAkeQjpMefiINjlBsD_A06FJlaBly8v9R-vg3qjOArTaUAh1nZVDfOb1A-iohrPVJPxxaxPv8L4sz-kgVz60g0L5KzkJ5Tx4MxZ_-G02iypxgC7K9eikZjtlGc8N1uwHIzUVmFvNmsEMiAd8da2GPLGQC3UbPZ3xC1N0gP_Pcgwf8eYKnBCBJ-UvzWrkI5rFy3nwxvqUw2s3YwjdwsUPPCgbvwgC3cDtBqQ1NY2sdxB-_hplYvTJPpN74oIr_URMjRyMSzZf3OeKwlqn-uuJKdIWs84vwk09s1HAU5qxRKcGgZgE-U1xCfRefyNqHgFl3MxVG2xUH2wYw3DfMURPVm00 "GreenhouseDiagram")

## Database

The database for this project is hosted on Supabase, providing a reliable and scalable solution for managing greenhouse data. You can view the database schema and architecture through the following link:

[View Database Schema on dbdiagram.io](https://dbdiagram.io/d/Greenhouse-68122d751ca52373f5fe1cde)

This schema outlines the relationships and structure of the tables used in the application, ensuring efficient data storage and retrieval.

## License

MIT © 2025 — Santiago Estrada Bernal

## Contact

For any inquiries, please contact [santiago.estrada6@eia.edu.co](mailto:santiago.estrada6@eia.edu.co).
