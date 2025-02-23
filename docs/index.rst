.. Rele documentation master file, created by
   sphinx-quickstart on Wed Jun  5 14:19:08 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Relé's documentation!
================================

Release v\ |version|. (`Installation <https://github.com/mercadona/rele>`_)

.. image:: https://travis-ci.org/mercadona/rele.svg?branch=master
    :target: https://travis-ci.org/mercadona/rele

.. image:: https://img.shields.io/badge/license-Apache%202-blue.svg
    :target: https://github.com/mercadona/rele/blob/master/LICENSE

-------------------

**Relé** makes integration with Google PubSub easier and is ready to
integrate seamlessly into any Django project.


Motivation and Features
_______________________
The Publish-Subscribe pattern and specifically the Google Cloud Pub/Sub library are
very powerful tools but you can easily cut your fingers on it. Relé
makes integration seamless by providing Publisher, Subscriber and Worker
classes.

Out of the box, Relé includes the following features:

    * Simple publishing API
    * Declarative subscribers
    * Scalable Worker
    * Ready to install Django integration
    * And much more...

What It Looks Like
__________________

.. code:: python

    import rele
    from rele import sub

    # Subscribe to the Pub/Sub topic

    @sub(topic='photo-uploaded')
    def photo_uploaded(data, **kwargs):
        print(f"Customer {data['customer_id']} has uploaded an image")


    # Publish to the topic

    rele.publish(topic='photo-uploaded', data={'customer_id': 123})

Install
_______

Relé supports Python 3.6+ and installing via ``pip``

.. code::

    $ pip install rele

or with Django integration

.. code::

    $ pip install rele[django]

User Guides
___________

.. toctree::
    :maxdepth: 1

    guides/basics
    guides/django
    guides/filters
    guides/emulator


Configuration
_____________

.. toctree::
    :maxdepth: 2

    api/settings


API Docs
________

This is the part of documentation that details the inner workings of Relé.


.. toctree::
    :maxdepth: 2

    api/reference

Project Info
____________

.. toctree::
   :maxdepth: 1

    Source Code <https://github.com/mercadona/rele>
    Contributing <https://github.com/mercadona/rele/blob/master/CONTRIBUTING.md>
    Code of Conduct <https://github.com/mercadona/rele/blob/master/CODE_OF_CONDUCT.md>
    License <https://github.com/mercadona/rele/blob/master/LICENSE>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
