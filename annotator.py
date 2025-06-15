import requests

def fetch_gene_info(gene_symbol):
    url = f"https://mygene.info/v3/query?q={gene_symbol}&species=human&fields=ensembl,name,symbol,entrezgene"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"⚠️ API request failed for {gene_symbol}")
        return None

    data = response.json()
    hits = data.get("hits", [])
    if not hits:
        return None

    for hit in hits:
        ensembl_data = hit.get("ensembl")
        ensembl_id = None

        if isinstance(ensembl_data, dict):
            ensembl_id = ensembl_data.get("gene")
        elif isinstance(ensembl_data, list) and len(ensembl_data) > 0:
            ensembl_id = ensembl_data[0].get("gene")

        if ensembl_id:
            return {
                "symbol": hit.get("symbol"),
                "name": hit.get("name"),
                "entrez": hit.get("entrezgene"),
                "ensembl": ensembl_id
            }

    # fallback to top hit without Ensembl
    top_hit = hits[0]
    return {
        "symbol": top_hit.get("symbol"),
        "name": top_hit.get("name"),
        "entrez": top_hit.get("entrezgene"),
        "ensembl": None
    }

