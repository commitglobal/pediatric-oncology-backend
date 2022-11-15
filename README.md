# Pediatric Oncology Case Manager

[![GitHub contributors][ico-contributors]][link-contributors]
[![GitHub last commit][ico-last-commit]][link-last-commit]
[![License: MPL 2.0][ico-license]][link-license]

The solution enables access to healthcare service for children withcancer, providing them with timely support in case they are taking refuge fromthe war in Ukraine. The solution is agnostic of geography and can beredeployed for any need of case management for the chronically ill who needto request assistance. The solution can be adapted with custom forms andthe content on the public interface can be easily changed with no need fortechnical support. This type of digital solution is essential in the case ofdisplaced populations as it allows them to request aid fast and easy for theirmedical needs and first responders can get a clear view of what availabilityexists to support them and provide them with. The platform is multilingual andallows for multiple interfaces for as many languages as needed with no needfor extra development.

[See the project live](https://app.ukrainechildcancerhelp.ro/)

[Contributing](#contributing) | [Built with](#built-with) | [Repos and projects](#repos-and-projects) | [Deployment](#deployment) | [Feedback](#feedback) | [License](#license) | [About Commit Global](#about-commit-global)

## Contributing

This project is built by amazing civic technologists and great volunteers and you can be one of them! Here's a list of ways in [which you can contribute to this project][link-contributing]. If you want to make any change to this repository, please **make a fork first**.

Help us out by testing this project in the [staging environment](https://oncologie-pediatrica.heroesof.tech/). If you see something that doesn't quite work the way you expect it to, open an Issue. Make sure to describe what you _expect to happen_ and _what is actually happening_ in detail.

If you would like to suggest new functionality, open an Issue and mark it as a __[Feature request]__. Please be specific about why you think this functionality will be of use. If you can, please include some visual description of what you would like the UI to look like, if you are suggesting new UI elements.

## Built With

### Programming languages

Python 3.9

### Platforms

### Backend framework

Django 3.2

### Package managers

pip

### Database technology & provider

PostgreSQL

## Deployment

Guide users through getting your code up and running on their own system. In this section you can talk about:
1. Make a copy of the `.env` file, change the variables and run the build command

    ```shell
    cp .env.dev .env
    # modify the variables in the .env and then build the development container
    make build-dev
    ```

2. Software dependencies

    You can run the app through docker, if it is installed on your machine. If you wish to run it manually you will need to have `gettext` installed.

### Environment variables

The `.env` files contain variables required to start the services and initialize them.

- `ENVIRONMENT` - [`test`|`development`|`production`] sets the type of deployment (default `production`)
- `RUN_MIGRATION` - [`yes`|`no`] run django migrations when you start the app (default `yes`)
- `RUN_COMPILEMESSAGES` - [`yes`|`no`] compile i18n messages when you first start the app (default `yes`)
- `RUN_SEED_DATA` - [`yes`|`no`] load the data from the `fixtures/` folders (default `no`)
- `RUN_COLLECT_STATIC` - [`yes`|`no`] collects static data like images/fonts (default `yes` - has no effect if `ENVIRONMENT != production`)
- `RUN_DEV_SERVER` - [`yes`|`no`] starts the app in development mode with a more comprehensive debugging toolbox (default `no`)
- `DATABASE_URL` - the URL Django will use to connect to the database (should be changed if you're not running through Docker)
- `SECRET_KEY` - the secret key Django will use to encrypt data (should be changed if you're not running through Docker)

## Staging environment setup

When deploying onto a machine, there is no need to clone the whole project. You only need a `.env` and the `docker-compose.staging.yaml` file. This uses a [watchtower](https://github.com/containrrr/watchtower) container to watch for a new version of the `staging` tag of the `code4romania/oncologie-pediatrica` docker image and update the containers as necessary. 

## Feedback

* Request a new feature on GitHub.
* Vote for popular feature requests.
* File a bug in GitHub Issues.
* Email us with other feedback contact@commitglobal.org

## License

This project is licensed under the MPL 2.0 License - see the [LICENSE](LICENSE) file for details

## About Commit Global

The team behind Commit Global has a robust and celebrated track record in the tech for social good field since 2015. We have built the fastest growing organization in the space, Code for Romania and set it up as a model of good practices on how to design and build technology that helps at scale. Our tools have served governments, UN agencies and large and small CSOs during crisis and peace time. Most recently we have built, deployed and maintained a first of its kind humanitarian ecosystem in support of refugees fleeing from Ukraine, ensuring their safe and uninterrupted access to information, healthcare and services, while equipping NGOs with the tools they need to be more effective.

All throughout our activity we have been one of the champions of cooperation and co-creation in the the civic tech field, constantly investing efforts and resources in working with and supporting the work of similar organizations around the world. As part of these efforts we created, curated and hosted the largest civic tech strategic event in history, the 2018 Code for All Global Summit: a 4 days offline event where hundreds of delegates from all continents exchanged ideas and digital solutions for the benefit of humanity.

Find more details on https://www.commitglobal.org/en

[ico-contributors]: https://img.shields.io/github/contributors/code4romania/war-taskforce-oncologie-pediatrica.svg?style=for-the-badge
[ico-last-commit]: https://img.shields.io/github/last-commit/code4romania/war-taskforce-oncologie-pediatrica.svg?style=for-the-badge
[ico-license]: https://img.shields.io/badge/license-MPL%202.0-brightgreen.svg?style=for-the-badge

[link-contributors]: https://github.com/code4romania/war-taskforce-oncologie-pediatrica/graphs/contributors
[link-last-commit]: https://github.com/code4romania/war-taskforce-oncologie-pediatrica/commits/main
[link-license]: https://opensource.org/licenses/MPL-2.0
[link-contributing]: https://github.com/code4romania/.github/blob/main/CONTRIBUTING.md

[link-production]: insert_link_here
[link-staging]: insert_link_here

[link-code4]: https://www.code4.ro/en/
[link-donate]: https://code4.ro/en/donate/
