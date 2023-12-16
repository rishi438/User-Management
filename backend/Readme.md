# Setup

[[Install python]] --> python -m venv c:\path\to\<venv name> 
                   --> {{C:\> <venv>\Scripts\activate.bat --> Windows  CMD}} or {{C:\> <venv>\Scripts\Activate.ps1 --> Windows  Powershell}}
                   --> pip install -r requirements.txt

Run FastAPI --> uvicorn main:app --reload
