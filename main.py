from typing import Any, Dict
from rich.console import Console


class Page:
    def __init__(self, title: str, content: str, info: Dict[str, Any]) -> None:
        self.title = title
        self.content = content
        self.info = info
    
    def display(self) -> str:
        return f"{self.title}\n{self.content}"
    """
    create table:
    TITLE
    --------
    body text | Info Title
    body text | Info: Value
    """

if __name__ == "__main__":
    console = console
