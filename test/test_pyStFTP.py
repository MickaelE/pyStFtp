from unittest import TestCase

from src.pyStFTP.pyStFTP import create_sftp_client, create_sftp_client2


class Test(TestCase):
    def test_create_sftp_client(self):
        host = 'localhost'
        port = 22
        username = 'mickael.eriksson'
        keyfile_path = '/Users/mickael.eriksson/.ssh/id_rsa.pub'
        password = 'Tea4ever'

        sftpclient = create_sftp_client(host, port, username, password,
                                        keyfile_path,
                                        'RSA')

        # Download
        filepath = "/etc/passwd"
        localpath = "/home/remotepasswd"
        sftpclient.get(filepath, localpath)

        # Upload
        filepath = "/home/foo.jpg"
        localpath = "/home/pony.jpg"
        sftpclient.put(localpath, filepath)

        # Close
        if sftpclient:
            sftpclient.close()
