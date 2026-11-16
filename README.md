# Student Registration System

A Flask + SQLite web application for managing student registration and records at **K.L.E. Society's Jagadguru Tontadarya College (JT College), BCA Program**.

## Features

- **Student management**: add, view, edit and delete student records
- **Detailed records**: student info, contact details and parent/guardian details
- **Unique USN enforcement**: duplicate USNs are rejected with an error message
- **Dashboard & analytics**: total students and semester-wise distribution (doughnut and bar charts via Chart.js)
- **Responsive UI**: Bootstrap 5 and Font Awesome, themed in the college's red/dark colours
- **Persistent storage**: SQLite database, created automatically on first run

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python, Flask 2.3.3               |
| Database  | SQLite (`sqlite3` standard module) |
| Frontend  | Jinja2, Bootstrap 5.3, Font Awesome 6.4 |
| Charts    | Chart.js 3.9.1                    |
| Deployment| Gunicorn (included in requirements) |

## Project Structure

```
Student-Registration/
├── app.py                  # Flask app: routes and database logic
├── db.sqlite               # SQLite database
├── requirements.txt        # Python dependencies
├── README.md
└── templates/
    ├── home.html           # Student list and summary cards
    ├── add_students.html   # Add student form
    ├── edit_students.html  # Edit student form
    ├── details.html        # Single student profile
    └── dashboard.html      # Analytics dashboard
```

## Getting Started

### Prerequisites

- Python 3.8 or newer
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/shrishant2006/Student-Registration.git
cd Student-Registration

# 2. (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open **http://127.0.0.1:5000/** in your browser. The `students` table is created automatically when the app starts.

### Production

```bash
gunicorn app:app
```

> Note: the database is initialised in the `if __name__ == '__main__'` block. When running under Gunicorn, create the database once first with `python -c "import app; app.init_db()"`.

## Routes

| Route                          | Methods   | Description                    |
|--------------------------------|-----------|--------------------------------|
| `/`                            | GET       | Home: list all students        |
| `/students/add/`               | GET, POST | Add a new student              |
| `/students/edit/<id>/`         | GET, POST | Edit a student                 |
| `/students/delete/<id>/`       | GET       | Delete a student               |
| `/students/details/<id>/`      | GET       | View full student details      |
| `/students/dashboard/`         | GET       | Analytics dashboard            |

## Database Schema

**Table: `students`**

| Column         | Type      | Notes                     |
|----------------|-----------|---------------------------|
| `id`           | INTEGER   | Primary key, auto-increment |
| `name`         | TEXT      | Required                  |
| `usn`          | TEXT      | Required, unique          |
| `semester`     | INTEGER   | Required (1–6)            |
| `email`        | TEXT      | Required                  |
| `phone`        | TEXT      | Required                  |
| `address`      | TEXT      | Required                  |
| `parent_name`  | TEXT      | Required                  |
| `parent_phone` | TEXT      | Required                  |
| `parent_email` | TEXT      | Optional                  |
| `created_at`   | TIMESTAMP | Defaults to current time  |

## Usage

1. **Home**: see all registered students with USN, name, semester, email and phone.
2. **Add New Student**: fill in the student, contact and parent/guardian sections, then save.
3. **View / Edit / Delete**: use the action buttons in each table row.
4. **Dashboard**: open it from the navbar to see enrolment totals and semester-wise charts.

## Known Limitations / Future Improvements

- Deleting uses a GET request; switching to POST (with CSRF protection) would be safer.
- Editing a student to an existing USN is not yet handled gracefully (only the add form shows the duplicate error).
- No authentication; anyone with access can modify records.
- Phone numbers are not validated to be 10 digits on the server side.
- Add search, filtering by semester, pagination and CSV export.
- Set `debug=False` and use a proper WSGI server for deployment.

## License

This project is for educational purposes. © 2026 K.L.E. Society's JT College, BCA Program.# Book Management

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
