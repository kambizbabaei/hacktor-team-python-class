"""
    - created at feb 5/20/2021 by mjghasempour
    - Email: topcodermc@gmail.com
    -  this package is Gateways of IoC
"""

from dependency_injector.containers import (
    DeclarativeContainer as DI_DeclarativeContainer
)


class GateWays(DI_DeclarativeContainer):
    """ IoC container of gateway (API Client to remote services) providers
            here we set database objects and other 3d party services like amazon (AWS) or ...
    """
    pass
