# StampAlbum Database Converter (MS Access to SQLite)

A Python-based utility designed to migrate philatelic (stamp collection) databases from Microsoft Access (`.mdb`) format to modern, lightweight SQLite (`.db`) databases.

## 📋 Overview

This tool automates the process of converting multi-file legacy Microsoft Access databases into SQLite format. It handles two primary types of databases within the philatelic management system:

1. **Master Database (`master.mdb`):** Stores application-wide settings, storage box/sleeve dimensions (`StampBox`), UI messages, and translations.
2. **Country-Specific Databases (`<Country>.mdb`):** Stores catalog data for individual countries, including stamp descriptions, face values, colors, series, issue years, and physical dimensions.

## 🛠️ Features

- **Automated Directory Scanning:** Scans the `databases/` folder for all country `.mdb` files.
- **Dynamic Table Creation:** Automatically builds matching SQLite schemas (`stamp_list` and `StampBox`) if they do not already exist.
- **Data Sanitization:** Cleans and escapes special characters (such as single quotes) to prevent SQL syntax errors during transfer.
- **Access Query Interface:** Includes a helper class (`Databases.py`) with pre-built SQL routines to query stamp information, dimensions, and matching storage pockets.

## 🚀 Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**
- **Microsoft Access Database Engine Driver** (32-bit or 64-bit depending on your Python installation)
- Python package: `pyodbc`

Install the required Python packages via pip:

```bash
pip install pyodbc
```

## 📁 Repository Structure

```text
.
├── databases/              # Directory containing input .mdb files
│   ├── master.mdb          # Main database containing storage & UI data
│   ├── France.mdb          # Example country database
│   └── ...                 # Additional country databases
├── Databases.py            # DB class managing ODBC connections & queries
├── main.py                 # Migration entry point
└── README.md               # Project documentation
```

## 💻 Usage

1. Place all your `.mdb` files (e.g., `master.mdb`, `France.mdb`, `USA.mdb`) into the `databases/` directory.
2. Run the main migration script:

```bash
python main.py
```

3. Upon completion, the script will generate corresponding `.db` files (e.g., `master.db`, `France.db`) in the root project directory.

## 📝 Database Schemas

### `stamp_list` (Country Database)
Stores details for individual stamps:
- `key` (INTEGER): Unique identifier
- `NBR` (TEXT): Stamp catalog number
- `SUB_NBR` (TEXT): Sub-number / variety
- `SEQUENCE` (INTEGER): Display order
- `year` (TEXT): Issue year
- `valuecolor` (TEXT): Face value and color description
- `stampDescription1` / `stampDescription` (TEXT): Stamp details
- `width` / `height` (TEXT): Dimensions
- `country`, `Type`, `Serie`, `ASCII_SEQ` (TEXT): Metadata

### `StampBox` (Master Database)
Stores information about storage pages and pockets:
- `id` (INTEGER): Unique identifier
- `pochette` (TEXT): Pocket type/reference
- `designation` (TEXT): Description
- `LX` / `LY` (INTEGER): Pocket width and height dimensions

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).