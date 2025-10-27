#!/bin/bash

# Script de lancement avec fix pour libomp
# Ce script résout le problème de XGBoost qui ne trouve pas libomp

echo "🔧 Configuration de l'environnement..."

# Créer le répertoire /opt/homebrew s'il n'existe pas (nécessite sudo)
echo "⚠️  Ce script va créer un lien symbolique pour libomp."
echo "📝 Vous devrez entrer votre mot de passe système."
echo ""

# Demander le mot de passe une fois
sudo -v

# Créer la structure de dossiers
sudo mkdir -p /opt/homebrew/opt/libomp

# Créer le lien symbolique vers libomp
if [ ! -L /opt/homebrew/opt/libomp/lib ]; then
    echo "🔗 Création du lien symbolique vers libomp..."
    sudo ln -sf /usr/local/opt/libomp/lib /opt/homebrew/opt/libomp/lib
    echo "✅ Lien symbolique créé"
else
    echo "✅ Lien symbolique déjà présent"
fi

# Vérifier que le lien fonctionne
if [ -f /opt/homebrew/opt/libomp/lib/libomp.dylib ]; then
    echo "✅ libomp.dylib trouvé"
else
    echo "❌ Erreur: libomp.dylib non trouvé"
    exit 1
fi

echo ""
echo "🚀 Lancement de l'application Streamlit..."
echo "📊 L'application va s'ouvrir dans votre navigateur"
echo "⏹️  Appuyez sur Ctrl+C pour arrêter l'application"
echo ""

# Activer l'environnement virtuel et lancer streamlit
cd "$(dirname "$0")"
source .venv/bin/activate
streamlit run app_prediction.py
