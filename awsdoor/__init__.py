import pkgutil
import importlib

# Load all commands in the package

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")