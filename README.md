
# Python Foundation for Spatial Analysis

A practical learning repository focused on building on my Python programming skills for geospatial data processing, spatial analysis, and workflow automation.

This repository documents my learning journey through the [Python Foundation for Spatial Analysis](https://spatialthoughts.com/courses/python-foundation-for-spatial-analysis/) course by **Spatial Thoughts**.

The goal is to strengthen my Python programming foundation and apply these skills to real-world geographic data analysis using commonly used geospatial libraries.

## Course Overview

The course introduces Python programming in a GIS context, progressing from fundamental programming concepts to processing vector and raster datasets and automating spatial workflows.

| Session | Focus | Topics |
|---------|-------|--------|
| 1 | Python Fundamentals | Variables, data types, strings, conditionals, loops, and functions |
| 2 | Data Processing | Geographic coordinates, third-party libraries, web APIs, and file handling |
| Assignment | Geocoding | Converting addresses into geographic coordinates using GeoPy |
| 3 | Tabular and Vector Data | Pandas, GeoPandas, and vector data analysis |
| 4 | Raster Data and Automation | NumPy, rioxarray, raster analysis, and workflow automation |
| Class Project | Applied Learning | Applying Python and geospatial concepts to a practical project |

**Official Course:** [Python Foundation for Spatial Analysis — Spatial Thoughts](https://spatialthoughts.com/courses/python-foundation-for-spatial-analysis/)

## Learning Objectives

By working through this course, I aim to:

- Develop a solid understanding of Python programming fundamentals.
- Write clean, reusable, and maintainable Python scripts.
- Work with geographic coordinates and spatial data structures.
- Read, process, clean, and transform datasets using Python.
- Understand how to interact with external libraries and web APIs.
- Perform vector-based spatial analysis using GeoPandas.
- Process and analyse raster datasets using NumPy and rioxarray.
- Automate repetitive geospatial processing tasks.
- Build reproducible Python workflows for geospatial applications.

## Development Environment

This project uses **uv** for Python environment and dependency management.

### Technologies

- Python 3.13.12
- uv — Python package and project manager
- Visual Studio Code
- Git and GitHub


## Python Libraries

The following libraries are introduced or explored throughout the learning process.

| Library | Purpose |
|---------|---------|
| [GeoPy](https://geopy.readthedocs.io/) | Geocoding, reverse geocoding, and geographical distance calculations |
| [Pandas](https://pandas.pydata.org/) | Tabular data processing, cleaning, and analysis |
| [GeoPandas](https://geopandas.org/) | Reading, manipulating, and analysing vector spatial datasets |
| [NumPy](https://numpy.org/) | Numerical operations and multidimensional arrays |
| [rioxarray](https://corteva.github.io/rioxarray/) | Working with georeferenced raster datasets |



## Exercises and Learning Progress

This repository contains practical exercises and notes developed throughout the course.

Topics include:

- Python variables, data types, and operators
- String manipulation and formatting
- Conditional statements and loops
- Functions and reusable code
- Geographic coordinate conversion
- Working with third-party Python packages
- Geocoding and geographic distance calculations
- Reading and writing data files
- Working with web APIs
- Tabular data analysis with Pandas
- Vector spatial analysis with GeoPandas
- Raster data processing with NumPy and rioxarray
- Automating geospatial workflows



## Dependency Management

Dependencies are managed using `uv`.

- `pyproject.toml` defines the project metadata and dependencies.
- `uv.lock` records resolved dependency versions for reproducibility.
- `.python-version` specifies the project's preferred Python version.
- `.venv/` contains the local Python virtual environment and is excluded from version control.
