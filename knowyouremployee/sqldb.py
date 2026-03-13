import pyodbc

SERVER = "localhost"
DB_NAME = "KnowYourEmployeeDB"

CONN_MASTER = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

def connect(database: str) -> pyodbc.Connection:
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

def create_database():
    conn = pyodbc.connect(CONN_MASTER, autocommit=True)
    cursor = conn.cursor()

    cursor.execute(f"""
    IF DB_ID('{DB_NAME}') IS NULL
    BEGIN
        CREATE DATABASE [{DB_NAME}]
    END
    """)

    cursor.close()
    conn.close()
    print(f"Database '{DB_NAME}' checked/created successfully.")

def create_tables():
    conn = connect(DB_NAME)
    cursor = conn.cursor()

    # 1. Employees table
    cursor.execute("""
    IF OBJECT_ID('dbo.Employees', 'U') IS NULL
    BEGIN
        CREATE TABLE dbo.Employees (
            EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
            FormDate DATE NULL,
            EmployeeCode NVARCHAR(50) NULL,
            CardNo NVARCHAR(50) NULL,
            EmployeeName NVARCHAR(200) NOT NULL,
            Gender NVARCHAR(20) NULL,
            Department NVARCHAR(100) NULL,
            Designation NVARCHAR(100) NULL,
            DateOfJoining DATE NULL,
            DateOfBirth DATE NULL,
            MobileNo NVARCHAR(20) NULL,
            AlternateMobileNo NVARCHAR(20) NULL,
            EmailID NVARCHAR(150) NULL,
            AadhaarNo NVARCHAR(20) NULL,
            PANNo NVARCHAR(20) NULL,
            ESICNo NVARCHAR(50) NULL,
            EPFNo NVARCHAR(50) NULL,
            BloodGroup NVARCHAR(20) NULL,
            ReligionCaste NVARCHAR(100) NULL,
            FatherNameOccupation NVARCHAR(255) NULL,
            MotherNameOccupation NVARCHAR(255) NULL,
            MaritalStatus NVARCHAR(20) NULL,
            SpouseName NVARCHAR(200) NULL,
            MarriageAnniversary DATE NULL,
            Skills NVARCHAR(MAX) NULL,
            PermanentAddress NVARCHAR(MAX) NULL,
            CorrespondenceAddress NVARCHAR(MAX) NULL,
            NomineeDetails NVARCHAR(255) NULL,
            EmployeeSignatureDate DATE NULL,
            CreatedAt DATETIME DEFAULT GETDATE()
        )
    END
    """)

    # 2. Education details
    cursor.execute("""
    IF OBJECT_ID('dbo.EmployeeEducation', 'U') IS NULL
    BEGIN
        CREATE TABLE dbo.EmployeeEducation (
            EducationID INT IDENTITY(1,1) PRIMARY KEY,
            EmployeeID INT NOT NULL,
            Qualification NVARCHAR(100) NULL,
            BoardUniversityName NVARCHAR(255) NULL,
            YearOfPassing NVARCHAR(20) NULL,
            Remarks NVARCHAR(255) NULL,
            CreatedAt DATETIME DEFAULT GETDATE(),
            CONSTRAINT FK_EmployeeEducation_Employee
                FOREIGN KEY (EmployeeID) REFERENCES dbo.Employees(EmployeeID)
                ON DELETE CASCADE
        )
    END
    """)

    # 3. Previous experience details
    cursor.execute("""
    IF OBJECT_ID('dbo.EmployeeExperience', 'U') IS NULL
    BEGIN
        CREATE TABLE dbo.EmployeeExperience (
            ExperienceID INT IDENTITY(1,1) PRIMARY KEY,
            EmployeeID INT NOT NULL,
            OrganizationName NVARCHAR(200) NULL,
            Designation NVARCHAR(100) NULL,
            PeriodFrom DATE NULL,
            PeriodTo DATE NULL,
            Remarks NVARCHAR(255) NULL,
            CreatedAt DATETIME DEFAULT GETDATE(),
            CONSTRAINT FK_EmployeeExperience_Employee
                FOREIGN KEY (EmployeeID) REFERENCES dbo.Employees(EmployeeID)
                ON DELETE CASCADE
        )
    END
    """)

    # 4. Children details
    cursor.execute("""
    IF OBJECT_ID('dbo.EmployeeChildren', 'U') IS NULL
    BEGIN
        CREATE TABLE dbo.EmployeeChildren (
            ChildID INT IDENTITY(1,1) PRIMARY KEY,
            EmployeeID INT NOT NULL,
            ChildName NVARCHAR(200) NULL,
            Gender NVARCHAR(20) NULL,
            DateOfBirth DATE NULL,
            Age INT NULL,
            Education NVARCHAR(100) NULL,
            RemarksSchoolCollege NVARCHAR(255) NULL,
            CreatedAt DATETIME DEFAULT GETDATE(),
            CONSTRAINT FK_EmployeeChildren_Employee
                FOREIGN KEY (EmployeeID) REFERENCES dbo.Employees(EmployeeID)
                ON DELETE CASCADE
        )
    END
    """)

    # 5. Bank details
    cursor.execute("""
    IF OBJECT_ID('dbo.EmployeeBankDetails', 'U') IS NULL
    BEGIN
        CREATE TABLE dbo.EmployeeBankDetails (
            BankID INT IDENTITY(1,1) PRIMARY KEY,
            EmployeeID INT NOT NULL,
            BankName NVARCHAR(150) NULL,
            BranchName NVARCHAR(150) NULL,
            AccountNo NVARCHAR(50) NULL,
            IFSCCode NVARCHAR(20) NULL,
            NomineeName NVARCHAR(200) NULL,
            NomineeRelation NVARCHAR(100) NULL,
            CreatedAt DATETIME DEFAULT GETDATE(),
            CONSTRAINT FK_EmployeeBankDetails_Employee
                FOREIGN KEY (EmployeeID) REFERENCES dbo.Employees(EmployeeID)
                ON DELETE CASCADE
        )
    END
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("All tables checked/created successfully.")

if __name__ == "__main__":
    create_database()
    create_tables()
    print("Step 1 completed successfully.")