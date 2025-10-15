# Deployment Instructions for Repo Rescue™ Showcase

This document provides instructions for deploying the Repo Rescue™ Showcase repository to GitHub and GitHub Pages.

---

## Prerequisites

- A GitHub account
- Git installed on your local machine
- Python 3.8+ installed
- MkDocs and MkDocs Material installed (`pip install mkdocs mkdocs-material`)

---

## Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in to your account.
2. Click the "+" icon in the top right corner and select "New repository."
3. Name the repository `RepoRescue-Showcase` (or your preferred name).
4. Set the repository visibility to **Public** (required for GitHub Pages).
5. Do **not** initialize the repository with a README, .gitignore, or license (we already have these files).
6. Click "Create repository."

---

## Step 2: Initialize Git and Push to GitHub

Navigate to the showcase repository directory and run the following commands:

```bash
cd /path/to/RepoRescue-Showcase

# Initialize Git
git init

# Add all files
git add .

# Commit the files
git commit -m "Initial commit: Repo Rescue™ Showcase"

# Add the remote repository
git remote add origin https://github.com/YOUR-USERNAME/RepoRescue-Showcase.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

---

## Step 3: Deploy Documentation to GitHub Pages

### Option 1: Automatic Deployment (Recommended)

The repository includes a GitHub Actions workflow that automatically builds and deploys the documentation site when changes are pushed to the `main` branch.

1. Go to your repository on GitHub.
2. Click on "Settings" > "Pages."
3. Under "Source," select "Deploy from a branch."
4. Under "Branch," select `gh-pages` and `/ (root)`.
5. Click "Save."

The documentation site will be automatically deployed to `https://YOUR-USERNAME.github.io/RepoRescue-Showcase/`.

### Option 2: Manual Deployment

If you prefer to deploy manually, run the following command:

```bash
mkdocs gh-deploy --force
```

This will build the documentation and push it to the `gh-pages` branch.

---

## Step 4: Verify Deployment

1. Go to `https://YOUR-USERNAME.github.io/RepoRescue-Showcase/` in your browser.
2. Verify that the documentation site is displayed correctly.
3. Test the navigation and search functionality.

---

## Step 5: Configure Repository Settings (Optional)

### Enable Issues and Discussions

1. Go to your repository on GitHub.
2. Click on "Settings."
3. Scroll down to the "Features" section.
4. Ensure "Issues" is checked (to enable issue tracking).
5. Optionally, enable "Discussions" for community conversations.

### Add Repository Description

1. Go to your repository on GitHub.
2. Click on the "About" section (top right).
3. Add a description: "A showcase repository demonstrating The GitPolish Protocol™ in action."
4. Add topics: `documentation`, `gitpolish-protocol`, `repo-rescue`, `showcase`
5. Optionally, add a website URL: `https://YOUR-USERNAME.github.io/RepoRescue-Showcase/`

---

## Step 6: Test Automated Workflows

The repository includes three GitHub Actions workflows:

1. **Documentation Build:** Automatically builds and deploys the documentation site.
2. **Markdown Lint:** Checks all markdown files for consistency.
3. **Link Check:** Verifies that there are no broken links in the documentation.

To test these workflows:

1. Make a small change to a markdown file (e.g., add a sentence to `README.md`).
2. Commit and push the change.
3. Go to the "Actions" tab in your GitHub repository.
4. Verify that all workflows run successfully.

---

## Troubleshooting

### Documentation Site Not Deploying

- Ensure the repository is **public** (GitHub Pages requires public repositories for free accounts).
- Check the "Actions" tab for any errors in the workflow.
- Verify that the `gh-pages` branch exists and contains the built documentation.

### Workflows Not Running

- Ensure that GitHub Actions is enabled for your repository (Settings > Actions > General).
- Check the workflow files in `.github/workflows/` for any syntax errors.

---

## Maintenance

To keep the showcase repository up-to-date:

1. Regularly update dependencies in `requirements.txt`.
2. Update the documentation to reflect any changes to The GitPolish Protocol.
3. Add new examples or features as they are developed.
4. Monitor the GitHub Actions workflows to ensure they continue to run successfully.

---

*For questions or support, contact hello@reporescue.com*

