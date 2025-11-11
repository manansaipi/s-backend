# Movie App Backend

This is the backend API for the Movie App, built with FastAPI. It provides a secure API for user registration, login, and managing a personal list of favorite movies.


## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

Python 3.8+

pip (Python package installer)

(Optional) Docker

## 🛠️ How to Run Locally

Follow these steps to get the backend server running on your local machine.

### 1. Clone the Repository

Clone the repository to your local machine: [https://github.com/manansaipi/s-backend.git](https://github.com/manansaipi/s-backend.git)

```
git clone https://github.com/manansaipi/s-backend.git
```

Navigate into the project directory
```
cd s-backend
```

### 2. Create a Virtual Environment

```
python -m venv venv
```
Activate it
#### On Windows:
```
.\venv\Scripts\activate
```
#### On macOS/Linux:
```
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages using the requirements.txt file.
```
pip install -r requirements.txt
```

### 4. Set Up Your Database
This application requires a running database to function.

- Start your MySQL database server (e.g., from XAMPP, Docker, or your system).

- Ensure it is running on ```localhost``` (or ```127.0.0.1```) at port ```3306```.

- Access your database (e.g., via ```phpMyAdmin``` or a command-line tool) and create a new database named ```movieapplication```.

- Ensure you have a user with ```root``` as the username and ```root``` as the password, who has permission to access this new database.

(If you use different credentials, you will need to update them in the ```.env``` file in step 5.)

### 5. Set Up Environment Variables

This application uses a ```.env``` file to manage all its configuration.
Create a file named ```.env``` or you can copy ```.env.example``` 

```
# Database Connection
DATABASE_USER=root
DATABASE_PASSWORD=root
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=movieapplication

# JWT Authentication
SECRET_KEY=YeSyXalxkx59dKSZTj3n5hOYIFptVbGb
```

#### A strong, random string is required for security
SECRET_KEY=your_super_secret_random_key_here

(Your application logic in core/config.py must be set up to load this .env file, usually with a library like python-dotenv).

### 6. Run the Application

Once your dependencies are installed, you can run the application using uvicorn.

#### This command runs the app from the 'main.py' file
```
uvicorn main:app --reload
```

The application should now be running. You can access it at:

API URL: http://127.0.0.1:8000

API Docs (Swagger): http://127.0.0.1:8000/docs

API Docs (ReDoc): http://127.0.0.1:8000/redoc
