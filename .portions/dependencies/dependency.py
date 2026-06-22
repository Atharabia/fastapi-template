from typing import Annotated

from fastapi import Depends


def get_DEPENDENCY_FUNCTION_NAME():
    pass


DEPENDENCY_TYPE_NAMEDep = Annotated[None, Depends(get_DEPENDENCY_FUNCTION_NAME)]
