# walmart-sales-prediction

[Presentation (PowerPoint)](docs/presentation.pptx)

[Presentation (PDF)](docs/presentation.pdf)

Walmart

![Walmart](docs/walmart.jpg)

LSTM Example 1

![LSTM Example 1](docs/lstm-results-1.png)

LSTM Example 2

![LSTM Example 2](docs/lstm-results-2.png)

# Requirements

* conda (anaconda etc'...) - for manage the python envrioment

# Technologies

* poetry - for managing the python packages. Only python, pip and poetry are installed by conda.
* jupyter-lab - for runing jupyter notebooks in the browser

# Install

```bash
conda env create -f environment.yml
conda activate walmart-sales-prediction
poetry install --no-root
```

# Get Started

Opening the Jupter Lab:

```bash
conda activate walmart-sales-prediction
jupyter-lab
```

## CI (Formaters and Linters)

* note: the CI is not used because we dont have .py files in the project.

For running the Formaters for clean the code. Run in the terminal:

```bash
make fix
```

For running the Linters for check the code. Run in the terminal:

```bash
make lint
```

For running the Formaters and Linters for clean and check the code. Run in the terminal:

```bash
make fix-lint
```

List of the Formaters and Linters:

* black - for format the code
* isort - for sort and clean the imports
* flake8 - for check the code according to PEP8
* mypy - for static type checking


For removeing the cache. Run in the terminal:

```bash
make clean
```

In practice, you dont need to run this command, it called by the other make commands.

# License

MIT License

# Authors

* Lior Shiboli
* Omer Priel
