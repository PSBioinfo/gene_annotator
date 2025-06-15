# Gene_Annotator
Command-line tool for retrieving and logging human gene annotations from MyGene.info. Supports single gene queries or batch queries from a file.

## Features
- Query a single gene ('--gene') or a list of genes ('--file')
- Uses [MyGene.info](https://mygene.info) live API
- Prints results to console
- Logs annotated results to 'annotation_logs.txt'
- Handles missing data and alternate formats
- Fully unit-tested with 'pytest'

## Installation

```bash
#Clone the repo
git clone https://github.com/PSBioinfo/gene_annotator.git
cd gene_annotator

#Create a virtual environment
python3 -m venv venv
source venv/bin/activate

#Install dependencies
pip install -r requirements.txt
```

## Dependencies
```
requests
pytest #for testing
```

## Usage

### Query a single gene
```bash
python main.py --gene TP53
```

### Query a list of genes from a file
```bash
python main.py --file genes.txt
```
#### Example ```genes.txt```:

TP53
BRCA1
EGFR
AIF1

#### Sample output:

Looking up: TP53
Name: tumor protein p53
Entrez: 7157
Ensembl: ENSG00000141510

📝 Results saved to: annotation_log.txt

### Running Tests

```bash
pytest tests/
```

## Project Structure
gene_annotator/
├── main.py               # CLI tool
├── annotator.py          # Core logic (API query)
├── tests/
│   └── test_core.py      # Unit tests for annotation function
├── annotation_log.txt    # Output log (auto-generated)
├── requirements.txt      # Dependencies
└── README.md 

## License
MIT License
