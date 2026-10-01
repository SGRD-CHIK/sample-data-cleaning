# Sample project: cleaning a messy contact spreadsheet

> This is a practice project, not paid client work.

## The problem

The spreadsheet had 6 records. The same type of data was written in different ways:

- **Names:** `  іван  петренко ` and `ОЛЕНА КОВАЛЬ` (extra spaces, mixed letter case)
- **Phone numbers:** `0501234567`, `+380 (67) 123-45-67`, `380671234567`
- **Amounts:** `$1200`, `850 USD`, `300`
- **Dates:** 5 different formats, including the unclear `03/05/2026`

Because of this, it was impossible to find duplicate records.

## What I did

| Field | Result |
|---|---|
| Names | Removed extra spaces, unified letter case (`Іван Петренко`) |
| Emails | Lowercase, no spaces |
| Phone numbers | One format: `+380XXXXXXXXX` |
| Amounts | Plain numbers, no currency symbols |
| Dates | Format `YYYY-MM-DD` |
| Duplicates | Removed 2 duplicate records |

The duplicates became visible only after cleaning. While `іван  петренко` and `Іван Петренко` looked different, the spreadsheet could not see them as the same person.

## What the client needs to confirm

| Record | Issue | What I did |
|---|---|---|
| Maria Shevchenko, email | `maria@@example.com` has a double @ | Marked as `CHECK`, did not change it |
| Andrii Melnyk, email | Missing | Marked as `CHECK` |
| Maria Shevchenko, date | `12.04.2026` | I read it as 12 April, based on similar records. There is no direct proof |
| Amounts | `$` and `USD` | I assumed both mean US dollars |
| Phone numbers | Some had 9 digits (no leading zero) | I added `+380`. This is an assumption |

## How I solved an unclear date

The record `03/05/2026` could mean 3 May or 5 March. The spreadsheet had a duplicate of this record with the date `5 March 2026`. So I decided that it means **5 March**.

Google Sheets read this date wrongly (as 3 May) and showed no error. This is why dates should always be checked manually.

## Result

6 records → **4 unique records**.

Files: `before.csv` (original data), `after.csv` (cleaned data).
