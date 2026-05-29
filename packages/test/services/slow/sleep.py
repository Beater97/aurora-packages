from __future__ import annotations

import time


def run(input: dict, context: dict) -> dict:
    seconds = float(input.get("seconds", 1))
    time.sleep(seconds)
    return {"value": "done", "slept_seconds": seconds}
