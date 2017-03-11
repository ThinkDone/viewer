# Setup Process

```shell
scrapy startproject viewer
cd viewer
scrapy genspider -l
scrapy genspider -t crawl eyes delete.it
```

# Usage

```shell
scrapy crawl eyes -a url=https://www.behance.net/
```