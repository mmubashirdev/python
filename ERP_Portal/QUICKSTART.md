# School Management System - Quick Start Guide

## Project Overview

A complete School Management System built with Python, featuring:

- **GUI**: Modern Tkinter interface with student and admin portals
- **Database**: SQL Server with pyodbc integration
- **OOP**: Fully object-oriented design with 6 core classes
- **Testing**: Comprehensive unit tests with 20+ test cases
- **Features**: Student management, attendance, fees, performance tracking, report generation

## File Structure

```
ERP_Portal/
├── ERP_pyodbc.py        [Database Layer] - All database operations and CRUD functions
├── models.py            [OOP Layer] - Student, Teacher, Performance, Attendance, Fee, School classes
├── ERP_GUI.py           [GUI Layer] - Complete Tkinter implementation
├── ERP.py               [Entry Point] - Main application launcher
├── unitTestStud.py      [Tests] - 20+ unit tests for core functionality
└── README.md            [Documentation] - Detailed setup and usage guide
```

## Key Features Implemented

### ✅ Database Layer (ERP_pyodbc.py)

- [x] Database initialization and table creation
- [x] CRUD operations for all 5 tables (Students, Teachers, Attendance, Fees, Performance)
- [x] GPA calculation: `calculate_student_gpa()`
- [x] Performance report generation: `get_performance_report()`
- [x] Cascade delete for data integrity

### ✅ OOP Models (models.py)

- [x] **Student** class: Login, GPA calculation, attendance/fee/performance retrieval
- [x] **Teacher** class: Subject management
- [x] **Performance** class: Grade calculation (A-F system)
- [x] **Attendance** class: Record management
- [x] **Fee** class: Amount and status tracking
- [x] **School** class: Centralized management and report generation

### ✅ GUI (ERP_GUI.py)

- [x] Student login screen with registration
- [x] Admin panel (password: `admin123`)
- [x] Student dashboard: Performance, Attendance, Fees, Report views
- [x] Admin management: Students, Teachers, Attendance, Fees, Performance
- [x] Modern Tkinter with ttk widgets
- [x] Treeview displays for data management
- [x] Dialog boxes for data entry

### ✅ Unit Testing (unitTestStud.py)

- [x] Student operations (add, login, retrieve)
- [x] Teacher operations
- [x] Performance tracking and GPA calculation
- [x] Attendance management
- [x] Fee management
- [x] Report generation
- [x] Data integrity (cascade deletes)
- [x] Boundary value testing

## How to Run

### Step 1: Install Dependencies

```bash
pip install pyodbc
```

### Step 2: Start GUI Application

```bash
python ERP_GUI.py
```

### Step 3: Run Unit Tests

```bash
python -m unittest unitTestStud.py
```

## Default Test Credentials

### Student Login

- Register a new student using "Add New Student" button
- Use registered credentials to login

### Admin Panel

- Click "Admin Panel" on login screen
- Password: `admin123`

## Grading System

| Grade | Range  |
| ----- | ------ |
| A     | 90-100 |
| B     | 80-89  |
| C     | 70-79  |
| D     | 60-69  |
| F     | 0-59   |

## Database Schema

### 5 Tables with Relationships:

1. **Students** (id, name, grade, password)
2. **Teachers** (id, name, subject)
3. **Attendance** (id, student_id→Students, date, status)
4. **Fees** (id, student_id→Students, amount, status)
5. **Performance** (id, student_id→Students, subject, marks)

## Git Commits

### Commit 1: Models & Database

```
7a84f60 - feat: Add OOP models and expanded database layer for School Management System
```

- Created models.py with OOP classes
- Expanded ERP_pyodbc.py with all CRUD operations
- Implemented GPA calculation and report generation

### Commit 2: GUI & Tests

```
44289cc - feat: Implement comprehensive GUI and unit tests for School Management System
```

- Complete Tkinter GUI implementation
- Student and admin portals with full features
- 20+ comprehensive unit tests
- Documentation and README

## Student Features

1. **View My Performance**

   - Subject-wise marks and grades
   - GPA display

2. **View My Attendance**

   - Date-wise attendance status
   - Attendance history

3. **View My Fees**

   - Fee amounts and payment status
   - Payment tracking

4. **Generate Report**
   - Comprehensive performance report
   - Attendance percentage
   - Fee summary
   - Subject-wise analysis

## Admin Features

1. **Manage Students**

   - Add new students
   - View all students
   - Delete students (cascade delete)

2. **Manage Teachers**

   - Add teachers
   - View all teachers
   - Delete teachers

3. **Manage Attendance**

   - Record attendance
   - View student attendance history

4. **Manage Fees**

   - Add fee records
   - Update payment status
   - Track pending fees

5. **Manage Performance**
   - Record student marks
   - View performance by student
   - Track grades

## Unit Tests Overview

**Total: 20+ Test Cases**

### Coverage by Module:

- Student Operations: 5 tests
- Teacher Operations: 3 tests
- Performance Tracking: 4 tests
- Attendance Management: 2 tests
- Fee Management: 3 tests
- Report Generation: 1 test
- School Management: 3 tests
- Data Integrity: 3 tests

### Test Execution:

```bash
python -m unittest unitTestStud.py -v
```

## Key OOP Principles Used

1. **Encapsulation**: Each class manages its own data and operations
2. **Inheritance**: Common functionality in parent classes
3. **Polymorphism**: Consistent interface across different entity types
4. **Abstraction**: Complex database operations hidden behind simple methods

## Error Handling

- Input validation for all forms
- Try-catch blocks for database operations
- User-friendly error messages via dialogs
- Graceful handling of missing data

## Security Features

- Password protection for students
- Admin authentication (hardcoded for demo)
- Input sanitization
- Role-based access control

## Performance Optimizations

- Efficient database queries
- Lazy loading of data
- Proper resource cleanup
- Connection pooling via pyodbc

## Future Enhancements

- [ ] Email notifications
- [ ] SMS alerts
- [ ] Parent portal
- [ ] Mobile app integration
- [ ] Advanced analytics dashboard
- [ ] Document generation (certificates)
- [ ] User authentication with hashing
- [ ] Database backup and recovery

## Troubleshooting

### Issue: Database connection failed

**Solution**: Ensure SQL Server is running and check ODBC driver installation

### Issue: Tkinter not found

**Solution**: `pip install tk` or reinstall Python with Tkinter

### Issue: pyodbc import error

**Solution**: `pip install pyodbc --upgrade`

## GitHub Repository

**Owner**: mmubashirdev
**Repository**: python
**Path**: /ERP_Portal

**URL**: https://github.com/mmubashirdev/python/tree/main/ERP_Portal

## Version Information

- **Version**: 1.0.0
- **Python**: 3.8+
- **Last Updated**: December 4, 2025
- **Status**: Production Ready

## Support & Contribution

For issues, feature requests, or contributions, please visit the GitHub repository.

---

**Project Status**: ✅ Complete and Tested
**All Requirements Met**: ✅ Yes
