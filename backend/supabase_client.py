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
        .upsert(
            {
                "email": email,
                "role": role,
                "location": location,
                "country": country,
                "preferred_language": preferred_language,
                "cv_storage_path": cv_storage_path,
                "active": True,
            },
            on_conflict="email",
        )
        .execute()
    )
    return response


def get_active_subscribers():
    response = supabase.table("subscribers").select("*").eq("active", True).execute()
    return response.data


def upload_cv(file_bytes: bytes, filename: str, email: str) -> str:
    suffix = os.path.splitext(filename)[1]
    path = f"{email}/cv{suffix}"
    supabase.storage.from_("resumes").upload(
        path=path, file=file_bytes, file_options={"upsert": "true"}
    )
    return path

def download_cv(cv_storage_path: str) -> bytes:
    response = supabase.storage.from_("resumes").download(cv_storage_path)
    return response

def get_subscriber_by_token(token: str) -> dict | None:
    response = supabase.table("subscribers").select("*").eq("token", token).execute()
    if not response.data:
        return None
    subscriber = response.data[0]
    if not subscriber["active"]:
        return None
    return subscriber

def get_subscriber_by_email(email: str) -> dict | None:
    response = supabase.table("subscribers").select("*").eq("email", email).execute()
    if not response.data:
        return None
    return response.data[0]

def create_subscriber_placeholder(email: str) -> dict:
    response = (
        supabase.table("subscribers")
        .upsert({"email": email, "active": True}, on_conflict="email")
        .execute()
    )
    return response.data[0]

def delete_subscriber(token: str) -> bool:
    subscriber = get_subscriber_by_token(token)
    if subscriber is None:
        return False
    cv_path = subscriber.get("cv_storage_path")
    if cv_path:
        supabase.storage.from_("resumes").remove([cv_path])
    supabase.table("subscribers").delete().eq("token", token).execute()
    return True