def run(input: dict, context: dict) -> dict:
    a = float(input.get("a", 0))
    b = float(input.get("b", 0))
    return {"result": a + b}
