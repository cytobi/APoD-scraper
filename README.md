# APoD-scraper

A tool to scrape the [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html).

## Install

Use [pip](https://pip.pypa.io/en/stable/) to install dependencies:
- requests
```bash
python3 -m pip install -U requests
```
- Beatiful Soup
```bash
python3 -m pip install -U beautifulsoup4
```

## Usage

- Make sure the tool can write to APoD-scraper/results/img.jpg
- Make sure you have wget:
```bash
wget -V
```
- Run the script (while in APoD-scraper/scripts):
```bash
python3 main.py
```

## Contributors
- [cytobi](https://github.com/cytobi)

## License

[MIT](https://choosealicense.com/licenses/mit/)
