# Book Management

A simple web app for managing a book collection, built with **Flask** and **SQLite**. Add, view, edit and delete books, and see an analytics dashboard with a category chart and an animated 3D background.

Repository: https://github.com/ameerkhudavanda/book_management.git

## Features

- **Book list**: see all books, newest first, in a table
- **Add a book**: title, author, price and category, with validation
- **Book details**: full details of a single book, including when it was added
- **Edit a book**: update any field, with the same validation
- **Delete a book**: removal via POST with a confirmation prompt
- **Analytics dashboard**: total books, average price, maximum price, and a bar chart of books per category (Chart.js), over a Three.js animated background

## Tech Stack

| Layer     | Technology                         |
|-----------|------------------------------------|
| Backend   | Python 3, Flask                    |
| Database  | SQLite (`sqlite3` standard library)|
| Frontend  | Jinja2 templates, Bootstrap 5.3    |
| Charts    | Chart.js                           |
| 3D effect | Three.js (r128)                    |

Bootstrap, Chart.js and Three.js are loaded from CDNs, so an internet connection is needed for the styling, chart and animation.

## Project Structure

```
book_management/
├── app.py                  # Flask app: routes and database logic
├── README.md
├── storage/
│   └── db.sqlite           # SQLite database (created automatically)
└── templates/
    ├── home.html           # Book list
    ├── add_books.html      # Add book form
    ├── edit_books.html     # Edit book form
    ├── details.html        # Single book view
    └── dashboard.html      # Analytics dashboard
```

## Getting Started

### Prerequisites

- Python 3.8 or newer
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ameerkhudavanda/book_management.git
cd book_management

# 2. (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install flask

# 4. Run the app
python app.py
```

Open http://127.0.0.1:5000/ in your browser.

The `storage/` folder and the `books` table are created automatically on first run, so no manual database setup is needed.

## Routes

| Method     | URL                        | Description                  |
|------------|----------------------------|------------------------------|
| GET        | `/`                        | List all books               |
| GET, POST  | `/books/add/`              | Show / submit add form       |
| GET, POST  | `/books/edit/<id>/`        | Show / submit edit form      |
| GET        | `/books/details/<id>/`     | View one book                |
| POST       | `/books/delete/<id>/`      | Delete a book                |
| GET        | `/books/dashboard/`        | Analytics dashboard          |

## Database Schema

Table `books`:

| Column       | Type      | Notes                         |
|--------------|-----------|-------------------------------|
| `id`         | INTEGER   | Primary key, auto-increment   |
| `title`      | TEXT      | Required                      |
| `author`     | TEXT      | Required                      |
| `price`      | REAL      | Required, must be ≥ 0         |
| `category`   | TEXT      | Required                      |
| `created_at` | TIMESTAMP | Defaults to current timestamp |

## Validation

- All fields are required (checked in the browser and again on the server).
- Price must be a valid number that is not negative.
- Queries use parameter placeholders (`?`), which protects against SQL injection.

## Notes

- `app.run(debug=True)` is meant for development only. Turn debug mode off and use a production server (e.g. Gunicorn) when deploying.
