# 🚀 CrawlerUgo

**Crawler Ugo** is a Python package for recursively crawling directories, collecting file stats, and executing custom actions on each file.  
It’s perfect for building file search tools, batch processors, or custom directory explorers.

---

## 📦 Installation

```bash
$ pip install crawlerugo
```




## Usage
crawl() takes three arguments
=> path (str), function (callable), max_depth (int|None) = None

``` python
from crawlerugo.crawler import crawl
import os

# Set your target directory
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def main():
    # Crawl the directory and run a custom action on each file
    result = crawl(base_dir, lambda f: f, 1000)  # max_depth is optional but if present indicates the debth count to crawl
    print("Crawled Data:", result)

if __name__ == "__main__":
    main()
```