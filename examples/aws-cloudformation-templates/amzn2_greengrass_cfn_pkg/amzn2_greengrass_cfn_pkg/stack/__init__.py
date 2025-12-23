"""Stack - parameters, outputs, and resources."""
from .params import *  # noqa: F403, F401

# Import resources with topological ordering
from cloudformation_dataclasses.core.resource_loader import setup_resources
setup_resources(__file__, __name__, globals())

# Import outputs after resources (outputs reference resource classes)
try:
    from .outputs import *  # noqa: F403, F401
except ImportError:
    pass
