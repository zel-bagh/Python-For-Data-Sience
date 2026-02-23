# ==============================
# Imports
# ==============================

import requests
import pandas as pd
import sys

# ==============================
# Configuration Section
# ==============================

BASE_URL = "https://data.cityofnewyork.us/resource/636b-3b5g.json?document_id="
INPUT_FILE = "Mortgages for Erwin.xlsx"
OUTPUT_FILE = "output.xlsx"

# ========================
# Global session for HTTP requests
# ========================sudo python3.12 get-pip.py

session = requests.Session()

# ==============================
# Main Function
# ==============================

def main():
    """
    Orchestrates the full workflow:
    1. Load document IDs from spreadsheet
    2. Fetch data from API for each ID
    3. Parse and structure the results
    4. Save final output to spreadsheet
    """

    # Extracting ids
    try:
        # ids = ['2024072900182002']
        ids = load_document_ids(INPUT_FILE)
        print(f"Successfully loaded {len(ids)} document IDs.")

    except FileNotFoundError:
        print("Error: The input file was not found.")
        print("Please check the file path and try again.")
        sys.exit(1)

    except PermissionError:
        print("Error: The file is currently open or access is denied.")
        print("Please close the file and try again.")
        sys.exit(1)

    except ValueError:
        print("Data Error: Empty file | no 'DOCUMENT ID' | no ids | invalid ids")
        sys.exit(1)

    except Exception as e:
        print("Unexpected error occurred.")
        print(f"Details: {e}")
        sys.exit(1)

    # Collect data
    records = []
    for id in ids:
        try:
            records.extend(fetch_document_data(id))
            # print(records[0])

        except requests.exceptions.RequestException as e:
            print(f"Network/server error: {e}")
            print("Stopping execution. Try again later.")
            sys.exit(1)
    
    # Store data
    try:
        save_to_excel(records, OUTPUT_FILE)
    except Exception as e:
        print(f"Failed to save Excel file: {e}")
    return

# ==============================
# Excel Handling Functions
# ==============================

def load_document_ids(file_path):
    """
    Reads the input spreadsheet.
    
    Responsibilities:
    - Open Excel file
    - Extract the column 'DOCUMENT ID'
    - Clean values (whitespaces, NaN)
    - Return a list of document IDs as strings

    Returns:
        list[str]
    """

    # Read Excel file
    df = pd.read_excel(file_path, usecols=["DOCUMENT ID"], dtype = str)

    # Extract the column and clean ids
    ids = df["DOCUMENT ID"].dropna().str.strip().loc[lambda x: x != ""]

    if ids.empty:
        raise ValueError()
    return ids.tolist()


def save_to_excel(records, output_file):
    """
    Save collected rows to Excel.
    records: list of dictionaries
    """

    # Save records into output_file
    df = pd.DataFrame(records)
    df.to_excel(output_file, index=False)
    print(f"Data successfully saved to {output_file}")
    return


# ==============================
# API Handling Functions
# ==============================

def fetch_document_data(id):
    """
    Calls NYC Open Data API for a specific document_id.

    Responsibilities:
    - Make a get request.
    - Parse and sort data.

    Returns:
        list[dict]
    """

    # Request data
    response = session.get(BASE_URL + id, timeout=10)
    rows = []

    # Return Empty row for an id with no response from server
    try:
        response.raise_for_status()
        json_data = response.json()
        if not json_data:
            raise ValueError

    except ValueError or requests.exceptions.HTTPError:
        print(f"No records for id: {id}")
        rows.append({
            "document_id": id,
            "address_1": "",
            "party_type": "",
            "name": ""
        })
        return rows

    # Process JSON into rows    
    for item in json_data:
        row = {
            "document_id": item.get("document_id", id),
            "address_1": item.get("address_1", ""),
            "party_type": item.get("party_type", ""),
            "name": item.get("name", "")
        }
        rows.append(row)
    
    # Sort rows
    if not rows:
        return rows
    rows_sorted = sorted(rows, key=lambda x: (x["address_1"], x["party_type"]))

    return rows_sorted

# ==============================
# Entry Point
# ==============================

if __name__ == "__main__":
    main()