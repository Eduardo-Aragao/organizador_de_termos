@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python main.py
echo.
echo Processo concluido. Pressione qualquer tecla para sair.
pause >nul