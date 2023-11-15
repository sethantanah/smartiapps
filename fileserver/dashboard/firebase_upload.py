import json
import os

from firebase_admin import credentials, initialize_app, storage
from django.core.files.storage import FileSystemStorage

service_account_info = {
  "type": "service_account",
  "project_id": "ulbooks",
  "private_key_id": "f0ada4c06790cc70130539cb608b10d0020f6e5b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDF+GZpEaVhvkkX\nlG7LRnN/M6kJI5c8i3wtvklb8eWo/0UEmOdO607eqSkRzL1/03drhvDxyBAuOpEk\nNknm/B4nopxd2cQwICMTfFS4LpB7QvrLKaUfTF0DGrNqDdKOa8dU48Wo5OdB6Kun\n3XY3DEb8T+wW7WpRY7YtbHD1kQvE0SylSKocE7EbLPKYQ/KlHJL2yF4NRKx6cukL\nZgNKyllh1cIEXwhCYA/WEvW40CRx/+woQ9PsfJ+xKVIFbSYjgbB0Hd6OKPglw9xq\nqG+O03rs8Ha4YS5iugAwgkAE6lbfjdnjLxFiaimK5B78LL0hNKUUPmEv+gB+v1cS\nICh2z2nTAgMBAAECggEABQZmlxEnGQGK+mm+nDNIGDj39+7q1lMWDlUvqIFN2onM\nNy8oY+TuJhG2JKkFQFreQ6DzubdhzcKXz4r/Ojk5DLmAbZNq+uu96C82OUyZRz+u\nfPysH8zA6aTCXBVIvGu47gswB7bztcURolupNgF+RcZDkFtrYPB+fc2sWldZrJ+1\nJQWZRrtgq0gbal/w6QRsv1yK1tmsI1Jrgm3Xf3KbepjfrfuOnHtNR17g+B/PCqil\nynMKPFqPaOwWaB5oKbodzFAf7VFmgOs9pbm4bbWa4+u2aUeN3EFzVLOBaHUJvdI3\nvKxFrcOQSzh+DPUM05EShqrm4addvhU0rE/wwMK1WQKBgQDxbsYT/SHz2YdWm7QM\nsX3Ygt+jCv5HwJDgSAWgQuel5uJK4pd7U1tkrBxk4p5tiw5bSfWv089w6JbKN65+\nzOXeoO2eSNIVJ3JzqtsDIUFU3VdSVNdvTgWpmHzeIGW7LWXvZel7DvYGTSjzuneV\nLZ1u2P/42K0y3xI7CT/nDGHOyQKBgQDR6kvBPJ8w9YEu9OO5ynqtQDvNL0lla2OP\nhOtJNZNNzYl3xQXczEB+H7R+XoAFKVGt8Gnj3NgAT4lSwYn6poNFGen2VZoC4ICR\nJrMpQ8iwLOYdO+qF8Go5yuhbW6OWQSDT9f++LbZ01lksufWEMSnHsyMVidDIKxxV\nlnCFBT/1uwKBgDLNGkTOeLx0wzOII8Sf/Fj4gNIv1/2FGXb38KceLNwNzwPu1e0P\nRyXRyU+5F5j5L5Yp49aRfQ7HAiOev8rSlnPX7Ofnbr0gxcZs5xSrhLG0uVELpSE4\ni5x6B5w9uOo/zTkoeo54QXBl//34+HydUokmhAX6occYhR+C/L1DL7lxAoGAOcaY\n7yi2UA1ibwAsJZjbRxAk5YacVvPFxVy6Pb4nOwTVT0fFI058ebpUPWvZJJKIzq0b\nGAJS2VMK4uIuDfUCsGQ/hvNsnloYSNsz+KmVdRgGhglVtWPEeP+mEG8aiWKHnI9a\nwodmbqYIiUztjGLTswlVILp74nwrIktz0MjvH70CgYEAqYlq1lNSFPh5Ib7sGATe\nz90KfxoUx6nvO9M0crtutfWXM5WjHfTcni5t0NFQcxC1HR5oInmXak1G0qY6CfWh\nPaRlkswG1942pnX774xqLF9eBtuM2rT1KnFLk1EcCZe4nAUMx1Cnjs6ntcpCZ5yV\nqAYO8pzPGf/yuTLvl1yBo68=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-c2g6s@ulbooks.iam.gserviceaccount.com",
  "client_id": "114959901181048133906",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-c2g6s%40ulbooks.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


 #json.loads(os.environ.get('FIREBASE_SERVICE_ACCOUNT_KEY'))
cred = credentials.Certificate(service_account_info)
initialize_app(cred, {'storageBucket': 'ulbooks.appspot.com'})


def uploadfile(file):
    # Put your local file path
    fileName = file_path(file)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
    fs = FileSystemStorage()
    fs.delete(file.name)
    return blob.public_url


def delete_firebase_file(file):
    print(file)
    storage.bucket()
    blob = storage.bucket()
    #blob.delete_blob(f'/opt/render/project/src/fileserver/songdir/{file}')


def file_path(file):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    uploaded_file_path = fs.path(filename)
    return uploaded_file_path
