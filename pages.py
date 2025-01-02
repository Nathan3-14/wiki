from rich.table import Table
from typing import Dict, Any

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



PyWiki = Page(
    "PyWiki",
    "",
    {"Creator": "Nathan3-14", "Pages": "1"}
)
