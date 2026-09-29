# Hotel Reservation API

A full-stack hotel reservation application with a separate backend API and frontend application.

## Project Structure

```text
📁 hotel_reservation_api/
│
├── 📁 backend/
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
│
├── 📁 frontend/
│   ├── 📁 css/
│   │   └── styles/
│   │
│   ├── 📁 js/
│   │   └── .gitkeep
│   │
│   └── index.html
│
├── .gitignore
├── LICENSE
└── README.md
```
## Tech Stack

| Technology | Purpose |
|:-----------|:--------|
| Python 3.10+ | Backend development |
| FastAPI | REST API framework |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |
| JavaScript | Frontend functionality |

## Project Setup

### Clone the Repository

```bash
git clone <repository-url>
cd hotel_reservation_api
```

### Environment Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
uv venv
```

Activate the virtual environment:

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies from `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

### Run the Application

Start the FastAPI development server:

```bash
uv run fastapi dev
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```
