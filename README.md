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
## LICENSE
```text
MIT License

Copyright (c) 2026 Mansurii

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```