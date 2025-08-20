# eteaching.plone.openbadges

Open Badge integration for [Plone 6](https://plone.org/).

Plone is enabled to host open badges with the add-on. The operator of the Plone website acts as the issuing institution. Schemas have been defined for two content types: for the OpenBadge and the BadgeAssertion. The OpenBadge is created by the organizer of the education program for which the badge is awarded, with a graphic in the form of an SVG file and award criteria. The so-called BadgeAssertion is created from this template for an individual person and additionally provided with information about the awarding institution. Encrypted information about the earner is also included in the form of an email address of a registered plone member. The badge assertion is thus the personalized badge and can then be shared by the recipient.

## Features

- Provides a way to create Open Badges
- Provides a way to host Open Badges
- Provides a way to register an issuing organization
- Provides a view that allows Open Badges to be viewed, shared, and validated.


## Prerequisites
- Plone 6.1 (Classic UI), Plone 6.0 (Classic UI)
- Python3 3.10, 3.12, 3.13 (Plone 6.1), 3.8, 3.9, 3.10, 3.11 (Plone 6.0)
- Python3 venv module
- Git

## Install with Plone 6.1 buildout

```bash
mkdir eteaching.plone.openbadges
cd eteaching.plone.openbadges
git clone https://github.com/e-teachingorg/eteaching.plone.openbadges.git .
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
