format:
	black --line-length 119 --target-version py310 .

init:
	PYTHONPATH=src python src/init_db.py

run:
	PYTHONPATH=src uvicorn main:app --reload
