lfrom setuptools import setup, find_packages

setup(
    name='y',  # שם החבילה שלך
    version='0.1',  # גרסה של החבילה
    packages=find_packages(),  # זה ימצא את כל החבילות בתיקיות בתוך המאגר
)
