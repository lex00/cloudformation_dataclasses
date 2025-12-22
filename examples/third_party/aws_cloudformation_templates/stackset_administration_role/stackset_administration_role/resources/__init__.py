"""Resource definitions - auto-discovers all resources."""
import pkgutil
import importlib
from pathlib import Path

# Auto-discover and import all modules in this package
_pkg_path = Path(__file__).parent
for _finder, _name, _ispkg in pkgutil.iter_modules([str(_pkg_path)]):
    if not _name.startswith("_"):
        _module = importlib.import_module(f".{_name}", __package__)
        # Export all public names from each module
        for _attr in dir(_module):
            if not _attr.startswith("_"):
                globals()[_attr] = getattr(_module, _attr)
