# notes
# SmartNotes Django Project

Welcome to **SmartNotes**! This is a Django-based web application for managing notes, featuring user authentication, note creation, editing, liking, and more.

## Features

- User registration, login, and logout
- Create, update, and delete notes
- Like notes
- Responsive Bootstrap UI

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Virtual environment tool: `venv` or `virtualenv`

## Installation

### 1. Clone the Repository

```
git clone https://github.com/jsuj1th/notes
cd STOREFRONT
```


### 2. Create and Activate a Virtual Environment

**On Windows:**

```
python -m venv venv
venv\Scripts\activate
```


**On macOS/Linux:**
```
python3 -m venv venv
source venv/bin/activate
```


### 3. Install Dependencies

``` 
pip install -r requirements.txt 
```

## Database Setup

### 4. Apply Migrations
```
 python manage.py migrate 
 ```


### 5. Create a Superuser (Admin)


```
 python manage.py createsuperuser
 ```


Follow the prompts to set up your admin account.

## Running the Project

### 6. Start the Development Server


```
 python manage.py runserver
 ```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register or log in to your account.
- Create, edit, and delete notes.
- Like notes using the like button.
- Use the navigation bar to access different features.

## Common Commands

| Command                          | Description                       |
|---------------------------------|---------------------------------|
| `python manage.py runserver`     | Start the development server     |
| `python manage.py migrate`       | Apply database migrations        |
| `python manage.py makemigrations` | Create new migrations            |
| `python manage.py createsuperuser` | Create an admin user             |

## Troubleshooting

- If you get a `ModuleNotFoundError`, ensure all dependencies are installed.
- For database errors, try running `python manage.py migrate` again.
- For static files, run `python manage.py collectstatic` (if deploying).

## License

This project is for educational purposes.

## Contributing

Pull requests and suggestions are welcome!

## Contact

For questions or support, open an issue or contact the maintainer.

**Happy coding!**
