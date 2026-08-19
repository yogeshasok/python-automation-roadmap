## Try /Except
In Python, try and except blocks are used to handle errors so your program does not crash when something goes wrong. This is called exception handling

Writing Exception is not recommended we should be specify the list of exception we are expecting in Except statement
```
try:
  pass
except Exception:
  pass
else:
  pass
finaly:
  pass
```
```
try:
  f = open("test.txt")
  var = bad_var
except FileNotFoundError as e:
  print(f"sorry!, file not found : {e}")
excpet Exception as e:
  print(f"Something wrong: {e}")
else:
  print(f.read())
  f.close()
finally:
  print("Runs all times") -- useful for releasing resources / clean up /closing files or database connection
```

else -- will run if try didn't thrown any exception

### Creating own Exception

use raise to thrown your own exception
```
class InvalidNumberException(Exception):
  pass
```
or
```
class InvalidNumberException(Exception):
  def __init__(self, number, message = "Invalid Number")
    self.number = number
    self.message = message
    # Pass the message to the parent Exception class
    super().__init__(self.message)

try:
  number = "852621999"
  if len(number) != 10:
    raise InvalidNumberException(number, message="Number only contains 9 digits")
  except InvalidNumberException as e:
    print(e.message)
    print(e.number)
```
  Inherit from Exception: Always make your custom error class a child of Exception.
  Naming convention: End your class name with the word Error (like NetworkTimeoutError).
  The raise keyword: Use raise followed by your error class to trigger it.

## Context Manager:
is a excellent tool that handles setup and clean up of resources (eg: we are using with keyword to open file right,  for which we don't need to add close statement. It will handled automatically because it is implementated based on context manager)
Creating custom Context Manager:
```
class SQLite:
  def __init__(self, file="application.db)
    self.file = file
  def __enter__(self):
    self.conn = sqlite3.connect(self.file)
    return self.conn.cursor()
  def __exit__(self):
    self.conn.close()

def fecth_blogs():
  try:
    with SQLite("application.db") as con:
      records = con.execute("SELECT * FROM BLOGS")
      return records
above will not work since __exit__() doesn't have required parameters. It should have type, value, traceback

def__init__(self, type, value, traceback):
  self.conn.close() --> right way

```

## Retry decorator with exception handling
consider if you trying to connect to db or somenetwork and you want to give a retry after 1st attempt
```
def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
  def deco_retry(f):
    @wraps(f)
    def f_retry(*args, **kwarg):
      mtries, mdelay = tries, delay
      while mtries > 1:
        try:
          return f(*args, **kwargs)
        except ExceptionToCheck as e:
          msg = f" {e} Retrying in {mdelay} seconds"
          if logger:
            logger.warning(,sg)
          else:
            print(msg)
          time.sleep(mdelay)
          mtries = mtries - 1
          mdelay = mdelay * backoff
      return f(*args, **kwargs)
    return f_retry
  return deco_retry

@retry(Exception, tries=4)
def test_fail(text):
  raise Exception("Fail")

```




