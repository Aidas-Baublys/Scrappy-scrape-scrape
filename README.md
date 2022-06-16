# Scrappy-scrape-scrape

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Aidas-Baublys/Scrappy-scrape-scrape/blob/LICENSE.md)

<!-- TOC -->
* [Scrappy-scrape-scrape](#Scrappy-scrape-scrape)
  * [About](#about)
    * [Usage](#usage)
      * [Automatic launch](#automatic-launch)
      * [Manual launch](#manual-launch)
    * [Requirements](#requirements)
<!-- TOC -->

## About

Also known as Putin & Porn console app, this small project scrapes news headlines and story leads about Putin from one Lithuanian news site and, with some help from the user, writes a fan fiction novel using only porn video titles from pornhub.

### Usage

#### Automatic launch

For Windows installation just **run automatic setup script** in Git Bash:

```bash
bash <(curl -s https://raw.githubusercontent.com/Aidas-Baublys/Scrappy-scrape-scrape/master/setup.sh)
```

#### Manual launch

1. Clone this repo:

   ```bash
   git clone https://github.com/Aidas-Baublys/Scrappy-scrape-scrape.git
   ```

2. Navigate into project:

   ```bash
   cd Scrappy-scrape-scrape/
   ```

3. Ensure pipenv is installed:

   ```bash
   pip install --upgrade pipenv --user
   ```

4. Install dependencies:

   ```bash
   pipenv install
   ```

5. Activate virtual environment:

   ```bash
   pipenv shell
   ```

6. Run project:

   ```bash
   python ./Scrappy-scrape-scrape/main.py
   ```

7. Enjoy.

## Requirements

* [X] Scrape one or more websites, that are publicly available - it can be a minimal project, or
you can go as in depth as you like.
* [X] It must scrape at least 2 kinds pages with navigation either in depth or breadth (e.g.:
items page + item page) - this is the minimal requirement to get a positive grade.
* [X] You can use any library / framework, but if you use bs4, selenium, requests-html please use
recommended python project structure.
* [X] It must contain a config file - you decide what parameters need to be configurable, simple
options: url, selectors, port, logging level, etc.
* [X] It must log errors to a centralized file - at least one log file, for example main.log.
* [X] Code is hosted in GitHub (can be private, but please invite the teacher as a collaborator to
verify the project) with at least 3 commits, containing readme file with launch instructions
(document how to launch the project easily), requirements.txt (or equivalent).
