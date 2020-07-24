import os
from dotenv import load_dotenv
from functions.smmryAPI.smmryapi import SmmryAPI

load_dotenv()
SMRRY_API_KEY = os.getenv("SMMRY_API_KEY")


def get_summary(url):
    smmry = SmmryAPI(SMRRY_API_KEY)
    try:
        s = smmry.summarize(url, length=3)
        return s.sm_api_title, s.sm_api_content, s.sm_api_content_reduced
    except:
        return None, None, None
