import requests

EDUCATION_CATEGORY_ID = 9  # General Knowledge category (most educational)
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"