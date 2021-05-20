"""
    created at Jan 18/2021 by amirr
    - this package is Services initializer of IoC
"""

from . import (
    DI_DeclarativeContainer, DI_Callable,
)

from .services import Services
from .core import Core


class Application(DI_DeclarativeContainer):
    """ IoC container of application component providers. """
    
    def __init__(self):
        super(Application, self).__init__()

    def __run_app__(self):
        pass

    main: DI_Callable = DI_Callable(
        __run_app__, self=None
    )

