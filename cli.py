import typer
from get_papers_list.fetch import search_pubmed, fetch_details
from get_papers_list.filter import extract_info
from get_papers_list.utils import save_to_csv

app = typer.Typer()

@app.command()
def main(query: str, file: str = None, debug: bool = False):
    if debug:
        typer.echo(f"Querying PubMed for: {query}")
    ids = search_pubmed(query)
    if debug:
        typer.echo(f"Found {len(ids)} articles")

    articles = fetch_details(ids)
    results = [extract_info(article) for article in articles]

    if file:
        save_to_csv(results, file)
        typer.echo(f"Results saved to {file}")
    else:
        for item in results:
            typer.echo(item)

if __name__ == "__main__":
    app()
