#!/usr/bin/env python3

import pytest
from src.metasploit.msfrpc import *


@pytest.fixture()
def client():
    client = MsfRpcClient('123')
    yield client
    client.call(MsfRpcMethod.AuthLogout)


def test_module_list(client):
    exs = client.modules.exploits
    assert "windows/smb/ms08_067_netapi" in exs


def test_module_options(client):
    ex = client.modules.use('exploit', 'windows/smb/ms08_067_netapi')
    assert "Proxies" in ex.options
    assert "RHOSTS" in ex.required


def test_module_settings(client):
    ex = client.modules.use('exploit', 'windows/smb/ms08_067_netapi')
    ex['RHOSTS'] = '127.0.0.1'
    opts = ex.runoptions
    assert opts['RHOSTS'] == '127.0.0.1'