# solar-challenge-week1
10 academy first challenge

mkdir -p .vscode src notebooks tests scripts

# Optional: VS Code settings
mkdir .vscode
echo '{}' > .vscode/settings.json

# Add README files
echo "# Notebooks Folder" > notebooks/README.md
echo "# Scripts Folder" > scripts/README.md

# Touch __init__.py in all Python folders
touch notebooks/__init__.py
touch tests/__init__.py
touch scripts/__init__.py

# Main README
cat > README.md <<EOL
# Solar Challenge Week 1

## Development Setup

1. Clone the repo
2. Create a virtual environment:

\`\`\`bash
python -m venv venv
source venv/bin/activate
\`\`\`

3. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Folder Structure

\`\`\`
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
\`\`\`
EOL

git add README.md notebooks/ scripts/ tests/ src/ .vscode/
git commit -m "docs: add README and folder structure"

