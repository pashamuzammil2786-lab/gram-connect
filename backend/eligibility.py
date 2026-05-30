from __future__ import annotations

from typing import Any

from database.db import get_schemes


ANY_VALUE = "Any"


def _matches_text(rule_value: str, user_value: str) -> bool:
    return rule_value == ANY_VALUE or rule_value.strip().lower() == user_value.strip().lower()


def _match_scheme(user_data: dict[str, Any], scheme: dict[str, Any]) -> tuple[bool, list[str], list[str]]:
    reasons: list[str] = []
    missing: list[str] = []

    age = int(user_data["age"])
    income = int(user_data["income"])

    if int(scheme["min_age"]) <= age <= int(scheme["max_age"]):
        reasons.append(f"age is within {scheme['min_age']}-{scheme['max_age']}")
    else:
        missing.append(f"age must be between {scheme['min_age']} and {scheme['max_age']}")

    if income <= int(scheme["income_limit"]):
        reasons.append(f"income is under Rs. {int(scheme['income_limit']):,}")
    else:
        missing.append(f"income must be Rs. {int(scheme['income_limit']):,} or less")

    for field in ("gender", "occupation", "state", "caste", "disability", "education"):
        if _matches_text(str(scheme[field]), str(user_data[field])):
            if scheme[field] != ANY_VALUE:
                reasons.append(f"{field} matches {scheme[field]}")
        else:
            missing.append(f"{field} must be {scheme[field]}")

    return not missing, reasons, missing


def check_eligibility(user_data: dict[str, Any]) -> list[dict[str, Any]]:
    eligible_schemes: list[dict[str, Any]] = []

    for scheme in get_schemes():
        is_eligible, reasons, missing = _match_scheme(user_data, scheme)
        if is_eligible:
            eligible_schemes.append(
                {
                    "scheme_name": scheme["scheme_name"],
                    "description": scheme["description"],
                    "benefits": scheme["benefits"],
                    "application_process": scheme["application_process"],
                    "application_link": scheme["application_link"],
                    "reasons": reasons,
                }
            )

    return eligible_schemes


def explain_near_matches(user_data: dict[str, Any], limit: int = 3) -> list[dict[str, Any]]:
    scored: list[dict[str, Any]] = []
    for scheme in get_schemes():
        is_eligible, reasons, missing = _match_scheme(user_data, scheme)
        if not is_eligible:
            scored.append(
                {
                    "scheme_name": scheme["scheme_name"],
                    "description": scheme["description"],
                    "missing": missing,
                    "score": len(reasons),
                }
            )

    return sorted(scored, key=lambda item: item["score"], reverse=True)[:limit]