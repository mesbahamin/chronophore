API Reference
=============

Modules
-------

chronophore
^^^^^^^^^^^

.. autofunction:: chronophore.chronophore.get_args
.. autofunction:: chronophore.chronophore.set_up_logging
.. autofunction:: chronophore.chronophore.main


config
^^^^^^

.. autofunction:: chronophore.config._load_config
.. autofunction:: chronophore.config._load_options
.. autofunction:: chronophore.config._use_default


controller
^^^^^^^^^^

.. autoexception:: chronophore.controller.AmbiguousUserType
.. autoexception:: chronophore.controller.UnregisteredUser

.. autoclass:: chronophore.controller.Status

.. autofunction:: chronophore.controller.flag_forgotten_entries
.. autofunction:: chronophore.controller.signed_in_users
.. autofunction:: chronophore.controller.get_user_name
.. autofunction:: chronophore.controller.sign_in
.. autofunction:: chronophore.controller.sign_out
.. autofunction:: chronophore.controller.undo_sign_in
.. autofunction:: chronophore.controller.undo_sign_out
.. autofunction:: chronophore.controller.sign


models
^^^^^^

.. autoclass:: chronophore.models.User
   :members:
   :private-members:
   :special-members:
   :member-order: bysource

.. autoclass:: chronophore.models.Entry
   :members:
   :private-members:
   :special-members:
   :member-order: bysource

.. autofunction:: chronophore.models.set_sqlite_pragma
.. autofunction:: chronophore.models.add_test_users


qtview
^^^^^^

.. autoclass:: chronophore.qtview.QtChronophoreUI
   :members:
   :special-members:
   :member-order: bysource

.. autoclass:: chronophore.qtview.QtUserTypeSelectionDialog
   :members:
   :private-members:
   :special-members:
   :member-order: bysource


tkview
^^^^^^

.. autoclass:: chronophore.tkview.TkChronophoreUI
   :members:
   :private-members:
   :special-members:
   :member-order: bysource

.. autoclass:: chronophore.tkview.TkUserTypeSelectionDialog
   :members:
   :private-members:
   :special-members:
   :member-order: bysource
