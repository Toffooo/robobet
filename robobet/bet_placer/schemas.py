import warnings
from dataclasses import dataclass
from typing import Any, Dict, Optional, Union


@dataclass
class RouterOperations:
    warnings.warn("This data structure will be deprecated. Don't use it")
    type: str
    keyword: str


@dataclass
class RouterLoop:
    exp: str
    value: Any


@dataclass
class RouterLinter:
    type: str
    tag: str
    attrs: Dict[str, str]
    children: Optional["RouterLinter"] = None
    index: Optional[int] = None


@dataclass
class RouterResponse:
    path: str
    linter: RouterLinter


def _process_children(linter, element: RouterLinter, counter=0):
    if linter is None:
        return element

    _obj = RouterLinter(
        type=linter["type"],
        tag=linter["tag"],
        attrs=linter["attrs"],
    )
    _val = element
    for _ in range(counter - 1):
        _val = getattr(element, "children")

    if _val is not None:
        _val.children = _obj

    if "children" not in linter:
        return element

    counter += 1

    return _process_children(linter["children"], _val, counter)


def create_router_response(
    path: str,
    linter: Dict[str, Union[str, Dict[str, str], int]],
) -> RouterResponse:

    rt = RouterLinter(
        type=linter["type"],
        tag=linter["tag"],
        attrs=linter["attrs"],
    )
    _linters = _process_children(linter.get("children"), rt)

    return RouterResponse(
        path=path,
        linter=_linters,
    )
