Changelog
=========

0.8.0 - Released (2022-05-01)
-----------------------------

* Ensure encoding detection is also applied to imports.
* Trap a couple pathological import cases that result in the loader not
  halting.

0.7.0 - Released (2021-07-06)
-----------------------------

* Ensure that any error raised during import be traped and ultimately
  result in an import loader error being raised, such that further
  processing on the partially loaded model may still be possible.

0.6 - Released (2016-03-08)
---------------------------

* Updated CeLEDS definitions to latest upstream snapshot.  Includes
  fixes for the Python code generation.
* Use CellML component name only as the identifier, as cmeta:id is of a
  different specification.  This is done for compatability reason.

0.5 - Released (2014-08-14)
---------------------------

* Allow the overriding of standard urljoin methods for alternative url
  openers.

0.4 - Released (2013-07-08)
---------------------------

* Include the latest CeLEDS file from the CellML API.
* Reconciled the difference in the types to represent UTF-8 encoded
  strings.

0.3 - Released (2012-10-03)
---------------------------

* Updated to make use of cgrspy.

0.2 - Released (2012-02-13)
---------------------------

* Made use of the Python bindings as found in CellML API 1.10.


0.1 - Released (2011-04-08)
---------------------------

* Released without any usage of the CellML API Python bindings due to
  lack of formalized installation process for the bindings at that time,
  but done so anyway to preserve usage of the method calls to here by
  PMR2.

