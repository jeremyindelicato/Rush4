@echo off
echo.
echo ========================================================
echo   Lancement de l'Application de Prediction Marketing
echo ========================================================
echo.

REM Verifier si streamlit est installe
streamlit --version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Streamlit n'est pas installe. Installation en cours...
    pip install streamlit plotly
    echo [OK] Installation terminee
    echo.
)

REM Verifier si le modele existe
if not exist "xgboost_champion_optimized.pkl" (
    echo [ERREUR] Le fichier 'xgboost_champion_optimized.pkl' est introuvable
    echo [INFO] Assurez-vous que le modele est dans le dossier 02_Prediction/
    echo.
    pause
    exit /b 1
)

echo [OK] Modele detecte
echo [OK] Lancement de l'application...
echo.
echo URL: http://localhost:8501
echo.
echo Pour arreter l'application : Ctrl+C
echo.

REM Lancer l'application
streamlit run app_prediction.py

pause
