#TaskApp

TaskApp is a simple task manager web application built with Flask. Users can add, update, and delete tasks. Each task includes content and a timestamp, stored in a SQLite database. The frontend is styled using SCSS for a clean and responsive UI.

## Features

- Add new tasks  
- Edit existing tasks  
- Delete tasks  
- View creation date of tasks  
- Clean and responsive design using SCSS

## Tech Stack

- Python 3  
- Flask  
- Flask-SQLAlchemy  
- SQLite  
- Flask-SCSS  
- HTML / Jinja2  
- SCSS (Sass)

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Sefagor/TaskApp.git
   cd TaskApp
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   venv\Scripts\activate        # On Windows
   # OR
   source venv/bin/activate     # On Mac/Linux
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:

   ```bash
   python app.py
   ```

5. **Access the app**:

   Open your browser and go to:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```
TaskApp/
│
├── static/
│   └── styles.scss
├── templates/
│   ├── base.html
│   ├── index.html
│   └── edit.html
├── app.py
├── requirements.txt
└── README.md
```

## Notes

- SCSS compilation requires a watcher. You can use the Sass CLI:

   ```bash
   sass --watch static/styles.scss static/styles.css
   ```

- If you encounter issues with database creation, ensure `database.db` is correctly configured and that `db.create_all()` is called within the app context.

## License

This project is licensed under the MIT License.
