from typing import ClassVar

from langdetect import LangDetectException, detect


class LanguageDetector:
    LANGUAGE_NAMES: ClassVar[dict[str, list[str]]] = {
        "en": ["english"],
        "de": ["german", "deutsch"],
        "fr": ["french", "français"],
        "it": ["italian", "italiano"],
        "es": ["spanish", "español"],
        "nl": ["nederlands", "dutch"],
        "pt": ["portuguese", "português"],
    }

    def __init__(self, preferred_languages: str):
        self.preferred_languages = {
            language.lower() for language in preferred_languages
        }

    def matches_preferred_language(self, description: str) -> bool:
        try:
            detected_code = detect(description)
        except LangDetectException:
            return True
        allowed_names = self.LANGUAGE_NAMES.get(detected_code)
        if allowed_names is None:
            return False
        return bool(self.preferred_languages.intersection(allowed_names))

    def filter_jobs_by_language(self, jobs: list[dict]) -> list[dict]:
        return [j for j in jobs if self.matches_preferred_language(j["description"])]
