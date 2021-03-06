import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context


def append_path():
    """Set python path dinamically."""
    # For now we are changing %PYTHONPATH dinamically but later won't be needed
    # because we will use poetry for packaging.
    import sys

    subdirs = [
        x[0] for x in os.walk(os.getcwd()) if x[0].split("/")[-1] != "__pycache__"
    ]
    for dirs in subdirs:
        sys.path.append(dirs)


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
# maybe other checks are unnecesary
# config.set_main_option("sqlalchemy.url", os.environ["DATABASE_URL"])

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
append_path()
from app.db.base import Base  # noqa

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    if os.getenv("TEST", False):
        url = os.getenv("TEST_DATABASE_URI")
    else:
        url = os.getenv("DATABASE_URI")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    except Exception as exception:
        print(exception)
        # logging.error(exception)
        raise exception


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    if os.getenv("TEST", False):
        configuration["sqlalchemy.url"] = os.getenv("TEST_DATABASE_URI")
    else:
        configuration["sqlalchemy.url"] = os.getenv("DATABASE_URI")
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        try:
            with context.begin_transaction():
                context.run_migrations()
        except Exception as exception:
            print(exception)
            # logging.error(exception)
            raise exception
        finally:
            connection.close()

        # original one
        # with context.begin_transaction():
        #     context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
