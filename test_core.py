import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from annotator import fetch_gene_info

def test_valid_gene():
    result = fetch_gene_info("TP53")
    assert result is not None
    assert result["symbol"] == "TP53"
    assert result["ensembl"] is not None

def test_invalid_gene():
    result = fetch_gene_info("THISISNOTGENE")
    assert result is None
