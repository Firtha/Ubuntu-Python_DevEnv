# Bitcoin cryptographie asymétrique

## Description du dépôt Git

Ce dépôt contient les éléments nécessaires au TP de Cryptographie asymétrique concluant le cours de présentation du même sujet.
Ce cours fait partie intégrante d'un support pédagogique sur le sujet ZeroNet.

L'objectif de ce TP est, grâce à Python, de produire une clé privé à la manière de Bitcoin (utilisant la librairie du même nom).
Nous utiliserons ensuite les formules mathématiques présentées dans le cours pour produire une clé publique à partir de cette clé privé, ainsi qu'une adresse à partir de cette adresse.

Ces deux clés seront ensuite utilisées pour chiffrer puis déchiffrer le fichier de votre choix, afin de pouvoir constater le résultat produit par le chiffrement et sa capacité à redevenir lisible suite au déchiffrement.


Pour cela ce projet contient une machine virtuelle Ubuntu 18.04 avec toutes les dépendances nécessaires à l'exécution du programme de TP en Python mais il est aussi possible de s'affranchir de cette machine virtuelle si vous avez tous les éléments nécessaires sur votre machine hôte.

Deux programmes sont disponibles :

- KeyDerivations.py : Ce programme met en application les principes de dérivations des clés. En partant d'une clé privée, il génère une clé privé via courbe elliptique ainsi qu'une adresse à partir de la clé publique via les fonctions de Hash.
- EncryptDecrypt.py : Ce programme met en application les principes de chiffrement et de déchiffrement asymétrique. A partir d'une clé privée et une clé publique, un message est chiffré puis déchiffré de manière asymétrique.

## Installation de Vagrant

Vagrant est un outil développé par HashiCorp permettant de construire simplement des machines virtuelles, l'outil fonctionne en partenariat avec les outils virtualBox ou VmWare (au choix). Il permet de donner une couche supplémentaire de gestion, en passant par des scripts simple à écrire.

Vagrant : https://www.vagrantup.com/downloads.

Si vous avez besoin de cet environnement virtuel vous devez dans ce cas aller télécharger vagrant au préalable.

## Cloner et monter la machine virtuelle

Commencez par cloner le projet sur votre machine hôte :

```bash
$ git clone https://github.com/Firtha/Ubuntu-Python_DevEnv.git
```

Monter la machine virtuelle via l'outil vagrant, puis accédez y via ssh : 

```bash
$ cd Ubuntu-Python_DevEnv
Ubuntu-Python_DevEnv $ vagrant up && vagrant ssh
```

Une fois le tunnel ssh établis, une dernière commande d'installation de module Python doit être saisie :

```bash
$ pip3 install bitcoin
```

A savoir, voici les commandes les plus utiles de Vagrant :

```bash
# Construire / Lancer la machine virtuelle
$ vagrant up

# Entrer dans la machine virtuelle via ssh
$ vagrant ssh

# Arrêter la machine virtuelle depuis la machine hôte
$ vagrant halt

# Détruire la machine virtuelle et nettoyer la machine hôte
$ vagrant destroy
```

## Instructions

Une fois dans la machine virtuelle via la commande ssh présentée ci-dessus :

```bash
$ python3.6 KeyDerivations.py
$ python3.6 EncryptDecrypt.py
```
