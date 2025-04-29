# 🚀 Space Fleet Manager – Text-Based Fleet Management Game

**Space Fleet Manager** est un jeu en ligne de commande dans lequel vous incarnez le gestionnaire d'une flotte spatiale. Recrutez des membres d’équipage, maintenez vos vaisseaux en bon état et gérez des événements aléatoires pour assurer la survie de votre flotte.

---

## 📦 Bibliothèques requises

### 🔹 Modules standards (inclus avec Python)

- `json` : lecture et écriture des données au format JSON  
- `random` : génération d'événements aléatoires  
- `atexit` : exécution d'une fonction à la fermeture du programme

### 🔹 Fichiers personnalisés (à placer dans le même dossier que le script principal)

- `fleet.py` : gestion de la flotte  
- `spaceship.py` : caractéristiques des vaisseaux  
- `crew.py` : gestion de l'équipage  
- `Operator.py` : gestion des opérateurs spécialisés  
- `mentalist.py` : personnages dotés de pouvoirs spéciaux  
- `member.py` : membres d’équipage de base

---

## 🛠️ Installation & Lancement

1. **Installer Python** :  
   Téléchargez [Python 3.10 ou supérieur](https://www.python.org/downloads/)

2. **Organisation des fichiers** :  
   Placez tous les fichiers `.py` dans le même dossier

3. **Initialisation** :  
   Lancez le script principal une première fois pour générer le fichier `fleet.json` (sauvegarde automatique des données)

---

## 🎮 Comment jouer

### 1. Démarrage

- Si l'option **Auto Load** est activée, les données sont automatiquement chargées  
- Sinon, le jeu démarre avec une flotte vide

### 2. Menus principaux

- 🛸 **Gestion de flotte** : ajouter, modifier ou supprimer des vaisseaux  
- 👨‍🚀 **Gestion de l’équipage** : assigner des rôles, faire évoluer les membres  
- ⚙️ **Paramètres** : activer/désactiver l'auto-save, modifier les options  
- 💾 **Sauvegarde & chargement** : automatique à la fermeture si activée  
- ❌ **Quitter** : fermeture du jeu (avec sauvegarde si activée)

### 3. Navigation

- Système de menus numérotés  
- Saisissez simplement le numéro correspondant à l'action souhaitée

---

## ✨ Fonctionnalités principales

### ✅ Initialisation automatique

- Le fichier `fleet.json` est généré si absent  
- Paramètres par défaut : auto-save et auto-load désactivés (modifiable)

### 🛸 Gestion de flotte

- Ajouter des vaisseaux (nom, type, état)  
- Modifier ou supprimer des vaisseaux  
- Afficher les détails de la flotte

### 👨‍🚀 Gestion de l’équipage

- Recruter des membres avec des rôles spécifiques (pilote, technicien, mentaliste, etc.)  
- Faire évoluer leurs compétences  
- Utiliser des compétences spéciales

### 🌌 Événements aléatoires

- Des événements inattendus (pannes, destructions, etc.) affectent la flotte  
- Augmente la difficulté et le réalisme de la gestion

---

## 🧪 Exemple de session

1. Lancer le jeu  
2. Accéder au menu principal  
3. Ajouter un nouveau vaisseau  
4. Recruter un équipage  
5. Gérer les événements aléatoires et maintenir la flotte en état

---

*Contributions, retours ou améliorations bienvenus !*
