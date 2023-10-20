import pytest

from webbrowser import open_new_tab

def teste_site():
    open_new_tab("https://www.realmadrid.com/pt")
for i in range(5):
    pytest.main(teste_site())