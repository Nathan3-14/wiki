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
    "PYWiki is a wiki-ish program where pages can be added through a custom class.",
    {"Creator": "Nathan3-14", "Pages": "1"}
)
TestPage = Page(
    "Test Page",
    "This is a test page to see how weighted titles are",
    {}
)

page_list = [PyWiki, TestPage]
pages = {wikipage.title.lower(): wikipage for wikipage in page_list}
