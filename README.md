# eteaching.plone.openbadges

Open Badge integration for [Plone 6](https://plone.org/).

Once the add-on has been installed, the Plone CMS operator can act as the issuing institution. This means they can use a control panel to enter their organisation's data, as well as any necessary prefixes for badge titles. They can then create a new badge in the portal using the new OpenBadges content type. This template provides a title, description, SVG image, award criteria and an associated resource. Additionally, an award period can be specified during which registered Plone members can collect the badge. The badge assertion (the personalised badge) is then automatically generated in the OpenBadge folder. To generate this, a logged-in Plone member must be directed to the badge's URL. This can be done via a link at the end of a successfully completed course, for example. The member will then receive a note detailing the criteria for receiving the badge and will be able to generate it with a single click and switch to the personalised badge view. There, the hosted badge can be verified by entering the email address or using the assertion from external systems. Additionally, badge recipients have the option to share their badge.

## Features

- Provides a way to create Open Badges
- Provides a way to host Open Badges
- Provides a way to register an issuing organization
- Provides a view that allows Open Badges to be viewed, shared, and validated.


## Prerequisites
* Plone 6.1 (Classic UI), Plone 6.0 should also work
* Python 3.10, 3.12, 3.13
* Git

## Install with Plone 6.1 buildout

```bash
git clone https://github.com/e-teachingorg/eteaching.plone.openbadges.git
cd eteaching.plone.openbadges
python3 -m venv .
bin/pip install -r https://dist.plone.org/release/6.1-latest/requirements.txt
bin/buildout
```

### Activate

```bash
bin/instance fg
```
* Point your browser to http://localhost:8080
* Add a new Plone Site (Classic UI)
* Login with admin admin
* Goto admin --> configuration --> extensions
* eteaching.plone.openbadges [Install]

## Install as source packages using buildout

Open your dev.cfg

```bash
[buildout]
extends = buildout.cfg

parts +=
    instance

auto-checkout +=
    eteaching.plone.openbadges

[instance]
eggs +=
    eteaching.plone.openbadges

[sources]
eteaching.plone.openbadges = git https://github.com/e-teachingorg/eteaching.plone.openbadges.git
```

### Rerun buildout

```bash
bin/buildout -c dev.cfg
```

### Activate

```bash
* Start Plone
* Point your browser to your plone site
* Login as admin
* Goto configuration --> extensions
* Install eteaching.plone.openbadges
```

## Authors

[Markus Schmidt](https://github.com/Arkusm)

## Contribute

- Issue Tracker: https://github.com/e-teachingorg/eteaching.plone.openbadges/issues
- Source Code: https://github.com/e-teachingorg/eteaching.plone.openbadges

## Support

If you are having issues, please let us know.

## License

The project is licensed under the GPLv2.

## Funding information
The eteaching.plone.openbadges was funded as part of a publicly financed project by the Federal Ministry of Research, Technology and Space of the Federal Republic of Germany.
