from pathlib import Path

BASE_APP_DIR = Path(__file__).parent

DATABASE = {
    "provider": "sqlite",
    "filename": str(BASE_APP_DIR / "db.sqlite"),
    "create_db": True,
}
