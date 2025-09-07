<!-- markdownlint-disable MD031 MD022 MD023 MD025 MD012 MD047 -->

# Contributing Guidelines

Thank you for your interest in contributing! Please follow the instructions below based on your role.

## For Classmates (Contributors)

**Expectations:**  
Contributors must fork the repository, open pull requests (PRs) for their changes, and expect review and approval before merging. Direct pushes to the `main` branch are not allowed.

Follow these steps to contribute changes:

1. **Fork the Repository**
   - Click the "Fork" button on GitHub to create your own copy of the repo.

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
   cd REPO-NAME
   ```

3. **Create a New Branch**
   ```bash
   git checkout -b your-feature-or-fix
   ```

4. **Make Your Changes**
   - Edit, add, or delete files as needed.

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Describe your changes"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin your-feature-or-fix
   ```

7. **Open a Pull Request**
   - Go to your fork on GitHub and click "Compare & pull request".
   - Fill out the PR template and submit.

## For Repo Owner (Alejandro)

**Expectations:**  
As the repo owner, you are responsible for maintaining code quality. You can push directly to the `main` branch but must be diligent to avoid introducing buggy commits.

**Daily Workflow for Alejandro:**
```bash
git checkout main
git pull origin main
# make edits
git add -A
git commit -m "Your message"
git push origin main
```

**Optional Feature Branch Workflow:** (for staging)
```bash
git checkout -b alejandro/feature-branch
# edits
git add -A
git commit -m "Work"
git checkout main
git pull origin main
git merge --no-ff alejandro/feature-branch
git push origin main
git branch -d alejandro/feature-branch
git push origin --delete alejandro/feature-branch
```

**Reviewing and Merging PRs from Contributors:**  
Continue to review pull requests submitted by contributors. Contributors must still go through the PR process for their changes to be merged.


# Quick Command Reference

## For Contributors
```bash
git checkout -b your-feature-or-fix
git add .
git commit -m "Describe your changes"`
git push origin your-feature-or-fix
# Then open a Pull Request on GitHub
```

## For Alejandro
```bash
git checkout main
git pull origin main
git add -A
git commit -m "Message"
git push origin main
```

_Optional: Feature branch workflow summary (recommended for larger changes):_
```bash
# create branch → edit → merge → delete branch
git checkout -b alejandro/feature-branch
# make edits
git add -A
git commit -m "Work"
git checkout main
git pull origin main
git merge --no-ff alejandro/feature-branch
git push origin main
git branch -d alejandro/feature-branch
git push origin --delete alejandro/feature-branch
```


### Environment Management Notes

Switching between Conda environments:

```bash
# list all environments
conda env list

# activate the ECON 695 environment
conda activate econ695

# deactivate current environment
conda deactivate

# switch back to the base environment
conda activate base
```

- **econ695** is the dedicated environment for this class (Python 3.13.5 + Jupyter + core packages).
- If you create other environments (e.g., fall2025), just `conda activate fall2025` when needed.
- In VS Code: select the right kernel/interpreter from the top-right of a notebook or via Command Palette.

<!-- markdownlint-enable MD031 MD022 MD023 MD025 MD012 MD047 -->