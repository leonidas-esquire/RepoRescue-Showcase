# Installation

This guide provides step-by-step instructions for installing the necessary dependencies to run this project and its documentation site locally.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
- [Git](https://git-scm.com/downloads/)

## Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Automation-Marketing-Experts/RepoRescue-Showcase.git
   cd RepoRescue-Showcase
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   This will install all the necessary Python packages, including MkDocs and its plugins.

## Running the Documentation Site

Once the dependencies are installed, you can run the documentation site locally:

```bash
mkdocs serve
```

This will start a local development server, and you can view the documentation site by opening your browser to `http://127.0.0.1:8000`.

## Troubleshooting

If you encounter any issues during installation, please refer to the [Troubleshooting](troubleshooting/common-issues.md) section of this documentation.

