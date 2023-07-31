CREATE USER recipe_manager SUPERUSER;
ALTER USER recipe_manager WITH PASSWORD 'dydJUaETVRvrDFwc';

GRANT ALL PRIVILEGES ON DATABASE db_recipes TO recipe_manager;
GRANT ALL PRIVILEGES ON SCHEMA public TO recipe_manager;

ALTER ROLE recipe_manager SET client_encoding TO 'utf8';
ALTER ROLE recipe_manager SET default_transaction_isolation TO 'read committed';
ALTER ROLE recipe_manager SET timezone TO 'UTC';