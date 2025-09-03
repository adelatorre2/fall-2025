

# Contributing Guidelines

Thank you for your interest in contributing! Please follow the instructions below based on your role.

## For Classmates (Contributors)

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

Follow these steps to review and merge contributions:

1. **Fetch Latest Changes**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Review Pull Requests**
   - Check the "Pull Requests" tab on GitHub.
   - Review code, request changes if needed, and discuss with contributor.

3. **Test Contributions Locally**
   ```bash
   git fetch origin pull/PR_NUMBER/head:pr-branch
   git checkout pr-branch
   # Run tests or review as needed
   ```

4. **Merge Approved Pull Requests**
   - Use GitHub's interface to merge after approval.

5. **Clean Up Local Branches**
   ```bash
   git branch -d pr-branch
   ```

6. **Pull Latest Main**
   ```bash
   git checkout main
   git pull origin main
   ```