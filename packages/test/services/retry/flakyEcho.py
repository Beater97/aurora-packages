from __future__ import annotations

import pathlib
import tempfile

_COUNTER_FILE = pathlib.Path(tempfile.gettempdir()) / "aurora_test_flaky_counter.txt"


def run(input: dict, context: dict) -> dict:
    fail_until = int(input.get("fail_until", 2))

    count = 0
    if _COUNTER_FILE.exists():
        try:
            count = int(_COUNTER_FILE.read_text().strip())
        except Exception:
            count = 0

    count += 1
    _COUNTER_FILE.write_text(str(count))

    if count < fail_until:
        raise RuntimeError(f"Intentional failure: attempt {count} of {fail_until}")

    _COUNTER_FILE.unlink(missing_ok=True)
    return {"value": input.get("value", "ok"), "succeeded_on_attempt": count}
