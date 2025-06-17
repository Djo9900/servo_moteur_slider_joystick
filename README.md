# 🎯 Projet : Contrôle d'un Servo SG92R avec Joystick et Interface Python

![Bannière du projet](images/schema_branchement.jpg) *Si vous avez une image représentative*

## 📋 Table des matières
- [Objectif](#-objectif)
- [Matériel](#-matériel-utilisé)
- [Branchement](#️-branchement-matériel)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Code source](#-code-source)
- [Résultats](#-résultats)
- [Auteurs](#-auteurs)

## 🎯 Objectif
Développer un système interactif pour contrôler un servo-moteur SG92R à rotation continue en utilisant :
- Un joystick analogique (KY-023)
- Une interface graphique Python (Tkinter)
- Une communication série avec Arduino Uno

## 🧰 Matériel utilisé
| Composant | Quantité |
|-----------|----------|
| Servo SG92R | 1 |
| Joystick KY-023 | 1 |
| Arduino Uno | 1 |
| Câbles Dupont | 10 |

## ⚙️ Branchement matériel
### Joystick KY-023
| Broche Joystick | Broche Arduino |
|-----------------|----------------|
| GND             | GND            |
| VCC             | 5V             |
| VRx             | A0             |
| VRy             | A1 (non utilisé)|

### Servo SG92R
| Fil Servo | Broche Arduino |
|-----------|----------------|
| Rouge     | 5V             |
| Marron    | GND            |
| Orange    | D9             |

## 📦 Installation
1. Télécharger le projet :
```bash
git clone https://github.com/votreutilisateur/votredepot.git
cd votredepot
