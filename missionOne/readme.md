This script fetches Ids from an Excel document, calls NYC Open Data API for each id,
processes the results, and exports them into an Excel file.

It handles:
- File errors
- Empty results
- Network errors
- Server-side errors


If running from source:

The script requires Python 3.10+ and the following packages:
- pandas
- requests
- openpyxl

You can install them via:

    pip install pandas requests openpyxl

Run:
python3.x source.py


If you are on Linux run the executable: (An executable version is available upon request.)

    ./executable
Make sure the Input file for ids 'Mortgages for Erwin.xlsx' is in the same directory as the executable.
The output file will be generated in the same directory.

