from rich.console import Console
from pages import PyWiki



if __name__ == "__main__":
    console = Console()
    
    console.print(PyWiki.display())
