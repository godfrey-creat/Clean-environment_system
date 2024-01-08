

```markdown
# MazingiraBora Command-Line Interpreter

## Overview
MazingiraBora is a command-line interpreter designed to facilitate booking services related to waste management. It enables clients to place bookings for services and allows garbage collection companies to accept these bookings.

## Features
- Create new instances of various classes: `Booking`, `User (Client)`, `Garbage_type`, `Garbage_collection_company`, `BaseModel`.
- Show information about instances based on class and ID.
- Place bookings for services as a client.
- Accept bookings as a garbage collection company.
- Update data sets for specific classes.

## Getting Started
### Prerequisites
- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/godfrey-creat/mazingirabora-cli.git
   cd mazingirabora-cli
   ```

2. Run the command-line interpreter:
   ```bash
   python console.py
   ```

## Usage
### Creating Instances
```bash
(mazingirabora) create User email="user@example.com" phone=1234567890 password="secret"
```

### Showing Instances
```bash
(mazingirabora) show User user_id
```

### Placing a Booking
```bash
(mazingirabora) place_booking client_id
```

### Accepting a Booking
```bash
(mazingirabora) accept_booking garbage_collection_company_id
```

### Updating Data Sets
```bash
(mazingirabora) update User user_id Amount_of_waste=10 pick_up_date="2023-12-31"
```

### Exiting the Console
```bash
(mazingirabora) quit
```

## Contributing
We welcome contributions! If you find a bug or have a feature request, please [open an issue](https://github.com/godfrey-creat/mazingirabora-cli/issues).

## License
This project is licensed under the [MIT License](LICENSE).
```

```markdown
# MazingiraBora Flask Web Application API

## Overview
MazingiraBora Flask Web Application API provides endpoints for managing GET, POST, PUT, and DELETE endpoints. It is built using Flask, a lightweight and extensible web framework for Python.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Teardown and Error Handling](#teardown-and-error-handling)

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Flask-CORS


### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/godfrey-creat/mazingirabora-api.git
   cd mazingirabora-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API
Run the following command to start the Flask web application API:
```bash
python api/v1/app.py
```
The API will be accessible at [http://localhost:5000](http://localhost:5000) by default.

### API Endpoints
- [Document each API endpoint with a brief description of its functionality]

## Configuration
- The API can be configured using environment variables:
  - `MAZINGIRABORA_API_HOST`: Host address (default: '0.0.0.0')
  - `MAZINGIRABORA_API_PORT`: Port number (default: 5000)

## Teardown and Error Handling
- The API automatically closes the storage connection after each request (see `teardown_flask` function).
- Custom error handlers are in place for 404 and 400 HTTP error codes
