# School Management System

A comprehensive Python-based School Management System built with Tkinter GUI, SQL Server database, and Object-Oriented Programming principles.

## Features

### Core Functionality
- **Student Management**: Register, update, delete, and manage students
- **Teacher Management**: Add and manage teachers with subjects
- **Attendance Tracking**: Record and track student attendance
- **Fee Management**: Manage student fees and payment status
- **Performance Tracking**: Record and analyze academic performance
- **GPA Calculation**: Automatic GPA calculation based on marks
- **Report Generation**: Comprehensive performance reports for students

### Authentication & Security
- Student login system with password protection
- Admin panel with secure authentication (password: `admin123`)
- Role-based access control

### User Interface
- Modern Tkinter-based GUI
- Intuitive navigation between screens
- Multiple views for students, teachers, and administrators
- Tree view displays for data management

### Database
- SQL Server integration using pyodbc
- Normalized database schema with proper relationships
- Cascade delete to maintain referential integrity
- CRUD operations for all entities

## Technology Stack

- **Language**: Python 3
- **GUI Framework**: Tkinter (ttk for modern widgets)
- **Database**: SQL Server with pyodbc driver
- **Testing**: Python unittest with mocking
- **Version Control**: Git & GitHub

## Project Structure

```
ERP_Portal/
├── ERP_pyodbc.py          # Database operations and CRUD functions
├── models.py              # OOP classes (Student, Teacher, Performance, etc.)
├── ERP_GUI.py             # Tkinter GUI implementation
├── ERP.py                 # Main entry point
├── unitTestStud.py        # Unit tests
├── README.md              # This file
└── __pycache__/           # Python cache files
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- SQL Server with ODBC Driver 17
- pip (Python package manager)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mmubashirdev/python.git
   cd python/ERP_Portal
   ```

2. **Install Dependencies**
   ```bash
   pip install pyodbc
   ```

3. **Configure Database Connection**
   - Ensure SQL Server is running with ODBC Driver 17
   - Update connection string in `ERP_pyodbc.py` if needed:
     ```python
     "Server={localhost\\MSSQLSERVER01};"
     ```

4. **Run the Application**
   ```bash
   python ERP_GUI.py
   ```

## Usage

### Student Features
- **Login**: Use registered credentials
- **View Performance**: See academic records with marks and grades
- **View Attendance**: Check attendance history
- **View Fees**: See fee payment status
- **Generate Report**: Download comprehensive performance report

### Admin Features
- **Admin Password**: `admin123`
- **Manage Students**: Add, view, delete students
- **Manage Teachers**: Add, view, delete teachers
- **Manage Attendance**: Record attendance for all students
- **Manage Fees**: Add and update fee records
- **Manage Performance**: Record student performance

### Grading System
- **A**: 90-100 marks
- **B**: 80-89 marks
- **C**: 70-79 marks
- **D**: 60-69 marks
- **F**: 0-59 marks

## Database Schema

### Tables

#### Students
- id (Primary Key)
- name (NVARCHAR)
- grade (NVARCHAR)
- password (NVARCHAR)

#### Teachers
- id (Primary Key)
- name (NVARCHAR)
- subject (NVARCHAR)

#### Attendance
- id (Primary Key)
- student_id (Foreign Key)
- date (DATE)
- status (Present/Absent)

#### Fees
- id (Primary Key)
- student_id (Foreign Key)
- amount (DECIMAL)
- status (Paid/Pending)

#### Performance
- id (Primary Key)
- student_id (Foreign Key)
- subject (NVARCHAR)
- marks (INT)

## Testing

Run unit tests with:
```bash
python -m unittest unitTestStud.py
```

### Test Coverage
- Student CRUD operations
- Teacher management
- Performance tracking and GPA calculation
- Attendance management
- Fee management
- Report generation
- Data integrity and cascade deletes

## OOP Design

### Classes

- **Student**: Represents a student with CRUD operations and GPA calculation
- **Teacher**: Represents a teacher with subject association
- **Performance**: Represents academic performance with grade calculation
- **Attendance**: Represents attendance records
- **Fee**: Represents fee information and payment status
- **School**: Factory/Manager class for coordinating all operations

## Key Functions

### Database Layer (ERP_pyodbc.py)
- `get_con()`: Establish database connection
- `init_db()`: Initialize database
- `create_tables()`: Create all necessary tables
- `calculate_student_gpa()`: Calculate GPA from marks
- `get_performance_report()`: Generate comprehensive report

### Models Layer (models.py)
- `Student.verify_login()`: Authenticate student
- `Performance.get_grade()`: Get letter grade from marks
- `School.generate_performance_report()`: Create detailed report

## Screenshots

### Login Screen
- Student login with name and password
- New student registration
- Admin access option

### Student Dashboard
- View academic performance
- Check attendance records
- Monitor fee payments
- Generate comprehensive report

### Admin Dashboard
- Complete CRUD operations for all entities
- Attendance recording
- Fee management
- Performance tracking

## Security Features

- Passwords stored in database
- Admin panel with password protection
- Role-based access control (Student vs Admin)
- Input validation and error handling

## Future Enhancements

- Email notifications for attendance and fees
- Parent portal for monitoring
- Analytics dashboard for administrators
- Mobile app integration
- Advanced reporting and analytics
- Automatic fee reminders
- Certificate generation

## Git Commits

### Commit 1: Initial Setup
- Created project structure
- Implemented database layer with CRUD operations
- Created OOP models

### Commit 2: GUI and Features Implementation
- Developed comprehensive Tkinter GUI
- Implemented all management features
- Added unit tests
- Created documentation

## Troubleshooting

### Database Connection Issues
- Verify SQL Server is running
- Check ODBC Driver 17 installation
- Update server name in connection string

### Import Errors
- Ensure all files are in the same directory
- Install pyodbc: `pip install pyodbc`

### GUI Issues
- Use Python 3.8 or higher
- Ensure Tkinter is installed with Python

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Mubashir Dev**
- GitHub: [@mmubashirdev](https://github.com/mmubashirdev)
- Repository: [python](https://github.com/mmubashirdev/python)

## Support

For support, email your queries or create an issue on GitHub.

---

**Last Updated**: December 4, 2025
**Version**: 1.0.0
