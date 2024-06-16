Generator Module
================

Il modulo `generator` fornisce funzioni per generare password sicure.

.. automodule:: createPassGenerator.generator
   :members:
   :undoc-members:
   :show-inheritance:

Funzioni
========

strong_pass
-----------
.. autofunction:: createPassGenerator.generator.strong_pass

La funzione `strong_pass` genera una password casuale di una lunghezza specificata.

**Argomenti:**

- `length` (int): La lunghezza desiderata della password. Valore predefinito è 12.
- `include_special` (bool): Se includere caratteri speciali. Valore predefinito è True.

**Esempio:**

.. code-block:: python

    from createPassGenerator.generator import strong_pass

    # Genera una password di 16 caratteri includendo caratteri speciali
    password = strong_pass(length=16, include_special=True)
    print(password)

get_user_data
-------------
.. autofunction:: createPassGenerator.generator.get_user_data

La funzione `get_user_data` recupera i dati dell'utente.

**Esempio:**

.. code-block:: python

    from createPassGenerator.generator import get_user_data

    # Recupera i dati dell'utente
    user_data = get_user_data()
    print(user_data)

create_file_excel
-----------------
.. autofunction:: createPassGenerator.generator.create_file_excel

La funzione `create_file_excel` crea un file Excel con i dati forniti.

**Esempio:**

.. code-block:: python

    from createPassGenerator.generator import create_file_excel

    # Crea un file Excel con i dati forniti
    create_file_excel(data)

write_to_excel
--------------
.. autofunction:: createPassGenerator.generator.write_to_excel

La funzione `write_to_excel` scrive i dati in un file Excel.

**Esempio:**

.. code-block:: python

    from createPassGenerator.generator import write_to_excel

    # Scrive i dati in un file Excel
    write_to_excel(file_path, data)

read_excel
----------
.. autofunction:: createPassGenerator.generator.read_excel

La funzione `read_excel` legge i dati da un file Excel.

**Esempio:**

.. code-block:: python

    from createPassGenerator.generator import read_excel

    # Legge i dati da un file Excel
    data = read_excel(file_path)
    print(data)
