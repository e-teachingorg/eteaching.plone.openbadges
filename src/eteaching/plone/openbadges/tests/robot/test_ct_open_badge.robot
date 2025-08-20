# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s eteaching.plone.openbadges -t test_open_badge.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src eteaching.plone.openbadges.testing.ETEACHING_PLONE_OPENBADGES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/eteaching/plone/openbadges/tests/robot/test_open_badge.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a OpenBadge
  Given a logged-in site administrator
    and an add OpenBadge form
   When I type 'My OpenBadge' into the title field
    and I submit the form
   Then a OpenBadge with the title 'My OpenBadge' has been created

Scenario: As a site administrator I can view a OpenBadge
  Given a logged-in site administrator
    and a OpenBadge 'My OpenBadge'
   When I go to the OpenBadge view
   Then I can see the OpenBadge title 'My OpenBadge'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add OpenBadge form
  Go To  ${PLONE_URL}/++add++OpenBadge

a OpenBadge 'My OpenBadge'
  Create content  type=OpenBadge  id=my-open_badge  title=My OpenBadge

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the OpenBadge view
  Go To  ${PLONE_URL}/my-open_badge
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a OpenBadge with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the OpenBadge title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
