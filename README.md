
# Automobile Service Station Management System

## Introduction

The **Automobile Service Station Management System** is a terminal-based application designed to manage customer records, service schedules, and staff logins for an automobile service station. The system allows users to add new customers, schedule services, and search or view customer details. It also provides a login and signup mechanism for staff, ensuring secure access to the system.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributors](#contributors)
- [License](#license)

## Features

- **Customer Registration**: Add new customer details such as name, address, phone number, vehicle details, and schedule service appointments.
- **Service Scheduling**: Update the schedule for customer services, including date, time, duration, and type of service.
- **Search and View**: Search for specific customers or view all customer records in a formatted table.
- **Login and Signup**: Secure staff login and signup functionality to ensure only authorized personnel can access the system.
- **Database Integration**: Uses a MySQL database to store customer and staff information.

## Installation

### Prerequisites
1. **Python 3.x** installed on your system.
2. **MySQL** server running locally.
3. Install the required Python packages by running:
    ```bash
    pip install mysql-connector-python prettytable
    ```

### MySQL Setup
1. Create a MySQL database named `assms`.
2. Use the provided SQL file (`mysql_query.sql`) to set up the necessary tables:
    - `customer_details`: Stores customer information.
    - `staffdatabase`: Stores staff login credentials.

Run the following command to execute the SQL setup:
```bash
mysql -u root -p assms < mysql_query.sql
```

## Usage

1. **Run the application**:
   ```bash
   python csproject2.py
   ```

2. **Login or Signup**: Upon starting the program, you will be prompted to log in or sign up as a staff member.
   - If you are a new staff member, sign up with your details.
   - Existing staff can log in using their credentials.

3. **Main Menu**:
   - `1. Add New Customer`: Register a new customer.
   - `2. Schedule`: Schedule or update a service for an existing customer.
   - `3. Search`: Search for a specific customer or view all records.
   - `4. Exit`: Exit the program.

## Dependencies

The project requires the following Python packages:
- `mysql-connector-python`: To handle MySQL database connections.
- `prettytable`: For displaying records in a formatted table.

Install them via:
```bash
pip install mysql-connector-python prettytable
```

## Configuration

In the script, ensure that the database connection parameters (such as host, user, password, and database name) are set correctly in the `databaseConnection` function:
```python
conn = sql_con.connect(host='localhost', user='root', passwd='YOUR_PASSWORD', database='assms')
```

Replace `YOUR_PASSWORD` with your actual MySQL root password.

## Examples

**Adding a new customer**:
- Follow the menu prompts to input the customer details, such as name, address, phone number, and service details.

**Viewing customer records**:
- Select the "View" option to display all customer records in a table.

**Scheduling a service**:
- Use the "Schedule" option to set or update a service appointment for an existing customer by providing the service date, time, and type.

## Contributors

- **<a href="https://github.com/aryan04dbz">Aryan Jha</a>** - Developer

---

Let me know if you need any additional sections or adjustments!