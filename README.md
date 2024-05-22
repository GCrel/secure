# Police Emergency Call Management

Analysis system for the study of incidents in a certain province

## Before you begin, you’ll need:

### Python 3.7

#### Install

* Windows:

```bash
winget install -e --id Python.Python.3.7
```

**Note**: In Windows you have to close and open the terminal every time the environment variables are modified.

* Linux distributions based on Debian

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3.7
```

Once installed you can update the python package manager (pip)

```bash
pip install --upgrade pip
```

### Create the virtual environment

For this you must clone the repository ([or download it](https://github.com/GCrel/secure/archive/refs/heads/main.zip)) :

```bash
git clone https://github.com/GCrel/secure.git
```

Once in the root of the project directory, execute the following command:

* Windows:

```bash
python -m venv ./venv
```

* Linux

```bash
python3 -m venv ./venv
```

This will create a `venv\` folder in which all dependencies are installed. You can enter the virtual environment from a Windows ([pwsh](https://apps.microsoft.com/detail/9mz1snwt0n5d?hl=en-us&gl=AR), PowerShell, cmd) or Linux terminal with the following command:

* Windows:

```bash
.\venv\Scripts\activate
```

**Note**: In PowerShell you could get an error like `CategoryInfo: SecurityError: (:) [], PSSecurityException`. To solve it you must enter the following command:

```powershell
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
```

* Linux:

```bash
source ./venv/bin/activate
```

### Install dependencies

within the virtual environment it must be installed:

* **jupyter notebook**

```bash
pip install notebook
```

* **SQLAlchemy**

```bash
pip install sqlalchemy==1.4
```

* **cx_Oracle**

```bash
pip install cx_Oracle==8.3
```

* **Pandas**

```bash
pip install pandas
```

### Install Oracle Instant Client

You can download Oracle Instant Client (V 19.22) from [here](https://www.oracle.com/ar/database/technologies/instant-client/winx64-64-downloads.html)

#### Windows

Once downloaded, you must unzip it and obtain a folder called `instantclient_19_22`, you must move this folder to the address `C:\Program Files\Oracle\`.

**Note**: If you do not have an `Oracle` folder you must create one.

Now you just have to [add the address to the PATH](https://www.neoguias.com/agregar-directorio-path-windows/) of the user and the system (`C:\Program Files\Oracle\instantclient_19_22`).



### Access credentials

These credentials allow access to the database created, in this case only the credentials of the database created by us will be used: [Credentials](https://drive.google.com/file/d/1oSdsQlnylWkLn4mviQ5zf3ecawkQA-d-/view?usp=sharing)

**Steps**:

1. Download credentials and unzip

2. Move the folder `network` obtained to the address where the `instantclient_19_22`.

3. Enter the virtual environment.

4. Run the `jupyter notebook` command.
