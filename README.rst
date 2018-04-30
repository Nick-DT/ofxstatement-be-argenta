ofxstatement-be-argenta
=======================

This is a plugin for the tool `ofxstatement`_. It parses the ``downloadTransactionHistoryXLS.xlsx`` file exported from the Belgian bank Argenta and writes is as an OFX file.

Usage
=====

  $ ofxstatement convert -t argenta downloadTransactionHistoryXLS.xlsx output.ofx

Credit
======

Credit to `kedder`_ for writing ofxstatement. 
And credit to `themalkolm`_ for writing the plugin `ofxstatement-seb`_ for parsing xlsx. I forked this project from it.

.. _ofxstatement: https://github.com/kedder/ofxstatement
.. _kedder: https://github.com/kedder
.. _themalkolm: https://github.com/themalkolm
.. _ofxstatement-seb: https://github.com/themalkolm/ofxstatement-seb
