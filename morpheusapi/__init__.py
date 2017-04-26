"""
About this library
==================

Morpheus is the leading Cloud Management Platform.  This API makes it very
easy to interact with your Morpheus Appliance by providing an easy to use,
conventional python interface.

Morpheus has a set of publicly documented API endpoints and a SDK, but this is
somewhat Java centric.  Luckily the endpoints for Morpheus are all REST based.
This library wraps the Morpheus REST interface to make most programmatic tasks
simpler.

This library can help you:

    * Query cloud data
    * Query billing data
    * Create instances
    * ...so much more to come (needs more documentation)

Project Author(s)
================

Adam Hicks (thomas.adam.hicks@gmail.com, ahicks@morpheusdata.com)

Current code lives on https://github.com/tadamhicks/morpheus-python
"""

from morpheusapi import (morpheus, billing)

__all__ = ["morpheus", "billing"]

__version__ = '2.11.1'
