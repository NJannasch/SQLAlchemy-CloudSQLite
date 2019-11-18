from setuptools import setup

setup(name='sqlalchemy_cloudsqlite',
      version='0.1',
      description='Cloud baked SQLite for Serverless Computing',
      url='https://github.com/njannasch/SQLAlchemy-CloudSQLite',
      author='Nils Jannasch',
      author_email='nils@njann.de',
      license='MIT',
      packages=['sqlalchemy_cloudsqlite'],
      install_requires=['sqlalchemy', 'boto3'],
      entry_points={
          "sqlalchemy.dialects": [
              "cloudsqlite = sqlalchemy_cloudsqlite.dialect:CloudSQLiteDialect",
          ],
      }
      )
