from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

from jose import jwt


def run(input: dict, context: dict) -> dict:
    secret = os.environ.get("JWT_SECRET", "")
    algorithm = os.environ.get("JWT_ALGORITHM", "HS256")

    if not secret:
        raise ValueError("JWT_SECRET environment variable is not set")

    sub = input.get("sub") or "test-user"
    groups = input.get("groups") or ["test-users"]
    expires_in = int(input.get("expires_in") or 3600)

    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "groups": groups,
        "iat": now,
        "exp": now + timedelta(seconds=expires_in),
    }

    token = jwt.encode(payload, secret, algorithm=algorithm)
    return {
        "token": token,
        "bearer": f"Bearer {token}",
        "sub": sub,
        "groups": groups,
        "expires_in": expires_in,
    }
