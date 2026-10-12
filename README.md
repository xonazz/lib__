# Biblioteca — CRUD em Django

## Como rodar
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations acervo
python manage.py migrate
python manage.py createsuperuser   # opcional, para /admin
python manage.py runserver
```
Acesse http://127.0.0.1:8000

## Banco online (PostgreSQL)
Defina as variáveis de ambiente antes de rodar `migrate`:
`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
(e instale `psycopg[binary]`). Sem elas, usa SQLite local.
