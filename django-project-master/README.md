<h1 align="center">Manish's Django Showcase</h1>

<!-- NEW BADGES-->

**Table of Contents:**

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [Python installation on Ubuntu](#python-installation-on-ubuntu)
    - [PostgreSQL installation on Ubuntu](#postgresql-installation-on-ubuntu)
- [Installation](#installation)
  - [Virtual Environment (`venv`)](#virtual-environment-venv)
  - [Running the project](#running-the-project)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project

View project **[here!](http://django.life/)**

Django—an open-source web framework that's designed on top of Python—can help you quickly bring your website ideas to life. This project utilizes Bootstrap 4 and vanilla JavaScript for the front-end, and a PostgresSQL database, with GraphQL used for API functionality. It also uses Selenium for test-driven development. Finally, this is will be deployed on a [DigitalOcean](https://digitalocean.com/) Droplet under their smallest plan, so I apologize for any issues regarding speed or connectivity!

<!-- GETTING STARTED -->
## Getting Started

For development, you will need Python 3.6 or higher, pip, venv, and PostgeSQL installed in your environment.

### Prerequisites

* A good understanding of web development (HTML, CSS, JavaScript)
* Basic knowledge of Python and SQL database systems
* Familar with Django framework for front-end and back-end development
* Object-oriented Programming (OOP) paradigm
* Model-View-Controller (MVC) paradigm
* Model-View-ViewMode (MVVM) paradigm
* Knowledge and use of the Command-line Interface (CLI)

#### Python installation on Ubuntu

On Ubuntu 20.04 and later, Python 3 comes pre-installed. Check first to see if you have the tools required already installed:

    $ python3 --version
    $ pip3 --version

Head over to the [official Python website](https://www.python.org/downloads/) and download the installer
Also, be sure to have `git` donwloaded and available in your PATH as well.

You can install Python and pip easily with apt install, just run the following commands:

    $ sudo apt install python3
    $ sudo apt install python3-pip

There are a few more packages and development tools to install to ensure that we have a robust setup for our programming environment:

    $ sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

If you need to update `pip`, you can make it using `pip`! Cool right? After running the following command, just open again the command line and be happy.

    $ python3 -m pip install --upgrade pip

#### PostgreSQL installation on Ubuntu

Installation of PostgreSQL via CLI:

```bash
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get install postgresql
```

Installation of the pgAdmin GUI:

```bash
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/
`lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
$ sudo apt-get update
$ sudo apt-get install pgadmin4 pgadmin4-apache2 -y
```
