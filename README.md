# Fall 2025 (Monorepo)

Centralized repository for all Fall 2025 courses.

## Quickstart (Python for ECON 695)
```
conda env create -f environment.yml
conda activate fall2025
python -m ipykernel install --user --name fall2025 --display-name "Python (Fall 2025)"
pre-commit install
jupyter lab
```
