import json
import pandas as pd
from typing import Any
from typing import cast



def read_transactions_from_csv(file_path: str) -> list[dict[str, Any]]:
    try:
        df = pd.read_csv(file_path)
        records = df.to_dict("records")
        return cast(list[dict[str, Any]], records)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []



from typing import Any, cast

def read_transactions_from_excel(file_path: str) -> list[dict[str, Any]]:
    try:
        df = pd.read_excel(file_path)
        return cast(list[dict[str, Any]], df.to_dict("records"))
    except (FileNotFoundError, ValueError):
        return []
