from typing import Any, Dict
from rich.console import Console
from rich.table import Table
from rich import box


class Page:
    def __init__(self, title: str, content: str, info: Dict[str, Any]) -> None:
        self.title = title
        self.content = content
        self.info = info
    
    def display(self) -> Table:
        page_table = Table(expand=True)
        info_table = Table.grid(expand=True)
        info_table.add_column()
        info_table.add_column()
        for key, value in self.info.items():
            info_table.add_row(key, value)
        
        page_table.add_column(self.title)
        page_table.add_column()
        page_table.add_row(self.content, info_table)
        
        
        return page_table
    """
    create table:
    TITLE
    --------
    body text | Info Title
    body text | Info: Value
    """

if __name__ == "__main__":
    console = Console()
    
    test_page = Page(
        "Test Page",
        "Hi there!\nThis is a cool test page\n:)",
        {"pages": "1", "a": ":smile:"}
    )
    console.print(test_page.display())
