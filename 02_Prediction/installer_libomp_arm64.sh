#!/bin/bash

echo "🔧 Installation de libomp ARM64 pour XGBoost"
echo "=============================================="
echo ""

# Vérifier si on est sur ARM64
ARCH=$(uname -m)
if [ "$ARCH" != "arm64" ]; then
    echo "❌ Ce script est pour Mac Apple Silicon (ARM64)"
    echo "   Votre architecture: $ARCH"
    exit 1
fi

echo "✅ Architecture détectée: $ARCH (Apple Silicon)"
echo ""

# Vérifier si Homebrew ARM64 est installé
if [ ! -f "/opt/homebrew/bin/brew" ]; then
    echo "📦 Installation de Homebrew ARM64..."
    echo "⚠️  Cela peut prendre quelques minutes"
    echo ""

    # Installer Homebrew pour ARM64
    arch -arm64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    if [ $? -ne 0 ]; then
        echo "❌ Erreur lors de l'installation de Homebrew"
        exit 1
    fi

    echo "✅ Homebrew ARM64 installé"
else
    echo "✅ Homebrew ARM64 déjà installé"
fi

echo ""
echo "📦 Installation de libomp ARM64..."

# Installer libomp avec Homebrew ARM64
/opt/homebrew/bin/brew install libomp

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'installation de libomp"
    exit 1
fi

echo ""
echo "✅ libomp ARM64 installé avec succès!"
echo ""

# Vérifier l'installation
if [ -f "/opt/homebrew/opt/libomp/lib/libomp.dylib" ]; then
    echo "✅ Vérification: libomp.dylib trouvé"
    file /opt/homebrew/opt/libomp/lib/libomp.dylib
    echo ""
    echo "🎉 Installation terminée avec succès!"
    echo ""
    echo "Vous pouvez maintenant lancer l'application:"
    echo "  cd 02_Prediction"
    echo "  source .venv/bin/activate"
    echo "  streamlit run app_prediction.py"
else
    echo "❌ Erreur: libomp.dylib non trouvé après installation"
    exit 1
fi
