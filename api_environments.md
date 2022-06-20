## Environments
- Development: environment for development, making frequent changes
- testing: environment for running test suites
- Want to be able to access both 
- Environmental variables:
  - connection string (location of database)
  - API keys
  - various config settings
- To view all **env variables**, type `env` command into terminal.
  - This can be a useful way to store sensitive/secret data

## dotenv (`.env`)
- Within `.env`, create environmental variables: URL for development_database, URL for test_database; API_keys, etc...
## gitignore (.gitignore`):
- A list of things to NOT push to github.  
- `.env` should be listed inside the .gitignore file.


**Fixtures** are a way to pass something into a unit test.  They use a decorator `@pytest.fixture`.  The name of the function is then passed into the test_function as a parameter.  This can be helpful to not have to make new assert statements for each test, and to have several different data types ready to use.
- I believe cleanup is a way to get rid of side-effects from a function (?)