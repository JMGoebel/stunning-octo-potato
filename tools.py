import arxiv
import requests
import os

client = arxiv.Client()

def fetch_arxiv_papers(title: str, papers_count: int):
    search_query = f'ti:"{title}"'
    search = arxiv.Search(
        query=search_query, 
        max_results=papers_count,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
  
    papers = []
    results = client.results(search)

    for result in results:
        paper_info = {
            'title': result.title,
            'summary': result.summary,
            'published': result.published,
            'journal_ref': result.journal_ref,
            'doi': result.doi,
            'primary_category': result.primary_category,
            'categories': result.categories,
            'pdf_url': result.pdf_url,
            'arxiv_url': result.entry_id,
            'authors': [author.name for author in result.authors],
        }
        papers.append(paper_info)
    return papers

def download_pdf(pdf_url: str, output_file_name: str):
    try:
        os.makedirs('papers', exist_ok=True)
        full_output_file_name = os.path.join('papers', output_file_name)
        response = requests.get(pdf_url)
        response.raise_for_status()
        with open(full_output_file_name, 'wb') as file:
            file.write(response.content + '.pdf')
        return f"PDF downloaded to {full_output_file_name}"
    except requests.exceptions.RequestException as e:
        return f"Error downloading the PDF: {e}"
    

  