import pytest
import os
import PasswordWallet

### TESTS FOR GENERAL FUNCTIONS RELEVANT TO .TXT FILE ###
def test_password_wallet_exist():
    try:
        with open("password_wallet.txt"):
            assert os.path.exists("password_wallet.txt")
    except:
        pytest.raises(FileNotFoundError)

def test_password_wallet_not_empty():
    try:
        with open("password_wallet.txt") as file:
            assert file is not None
    except:
        pytest.raises(FileNotFoundError)

### TESTS FOR ADD_PSW FUNCTION ###
def test_create_dic_line():
    assert PasswordWallet.create_dic_line("atest", "123") == {"account": "atest", "password": "123"}

def test_create_new_data():
    a = [{'account': "atest", 'password': "123"}]
    b = {'account': "btest", 'password': "456"}
    assert PasswordWallet.create_new_data(a, b) == "atest , 123\nbtest , 456"

def test_update_wallet():
    old_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                old_list.append(old_line)
        a = "abc , 123"
        PasswordWallet.update_wallet(a)
        with open("password_wallet.txt") as file:
            assert "abc , 123" in file
        new_data = "".join(b for b in old_list)
        with open("password_wallet.txt", "w") as file:
            file.write(new_data)
    except:
        pytest.raises(FileNotFoundError)
