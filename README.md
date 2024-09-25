# COVID Management System

A simple COVID management system for health organizations using MySQL and Python. This system allows the management of patients and staff records, facilitates login for authorized users, and provides a self-assessment test for COVID-19 symptoms.

## Features

- **Login System**: Admins can create a new account if no user exists. Existing users can log in to manage records.
- **Manage Patients**: Add, view, and remove patient records.
- **Manage Staff**: Add, view, and remove staff members.
- **Change Password**: Logged-in admins can change their account password.
- **COVID-19 Precautions**: Information on preventive measures.
- **Self-Assessment Test**: A simple test to check for COVID-19 symptoms based on user input.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Database Structure](#database-structure)
5. [Self-Assessment Test](#self-assessment-test)
6. [Contributing](#contributing)

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.x**
- **MySQL**
- **MySQL Connector for Python** (`mysql-connector-python`)

You can install the required MySQL connector by running:

```bash
pip install mysql-connector-python
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/covid-management-system.git
   ```

2. **Configure MySQL**:
   
   - Ensure your MySQL server is running.
   - Update the MySQL connection details (username and password) in the script if necessary.
   - The script will automatically create the database `covid_management` and its required tables.

3. **Run the Application**:
   
   ```bash
   python app.py
   ```

## Usage

### Login/Register

- On the first run, you’ll be prompted to create a new admin account.
- If an admin account exists, use the login option to access the system.
- Once logged in, you can:
  - Add/view/remove patient records.
  - Add/view/remove staff records.
  - Change your password.
  - Log out.

### Self-Assessment Test

Non-registered users can take a simple self-assessment test by selecting the option from the main menu. Based on the answers, the system will suggest whether to seek medical advice.

## Database Structure

The database consists of four tables:

- `staff`: Stores information about hospital staff.
  - Fields: `sno`, `name`, `age`, `gender`, `post`, `salary`
  
- `patients`: Stores information about COVID-19 patients.
  - Fields: `sno`, `name`, `age`, `gender`, `date`

- `login`: Stores admin login credentials.
  - Fields: `admin`, `password`
  
- `sno`: Keeps track of the serial numbers of patients and staff.
  - Fields: `patient`, `staff`

## Self-Assessment Test

The self-assessment test evaluates a user’s symptoms based on the following questions:

1. Cough (dry or wet)
2. Sneezing
3. Pain in the body
4. Weakness
5. Mucus
6. Temperature
7. Breathing difficulty

Based on the answers provided, the system gives feedback on whether the user should seek medical help.

## Contributing

If you'd like to contribute to the project:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes.
4. Push the changes to your branch: `git push origin feature-branch-name`.
5. Submit a pull request.

