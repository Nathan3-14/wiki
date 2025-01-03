from typing import Any, Dict
from rich.console import Console
from pages import pages


def get_key(_dict: Dict[Any, Any], _value: Any) -> Any:
    for key, value in _dict.items():
        if value == _value:
            return key
    print(f"no match :( of {_value} in {_dict}")


if __name__ == "__main__":
    console = Console()
    console.print("Search: ", end="")
    search_term = input()
    console.print("")
    
    results = {}
    if search_term.lower() in list(pages.keys()):
        console.print(pages[search_term].display())
    else:
        for wikipage_title, wikipage in pages.items():
            if search_term in wikipage_title or search_term in wikipage.content:
                results[wikipage_title] = wikipage_title.count(search_term) * 3 + wikipage.content.lower().count(search_term)
        results = {get_key(results, value): value for value in sorted(list(results.values()), reverse=True)}
        console.print(results)
        console.print("Potential matches:")
        for index, title in enumerate(results.keys()):
            console.print(f"{index}: {title}")