"""
    - created at feb 5/20/2021 by mjghasempour
    - Email: topcodermc@gmail.com
    - this package is core of IOC for config handlers and other critical configs
"""

from dependency_injector.containers import (
    DeclarativeContainer as DI_DeclarativeContainer
)
from dependency_injector.providers import (
    Singleton as DI_provider_singleton
)


class Core(DI_DeclarativeContainer):
    """ IoC container of core component providers.
            here we initialize the configs and other core options like logger or ...
    """
    pass
