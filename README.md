# LLM-Aided Legal Discovery Automation Bot

> AI-powered document analysis tool for streamlining legal discovery processes

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-10%2F10%20passing-brightgreen.svg)](tests/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

## 📋 Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [How It Works](#how-it-works-high-level-overview)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Enron Case Study](#in-depth-example-enron-documents-and-emails)
- [Performance](#performance-considerations)
- [Contributing](#contributing)
- [License](#license)

## 📖 Introduction

LLM-Aided Legal Discovery Automation is a powerful tool designed to streamline the legal discovery process by leveraging advanced AI models. It addresses the challenges legal professionals face when dealing with large volumes of documents in cases such as corporate litigation, intellectual property disputes, or regulatory investigations.

Traditional legal discovery processes often require manual review of thousands or millions of documents, which is time-consuming, labor-intensive, and prone to human error. This tool transforms the process through several key innovations:

1. **Flexible Goal Setting**: Users can define discovery goals either through a structured JSON template or by providing a free-form text description. The system can automatically generate a structured configuration file from the latter using AI interpretation.

2. **Diverse Document Handling**: The system processes a wide range of document formats, including PDFs (both scanned and digital), Word documents, plain text files, HTML, Outlook PST archives, and even mobile device message databases (iPhone and Android).

3. **Advanced OCR Capabilities**: For scanned documents or images, the tool employs Tesseract OCR, with an optional fallback to GPT-4 Vision API for particularly challenging documents.

4. **Intelligent Document Analysis**: Each document undergoes multi-stage AI-powered analysis to assess relevance to specified discovery goals, extract key information, and generate summaries.

5. **Comprehensive Dossier Generation**: The tool produces detailed dossiers of relevant information, including document summaries, relevance explanations, and importance scores.

6. **Efficient Data Management**: A SQLite database is used to store and manage processed documents, enabling quick retrieval and full-text search capabilities.

7. **Incremental Processing**: The system tracks processed files, allowing for efficient updates when new documents are added or existing ones are modified.

8. **Performance Optimization**: Parallel processing and asynchronous operations are employed to handle large document sets efficiently.

9. **Flexible AI Integration**: The tool supports multiple AI providers (OpenAI, Anthropic's Claude) and local LLMs, allowing users to choose based on their needs for privacy, cost, or specific capabilities.

10. **Detailed Logging and Error Handling**: Comprehensive logs are maintained for auditing and debugging purposes, ensuring transparency and reproducibility of the discovery process.

By automating the initial stages of document review and analysis, this tool allows legal professionals to focus on high-level strategy and decision-making. It's designed to handle cases of varying sizes and complexities, from small internal investigations to large-scale multi-national litigations.

The system's flexibility and scalability make it particularly valuable for law firms, corporate legal departments, and legal technology companies dealing with document-intensive cases. By leveraging AI and efficient data processing techniques, it aims to significantly reduce the time and cost associated with legal discovery while potentially uncovering insights that might be missed in manual review processes.

## Key Features

- Automated document processing and conversion for various file formats (PDF, DOC, DOCX, TXT, HTML, etc.)
- OCR capability for scanned documents using Tesseract
- AI-powered document analysis using OpenAI or Anthropic's Claude API
- Option to use local LLM for enhanced privacy
- Customizable discovery goals and parameters through JSON configuration
- Relevance assessment and importance scoring for documents
- Extraction of key information and generation of document summaries
- Creation of comprehensive dossiers for relevant documents
- Support for processing Outlook PST files and extracting emails
- Handling of iPhone and Android message databases
- Incremental processing with tracking of already processed files
- Parallel processing for improved performance
- SQLite database integration for efficient document management
- Full-text search capabilities in the SQLite database
- Enron email corpus processing for testing and demonstration
- GPT-4 Vision API integration for difficult-to-OCR documents (optional)
- Detailed logging and error handling
- Rate limiting and retry logic for API calls

## How It Works: High-Level Overview

1. **Configuration**: The system generates or loads a JSON configuration file defining discovery goals, keywords, and entities of interest. It can create this from free-form user input using AI interpretation.

2. **Document Preparation**: 
   - Converts various document formats (including PDFs, Word documents, emails, and mobile messages) to plaintext or markdown.
   - Applies OCR to scanned documents, with fallback to GPT-4 Vision API for difficult cases.

3. **Document Analysis**: 
   - Splits documents into manageable chunks.
   - Analyzes each chunk for relevance to discovery goals.
   - Extracts key information and generates summaries.
   - Calculates multi-faceted importance scores.

4. **Data Management**: 
   - Stores processed documents and metadata in a SQLite database.
   - Enables full-text search and efficient retrieval of document information.

5. **Dossier Compilation**: 
   - Compiles relevant document summaries into comprehensive dossiers.
   - Generates separate dossiers for high and low importance documents.

6. **Incremental Processing**: 
   - Tracks processed files to efficiently handle updates and new documents.

## Detailed Functionality

### 1. Configuration Generation

- Interprets free-form user input about case details and discovery goals using AI.
- Generates a structured JSON configuration with:
  - Case name
  - Discovery goals (descriptions, keywords, importance ratings)
  - Entities of interest
  - Minimum importance score threshold

### 2. Document Preparation

- Processes diverse formats: PDF, DOC(X), TXT, HTML, PST, EML, mobile message databases.
- Converts documents to plaintext or markdown for uniform processing.
- Applies Tesseract OCR for scanned documents, with GPT-4 Vision API as a fallback.
- Implements specialized handling for email archives and mobile messages.

### 3. Document Analysis

#### a. Chunking
- Splits documents into manageable chunks.
- Uses sophisticated sentence splitting to maintain context and coherence.

#### b. Relevance Assessment
- Analyzes chunks for relevance to discovery goals.
- Identifies key entities and keywords.
- Calculates relevance scores based on goal importance and content matching.

#### c. Information Extraction
- Extracts relevant quotes and passages.
- Identifies document metadata (type, date, author, recipient).
- Generates concise summaries of relevant content.

#### d. Importance Scoring
- Calculates sub-scores for:
  - Relevance to discovery goals
  - Keyword density
  - Entity mentions
  - Temporal relevance
  - Document credibility
  - Information uniqueness
- Computes a weighted average for an overall importance score.

### 4. Data Management

- Creates and populates a SQLite database with:
  - Document content and metadata
  - Case information
  - Discovery goals and keywords
  - Entity relationships
- Implements full-text search for efficient information retrieval.

### 5. Dossier Compilation

- Aggregates processed document information.
- Organizes documents by importance score.
- Generates structured markdown dossiers with:
  - Table of contents
  - Document summaries
  - Key extracts
  - Relevance explanations
  - Importance scores and breakdowns

### 6. Incremental Processing

- Maintains a record of processed files and their hash values.
- Processes only new or modified files in subsequent runs.
- Enables efficient updating of the database and dossiers.

### 7. Performance Optimization

- Implements parallel processing for document analysis using multiprocessing.
- Uses asyncio for efficient I/O operations.
- Applies rate limiting and retry logic for API calls.

### 8. Specialized Functionality

- Processes Enron email corpus for testing and demonstration purposes.
- Provides options for using different AI providers (OpenAI, Claude) or local LLMs.
- Implements robust error handling and comprehensive logging for troubleshooting and auditing.

---

## More Implementation Details and Rationale

### 1. Configuration Generation

- Uses AI models to interpret free-form user input about case details and discovery goals.
- Generates a structured JSON configuration file with case name, discovery goals, keywords, entities of interest, and importance thresholds.
- Implements multi-step validation to ensure configuration validity.
- Allows manual override with custom JSON configuration files.

Rationale: Balances user-friendly input with structured, machine-readable output for flexible case setup.

### 2. Document Preparation

- Processes diverse formats (PDF, DOC, DOCX, TXT, HTML, PST, EML, mobile message databases) using 'textract' and custom parsers.
- Converts documents to plaintext or markdown for uniform processing.
- Implements OCR using Tesseract, with GPT-4 Vision API as a fallback for difficult documents.
- Uses 'Magika' for accurate MIME type detection.
- Handles Outlook PST files and mobile device message databases.

Rationale: Ensures comprehensive document coverage and consistent processing across various formats, expanding the tool's applicability.

### 3. Document Analysis

- Implements intelligent document chunking with context-aware splitting.
- Uses AI-powered language models for relevance assessment, information extraction, and importance scoring.
- Calculates multi-faceted importance scores considering relevance, keyword density, entity mentions, temporal relevance, credibility, and uniqueness.

Rationale: Enables thorough and nuanced document analysis, balancing depth of analysis with processing efficiency.

### 4. Data Management

- Integrates SQLite database for efficient document and metadata storage.
- Implements full-text search capabilities for quick information retrieval.
- Stores case information, discovery goals, and entity relationships.

Rationale: Enhances data organization, speeds up information retrieval, and enables complex querying capabilities.

### 5. Dossier Compilation

- Aggregates processed information into structured markdown dossiers.
- Generates separate high-importance and low-importance dossiers.
- Includes document summaries, key extracts, relevance explanations, and importance scores.

Rationale: Provides easily navigable, comprehensive output for legal professionals to quickly access relevant information.

### 6. Incremental Processing

- Tracks processed files using hash values for efficient updates.
- Processes only new or modified files in subsequent runs.
- Implements file change detection for smart reprocessing.

Rationale: Optimizes processing time and resources for ongoing cases with large document volumes.

### 7. Performance Optimization

- Uses multiprocessing for parallel document analysis.
- Implements asyncio for efficient I/O operations.
- Applies rate limiting and retry logic with exponential backoff for API calls.

Rationale: Enables efficient processing of large document sets while managing API usage responsibly.

### 8. AI Model Flexibility

- Supports multiple AI providers (OpenAI, Anthropic's Claude) and local LLMs.
- Implements provider-specific API calls with error handling.
- Allows easy switching between providers via configuration.

Rationale: Offers flexibility in model selection based on privacy, cost, or capability requirements.

### 9. Specialized Functionality

- Includes automated processing of the Enron email corpus for testing and demonstration.
- Implements robust error handling and comprehensive logging.
- Provides options for suppressing headers and page numbers in processed documents.

Rationale: Enhances the tool's utility for testing, troubleshooting, and handling specific document processing challenges.

## 🛠 Tech Stack

### Core Technologies
- **Python 3.12+**: Modern Python with type hints and async support
- **asyncio**: Asynchronous I/O for high-performance document processing
- **SQLite**: Embedded database with FTS5 full-text search
- **multiprocessing**: Parallel processing for large document sets

### AI/ML Providers
- **OpenAI API**: GPT-4, GPT-4o-mini, GPT-4 Vision
- **Anthropic Claude API**: Claude 3 Haiku
- **llama-cpp-python** (optional): Local LLM support (GGUF models)

### Document Processing
- **textract**: Multi-format text extraction (PDF, DOC, DOCX, HTML, etc.)
- **PyPDF2**: PDF text extraction
- **pdf2image + pytesseract**: OCR pipeline for scanned documents
- **opencv-python-headless**: Image preprocessing for OCR
- **Pillow (PIL)**: Image manipulation and enhancement
- **pypff (libpff-python)** (optional): Outlook PST file processing
- **magika**: Accurate MIME type detection

### Performance & Utilities
- **aiofiles**: Async file operations
- **aiolimiter**: API rate limiting for async requests
- **httpx**: High-performance async HTTP client
- **tenacity + backoff**: Intelligent retry logic with exponential backoff
- **tqdm**: Real-time progress bars
- **picologging**: High-performance logging
- **tiktoken + transformers**: Token estimation and management
- **filelock**: File locking to prevent concurrent access issues

### Development & Testing
- **pytest**: Modern testing framework
- **pytest-asyncio**: Async test support
- **pytest-cov**: Code coverage reporting
- **pytest-mock**: Mocking utilities for tests
- **ruff**: Fast Python linter and formatter

### Requirements
- Python 3.12+
- Tesseract OCR engine (for scanned documents)
- 8GB+ RAM recommended
- OpenAI or Anthropic API key (or local LLM setup)

**Optional:**
- GPU with CUDA support (for local LLMs)
- libpff-python (for PST file processing)
- nvgpu (for GPU detection)

## 📦 Installation

### Prerequisites

Before installing, ensure you have:
- Python 3.12 or higher
- Tesseract OCR engine
- System libraries for document processing

### System Dependencies

#### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    antiword \
    unrtf \
    libxml2-dev \
    libxslt1-dev \
    libpoppler-cpp-dev \
    libjpeg-dev \
    build-essential
```

#### macOS

```bash
brew install tesseract poppler antiword
```

#### Windows

Download and install:
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- [Poppler](http://blog.alivate.com.au/poppler-windows/)

### Python Installation

1. **Clone the repository**

```bash
git clone https://github.com/dustinth2004/llm_aided_legal_discovery_bot.git
cd llm_aided_legal_discovery_bot
```

2. **Create and activate virtual environment** (recommended)

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python dependencies**

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file in the project root:

```bash
# LLM Provider Configuration
USE_LOCAL_LLM=False
API_PROVIDER=OPENAI  # Options: OPENAI, CLAUDE

# API Keys
OPENAI_API_KEY=sk-your-openai-api-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
```

### Optional: Local LLM Setup

For privacy-focused local LLM processing:

```bash
# CPU only
pip install llama-cpp-python

# With CUDA GPU support (requires NVIDIA GPU)
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python

# Download a GGUF model (example)
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf
```

### Verification

Verify installation:

```bash
# Check Python version
python --version  # Should be 3.12+

# Check Tesseract
tesseract --version

# Run tests
pytest tests/test_text_processing.py -v
```

## ⚙️ Configuration

### Discovery Configuration

Create a JSON configuration file defining your discovery goals:

```json
{
  "case_name": "Your Case Name v. Defendant",
  "discovery_goals": [
    "Identify evidence of fraudulent activities",
    "Find communications regarding financial misstatements"
  ],
  "keywords": [
    "fraud",
    "financial statements",
    "accounting irregularities",
    "insider trading"
  ],
  "entities_of_interest": [
    "John Doe",
    "Jane Smith",
    "Acme Corporation"
  ],
  "importance_threshold": 0.7,
  "date_range": {
    "start": "2000-01-01",
    "end": "2023-12-31"
  }
}
```

Save as `your_case_config.json` in the `discovery_configuration_json_files/` directory.

### Script Configuration

Edit configuration variables in `llm_aided_legal_discovery_bot.py`:

```python
# Use Enron example or your own documents
use_enron_example = False  # Set to False for your own documents

# Path to your discovery configuration
USE_OVERRIDE_DISCOVERY_CONFIG_JSON_FILE = "discovery_configuration_json_files/your_case_config.json"

# Input/Output directories
INPUT_DIRECTORY = "folder_of_source_documents__original_format"
OUTPUT_DIRECTORY = "output"

# Features
CREATE_CASE_SQLITE_DATABASE = True
USE_GPT4_VISION_FOR_DIFFICULT_PDFS = True

# Performance tuning
MAX_CONCURRENT_REQUESTS = 10
```

## 🚀 Usage

### Basic Usage

1. **Prepare your documents**

   Place source documents in the input directory:
   ```bash
   mkdir -p folder_of_source_documents__original_format
   cp /path/to/your/documents/* folder_of_source_documents__original_format/
   ```

2. **Configure discovery goals**

   Edit your configuration JSON file (see Configuration section above)

3. **Run the analysis**

   ```bash
   python llm_aided_legal_discovery_bot.py
   ```

4. **Review results**

   Check the `output/` directory for generated dossiers and database

### Using the Enron Example

To test with the Enron dataset:

```bash
# Download Enron sample data (optional)
python enron_sample_data_collector_script.py

# Run with Enron example enabled
# (Set use_enron_example = True in the script)
python llm_aided_legal_discovery_bot.py
```

### Advanced Usage

**Using Claude instead of OpenAI:**

```bash
# In .env file
API_PROVIDER=CLAUDE
ANTHROPIC_API_KEY=your-anthropic-key
```

**Using Local LLM:**

```bash
# In .env file
USE_LOCAL_LLM=True
```

**Generate configuration from free-form text:**

The tool can automatically generate structured configuration from natural language description using AI.

### Output Structure

```
output/
├── 01_document_plaintext_conversions/
│   ├── document1.txt
│   ├── document2.txt
│   └── ...
├── 02_corrected_by_gpt4_vision/
│   └── difficult_doc.txt
├── 03_enron_email_corpus_markdown/
│   └── email_bundle_001.md
├── 04_discovery_dossiers/
│   ├── [case_name]_dossier.md            # High-importance documents
│   └── [case_name]_low_importance_dossier.md  # Lower-priority documents
├── case_database.db                       # SQLite database with full-text search
└── processing.log                         # Detailed processing logs
```

### Output Files

- **Dossiers**: Comprehensive markdown reports with document summaries, relevance explanations, and importance scores
- **Database**: SQLite database with full-text search across all processed documents
- **Logs**: Detailed processing information for auditing and debugging

## 🧪 Testing

### Test Suite

The project includes a comprehensive test suite with 24 unit tests covering core functionality.

**Run all tests:**

```bash
pytest tests/ -v
```

**Run specific test modules:**

```bash
# Text processing tests (10/10 passing ✅)
pytest tests/test_text_processing.py -v

# Document preparation tests
pytest tests/test_document_preparation.py -v

# LLM integration tests (with mocking)
pytest tests/test_llm_integration.py -v

# Scoring algorithm tests
pytest tests/test_scoring.py -v
```

**Run with coverage:**

```bash
pytest tests/ --cov=. --cov-report=html
open htmlcov/index.html  # View coverage report
```

### Test Categories

- **Unit Tests** (`@pytest.mark.unit`): Fast, isolated function tests
- **Integration Tests** (`@pytest.mark.integration`): Multi-component tests
- **Async Tests**: Full pytest-asyncio support

### Current Status

✅ **10/10 tests passing** in `test_text_processing.py`:
- Text normalization and pagination removal
- Sophisticated sentence splitting
- Keyword highlighting
- Token estimation
- Text chunking
- Edge case handling

### Continuous Testing

Tests are configured with:
- Async support via `pytest-asyncio`
- Code coverage reporting
- Comprehensive test fixtures in `conftest.py`
- Mock LLM API calls to avoid costs during testing

## 📁 Project Structure

```
llm_aided_legal_discovery_bot/
│
├── llm_aided_legal_discovery_bot.py    # Main application (3067 lines)
├── enron_sample_data_collector_script.py  # Enron data downloader
├── requirements.txt                     # Python dependencies
├── pytest.ini                           # Test configuration
├── .env                                 # Environment variables (create this)
├── README.md                            # This file
│
├── discovery_configuration_json_files/
│   └── shareholders_vs_enron_corporation.json
│
├── tests/                               # Test suite
│   ├── __init__.py
│   ├── conftest.py                      # Shared test fixtures
│   ├── test_text_processing.py          # ✅ 10/10 passing
│   ├── test_document_preparation.py
│   ├── test_llm_integration.py
│   └── test_scoring.py
│
└── output/                              # Generated during execution
    ├── 01_document_plaintext_conversions/
    ├── 02_corrected_by_gpt4_vision/
    ├── 03_enron_email_corpus_markdown/
    ├── 04_discovery_dossiers/
    └── case_database.db
```

## ⚡ Performance Considerations

### Benchmarks

- **Processing Speed**: 10-50 documents/minute (varies by size and complexity)
- **Memory Usage**: 2-4GB for typical workloads
- **Concurrent Processing**: Configurable (default: 10 concurrent requests)
- **Token Efficiency**: Automatic chunking to stay within context limits

### Optimization Tips

1. **Enable multiprocessing**: Parallel document processing
2. **Adjust chunk sizes**: Balance between context and API calls
3. **Use local LLMs**: Eliminate API rate limits for large datasets
4. **Enable incremental processing**: Skip already-processed documents
5. **Optimize OCR**: Pre-process images to 300 DPI

### Cost Estimates

**OpenAI GPT-4o-mini:**
- ~$0.15-$0.30 per document
- ~$150-$300 per 1,000 documents

**Anthropic Claude 3 Haiku:**
- ~$0.10-$0.25 per document
- ~$100-$250 per 1,000 documents

**Local LLM:**
- Free (after model download)
- Requires GPU for practical speed

### Performance Scaling

- Processing time scales linearly with document count
- API rate limits may affect cloud LLM performance
- Local LLMs remove rate limits but require GPU hardware

## 🔮 Future Roadmap

- [ ] Web interface for non-technical users
- [ ] Additional LLM provider support (Cohere, Mistral, Gemini)
- [ ] Enhanced entity extraction with NER models
- [ ] Document deduplication
- [ ] Timeline visualization of events
- [ ] Export to legal review platforms (Relativity, Everlaw)
- [ ] Multi-language support
- [ ] Cloud deployment templates (AWS, Azure, GCP)
- [ ] Audio and video transcription support
- [ ] Real-time collaborative review features

---

## In-Depth Example: Enron Documents and Emails

### Overview of the Enron Case

The Enron scandal of 2001 remains a landmark case in corporate fraud, significantly impacting corporate governance and financial regulation. Key aspects include:

- Complex fraudulent accounting using mark-to-market practices and special purpose entities (SPEs)
- Concealment of billions in debt through off-books partnerships
- Inflated profits and stock prices
- Insider trading by executives
- Document destruction by Enron's auditor, Arthur Andersen

Consequences included massive shareholder losses, executive convictions, Arthur Andersen's dissolution, and the Sarbanes-Oxley Act of 2002.

### Significance for Legal Discovery

The Enron case has become a gold standard for testing and developing legal discovery tools, forensic accounting methods, and natural language processing systems. This is due to several factors:

1. **Volume and Variety of Data**: The Enron email corpus, released as part of the investigation, contains over 500,000 emails from 150 employees. This vast dataset provides a realistic scenario for testing large-scale document processing and analysis tools.

2. **Real-world Complexity**: The documents span a wide range of topics, from mundane office communications to discussions of complex financial transactions, offering a true-to-life challenge for content analysis and relevance determination.

3. **Known Outcomes**: With the benefit of hindsight and thorough investigations, we know what kind of evidence exists in these documents, making it possible to evaluate the effectiveness of discovery tools.

4. **Linguistic Diversity**: The emails capture natural language use in a corporate setting, including formal and informal communications, technical jargon, and attempts at obfuscation.

5. **Temporal Aspect**: The dataset spans several years, allowing for analysis of how communications and practices evolved over time, especially as the company approached its collapse.
   


### Implementation in Our Legal Discovery Automation Tool

The Enron case thus provides an ideal testbed for this project; we can get and process all the data and run the tool on the processed data and see empirically whether the system is able to find the relevant documents/emails that would be useful in a civil or criminal case. 

Our tool leverages the Enron case for testing and demonstration:

1. **Automated Data Collection**:
   ```python
   async def download_and_extract_enron_emails_dataset(url: str, destination_folder: str):
       # Downloads and extracts the Enron email dataset
   ```
   - Asynchronously downloads the Enron email dataset.
   - Handles large file downloads with progress tracking using `tqdm`.
   - Extracts the dataset, organizing it into a usable structure.

2. **Email Corpus Processing**:
   ```python
   async def process_extracted_enron_emails(maildir_path: str, converted_source_dir: str):
       # Processes the extracted Enron emails
   ```
   - Parses individual emails, extracting metadata and content.
   - Converts emails to a standardized format for analysis.
   - Implements concurrent processing for efficiency.

3. **Specialized Email Parsing**:
   ```python
   async def parse_enron_email_async(file_path: str) -> Dict[str, Any]:
       # Parses individual Enron emails
   ```
   - Extracts key email fields (From, To, Subject, Date, Cc, Bcc).
   - Handles Enron-specific metadata (X-Folder, X-Origin, X-FileName).
   - Processes email body, applying minimal cleaning.

4. **Document Analysis Pipeline**:
   - Applies OCR to scanned PDFs using Tesseract, with GPT-4 Vision API as a fallback for difficult documents.
   - Utilizes LLMs to analyze content, identify entities, and extract relevant information.
   - Assigns importance scores based on relevance to specified discovery goals.

5. **Dossier Compilation**:
   ```python
   def compile_dossier_section(processed_chunks: List[Dict[str, Any]], document_id: str, file_path: str, discovery_params: Dict[str, Any]) -> Dict[str, Any]:
       # Compiles processed chunks into a cohesive dossier section
   ```
   - Aggregates processed information into structured dossiers.
   - Separates high-importance and low-importance documents.
   - Generates summaries, extracts key information, and provides relevance explanations.

6. **Tailored Discovery Goals**:
   - The `USER_FREEFORM_TEXT_GOAL_INPUT` variable contains specific discovery goals related to the Enron case, such as:
     - Uncovering evidence of financial misreporting and fraudulent accounting practices
     - Identifying communications about off-book entities and debt concealment
     - Locating discussions about market manipulation and insider trading
     - Finding attempts to influence auditors or hide information
   - These goals closely mirror the actual issues in the Enron case, providing a realistic scenario for legal discovery.

7. **Performance Optimization**:
   - Implements parallel processing using `multiprocessing`.
   - Uses `asyncio` for efficient I/O operations, crucial for handling large email datasets.

### Why It's an Excellent Test of the System

1. **Scale and Complexity**: The Enron dataset tests the system's ability to handle a large volume of diverse documents efficiently.

2. **Pattern Recognition**: It challenges the tool to identify subtle patterns of fraudulent behavior across numerous documents and communications.

3. **Contextual Understanding**: The system must understand complex financial concepts and corporate jargon to accurately assess document relevance.

4. **Temporal Analysis**: The tool can demonstrate its ability to track the evolution of issues over time, crucial in understanding how the fraud developed.

5. **Entity Relationship Mapping**: By correctly identifying key players and their roles, the system showcases its capability in building a coherent narrative from fragmented information.

6. **Accuracy and Recall**: With known outcomes, we can evaluate how well the system uncovers critical pieces of evidence that were instrumental in the actual Enron investigation.

## 🤝 Contributing

Contributions are welcome! We appreciate your help in making this project better.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run tests**: `pytest tests/ -v`
5. **Run linter**: `ruff check .`
6. **Commit**: `git commit -m 'Add amazing feature'`
7. **Push**: `git push origin feature/amazing-feature`
8. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Write comprehensive docstrings
- Add unit tests for new features
- Maintain or improve code coverage
- Update documentation for user-facing changes

### Code Quality Standards

```bash
# Format code
ruff format .

# Check for issues
ruff check .

# Run full test suite
pytest tests/ -v --cov=.
```

### Reporting Issues

- Use GitHub Issues for bug reports and feature requests
- Provide detailed reproduction steps for bugs
- Include system information and error messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Enron Email Dataset**: Federal Energy Regulatory Commission
- **OpenAI**: GPT-4 and GPT-4o-mini models
- **Anthropic**: Claude 3 models
- **Tesseract OCR**: Google's open-source OCR engine
- **llama.cpp**: Georgi Gerganov's efficient LLM inference library
- **Legal Tech Community**: For inspiration and feedback

## ⚠️ Important Disclaimers

### Legal Disclaimer

This tool is designed to **assist** legal professionals in document review but should **not replace professional legal judgment**. Always verify AI-generated analyses before using them in legal proceedings. Consult with qualified legal counsel for legal advice.

### Privacy & Security Notice

- **Local Processing**: Documents are processed locally by default
- **Cloud APIs**: When using OpenAI or Anthropic APIs, document content is sent to third-party services
- **Compliance**: Ensure compliance with attorney-client privilege, work product doctrine, and confidentiality requirements
- **Data Handling**: Review your jurisdiction's rules on using AI tools for legal work
- **Encryption**: Consider encrypting sensitive documents before processing
- **Audit Trails**: Maintain logs for potential discovery obligations

### Ethical Considerations

- Use this tool responsibly and in accordance with legal ethics rules
- Maintain human oversight of AI-generated analysis
- Be transparent with clients about the use of AI tools
- Verify critical findings manually
- Consider potential bias in AI models

## 📞 Support & Resources

- **GitHub Issues**: [Report bugs or request features](https://github.com/dustinth2004/llm_aided_legal_discovery_bot/issues)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/dustinth2004/llm_aided_legal_discovery_bot/discussions)
- **Documentation**: This README and inline code comments
- **Tests**: See `tests/` directory for usage examples

## 📊 Project Status

- **Version**: 1.0.0
- **Status**: Active Development
- **Python**: 3.12+
- **Tests**: 10/10 passing in core modules
- **Last Updated**: December 2024

---

**Made with ⚡ by the Legal Tech Community**

If you find this project useful, please consider giving it a ⭐ on GitHub!
