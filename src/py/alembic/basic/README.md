## Experiments
1. Initialise the project. 
    ```
    poetry init -n
    poetry add sqlmodel python-dotenv uvicorn alembic
    poetry run alembic init migrations     
    ```
2. Edit to use sqlite and sqlmodel. 
    ```
    # alembic.ini
    sqlalchemy.url = sqlite:///database.db
    # env.py
    import sqlmodel
    from sqlmodel import SQLModel
    ... import table objects
    target_metadata = SQLModel.metadata
    ```
