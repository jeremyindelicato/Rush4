#!/bin/bash

echo "🔧 Fix XGBoost - Installation simplifiée de libomp ARM64"
echo "========================================================="
echo ""

# Chemin vers le venv
VENV_PATH=".venv"
XGBOOST_LIB="$VENV_PATH/lib/python3.9/site-packages/xgboost/lib"

# Vérifier que le venv existe
if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Erreur: Environnement virtuel non trouvé"
    echo "   Exécutez d'abord: python3 -m venv .venv"
    exit 1
fi

# Vérifier que xgboost est installé
if [ ! -d "$XGBOOST_LIB" ]; then
    echo "❌ Erreur: XGBoost non trouvé dans le venv"
    echo "   Exécutez d'abord: source .venv/bin/activate && pip install xgboost"
    exit 1
fi

echo "✅ XGBoost trouvé dans: $XGBOOST_LIB"
echo ""

# Méthode 1: Installer Homebrew ARM64 et libomp
echo "📦 Méthode: Installation via Homebrew ARM64"
echo ""

# Vérifier si Homebrew ARM64 existe
if [ ! -f "/opt/homebrew/bin/brew" ]; then
    echo "⚠️  Homebrew ARM64 n'est pas installé."
    echo "📝 Installation de Homebrew ARM64 (cela peut prendre quelques minutes)..."
    echo ""

    arch -arm64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    if [ $? -ne 0 ]; then
        echo "❌ Erreur lors de l'installation de Homebrew ARM64"
        exit 1
    fi

    echo "✅ Homebrew ARM64 installé"
fi

# Installer libomp
echo ""
echo "📦 Installation de libomp ARM64..."
/opt/homebrew/bin/brew install libomp

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'installation de libomp"
    exit 1
fi

echo ""
echo "✅ libomp ARM64 installé!"
echo ""

# Vérifier l'installation
if [ -f "/opt/homebrew/opt/libomp/lib/libomp.dylib" ]; then
    echo "✅ Vérification: libomp.dylib trouvé"
    echo "   Architecture:"
    file /opt/homebrew/opt/libomp/lib/libomp.dylib
    echo ""
    echo "🎉 Installation terminée avec succès!"
    echo ""
    echo "🚀 Vous pouvez maintenant lancer l'application:"
    echo "   source .venv/bin/activate"
    echo "   streamlit run app_prediction.py"
else
    echo "❌ Erreur: libomp.dylib non trouvé"
    exit 1
fi
