#!/bin/bash

echo "🚀 Lancement de l'Application de Prédiction Marketing"
echo "======================================================"
echo ""

# Vérifier si streamlit est installé
if ! command -v streamlit &> /dev/null
then
    echo "⚠️  Streamlit n'est pas installé. Installation en cours..."
    pip install streamlit plotly
    echo "✅ Installation terminée"
    echo ""
fi

# Vérifier si le modèle existe
if [ ! -f "xgboost_champion_optimized.pkl" ]; then
    echo "❌ ERREUR: Le fichier 'xgboost_champion_optimized.pkl' est introuvable"
    echo "📁 Assurez-vous que le modèle est dans le dossier 02_Prediction/"
    echo ""
    exit 1
fi

echo "✅ Modèle détecté"
echo "✅ Lancement de l'application..."
echo ""
echo "🌐 L'application s'ouvrira dans votre navigateur"
echo "📍 URL: http://localhost:8501"
echo ""
echo "💡 Pour arrêter l'application : Ctrl+C"
echo ""

# Lancer l'application
streamlit run app_prediction.py
