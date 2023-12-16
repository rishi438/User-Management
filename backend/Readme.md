# Setup
Python 3.10.9 {{pip 23.3.1}}

# Installation 
1. Create a virtual environment:
```
python -m venv c:\path\to\<venv name>
```    
2. Activate the virtual environment:
- For Windows CMD:
  ```
  C:\> <venv>\Scripts\activate.bat
  ```
- For Windows Powershell:
  ```
  C:\> <venv>\Scripts\Activate.ps1
  ```
3. Install project dependencies:
```
pip install -r requirements.txt
```

Running Application
```
 uvicorn main:app --reload
```
