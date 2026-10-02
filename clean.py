import pandas as pd
from datetime import datetime

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

df = pd.read_csv("before.csv", dtype=str)

df["name"] = df["name"].str.split().str.join(" ").str.title()
df["email"] = df["email"].str.strip().str.lower()

pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

is_valid = df["email"].fillna("").str.match(pattern)

df["email_status"] = is_valid.map({True: "OK", False: "CHECK"})

def fix_phone(digits):
    if len(digits) == 9:
        return "+380" + digits
    if len(digits) == 10 and digits.startswith("0"):
        return "+38" + digits
    if len(digits) == 12 and digits.startswith("380"):
        return "+" + digits
    return  "CHECK"

only_digits= df["phone"].fillna("").str.replace(r"\D", "", regex=True)
df["phone"] = only_digits.apply(fix_phone)

df["amount"] = df["amount"].fillna("").str.replace(r"[^0-9.]", "", regex=True)
df["amount"] = pd.to_numeric(df["amount"])



DATE_FORMATS = [
    "%Y-%m-%d", # 2026-05-03
    "%Y/%m/%d", # 2026/04/15
    "%d %B %Y", # 5 March 2026
    "%d.%m.%Y", # 12.04.2026 (крапка: спочатку день)
    "%m/%d/%Y", # 03/05/2026 (скісна риска: спочатку місяць)
]

def fix_date(text):
    text = str(text).strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return "CHECK"

df["date"] = df["date"].apply(fix_date)

result = df[["name", "email", "email_status", "phone", "amount", "date"]]

rows_before = len(result)
result = result.drop_duplicates().reset_index(drop=True)
rows_after = len(result)

result.to_csv("after_python.csv", index=False, encoding="utf-8-sig")
result.to_excel("after_python.xlsx", index=False)

print(result)

print(f"Було рядків: {rows_before}, стало: {rows_after}, видалено дублікатів: {rows_before - rows_after}")