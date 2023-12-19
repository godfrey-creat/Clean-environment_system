

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
   python mazingirabora.py
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
