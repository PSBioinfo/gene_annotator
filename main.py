import argparse
from annotator import fetch_gene_info
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Fetch gene annotation info from MyGene.info")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--gene", help="Single gene symbol (e.g., TP53)")
    group.add_argument("--file", help="Path to text file with gene symbols (one per line)")
    args = parser.parse_args()

    # Load input genes
    genes = []
    if args.gene:
        genes = [args.gene]
    elif args.file:
        if not os.path.exists(args.file):
            print(f"⚠️ File not found: {args.file}")
            return
        with open(args.file) as f:
            genes = [line.strip() for line in f if line.strip()]

    # Create or append to log file
    log_file = "annotation_log.txt"
    with open(log_file, "a") as log:
        log.write(f"\n--- Gene Annotation Log: {datetime.now()} ---\n")

        for gene in genes:
            print(f"\n🔍 Looking up: {gene}")
            result = fetch_gene_info(gene)

            if result:
                output = (
                    f"✅ Gene: {result['symbol']}\n"
                    f"   Name: {result['name']}\n"
                    f"   Entrez: {result['entrez']}\n"
                    f"   Ensembl: {result['ensembl']}\n"
                )
            else:
                output = f"⚠️ No data found for {gene}\n"

            print(output)               # print to console
            log.write(output + "\n")   # write to file

    print(f"\n📝 Results saved to: {log_file}")

if __name__ == "__main__":
    main()

