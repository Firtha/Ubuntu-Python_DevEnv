# Bitcoin cryptographie asymétrique

## Description du dépôt Git

Ce dépôt contient les éléments nécessaires au TP de Cryptographie asymétrique concluant le cours de présentation du même sujet.
Ce cours fait partie intégrante d'un support pédagogique sur le sujet ZeroNet.

L'objectif de ce TP est, grâce à Python, de produire une clé privé à la manière de Bitcoin (utilisant la librairie du même nom).
Nous utiliserons ensuite les formules mathématiques présentées dans le cours pour produire une clé publique à partir de cette clé privé, ainsi qu'une adresse à partir de cette adresse.

Ces deux clés seront ensuite utilisées pour chiffrer puis déchiffrer le fichier de votre choix, afin de pouvoir constater le résultat produit par le chiffrement et sa capacité à redevenir lisible suite au déchiffrement.


Pour cela ce projet contient une machine virtuelle Ubuntu 18.04 avec toutes les dépendances nécessaires à l'exécution du programme de TP en Python mais il est aussi possible de s'affranchir de cette machine virtuelle si vous avez tous les éléments nécessaires sur votre machine hôte.

## Installation de Vagrant

Vagrant est un outil développé par HashiCorp permettant de construire simplement des machines virtuelles, l'outil fonctionne en partenariat avec les outils virtualBox ou VmWare (au choix). Il permet de donner une couche supplémentaire de gestion, en passant par des scripts simple à écrire.

Vagrant : https://www.vagrantup.com/downloads.

Si vous avez besoin de cet environnement virtuel vous devez dans ce cas aller télécharger vagrant au préalable.

## Cloner et monter la machine virtuelle

## Instructions