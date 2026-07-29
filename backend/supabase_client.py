import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SECRET_KEY")
supabase: Client = create_client(url, key)


def add_subscriber(
    email: str,
    role: str,
    location: str,
    country: str,
    preferred_language: str,
    cv_storage_path: str,
):
    response = (
        supabase.table("subscribers")
        .insert(
            {
                "email": email,
                "role": role,
                "location": location,
                "country": country,
                "preferred_language": preferred_language,
                "cv_storage_path": cv_storage_path,
                "active": True,
            }
        )
        .execute()
    )
    return response


def get_active_subscribers():
    response = supabase.table("subscribers").select("*").eq("active", True).execute()
    return response.data


def upload_cv(file_bytes: bytes, filename: str, email: str) -> str:
    path = f"{email}/{filename}"
    supabase.storage.from_("resumes").upload(
        path=path, file=file_bytes, file_options={"upsert": "true"}
    )
    return path

