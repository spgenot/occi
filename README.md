# occi
Description du code:
	- Un package trajectories: contient les modules définissant les trajectoires et le modèle
	- Un package test: contient toutes les unittest et un générateur de trajectoires
	- un script main, sans paramètre, qui run les différentes fonctionnalités possible (un plot d’une seule trajectoire, un plot de plusieurs trajectoires, le modèle et le plot contenant les points pauses pour chaque trajectoire)		

Modèle: 
	- Trajectoire sont modélisé par (x,y,t)
	- Par simplicité, on ne considère pas l’erreur
	- On considère une pause comme une zone de plus forte densité de points
	- On utilise l’algorithme DBScan pour découvrir ces pauses.
	- DBScan nous donne:
		- des points qui appartiennent a un même cluster, donc en pause.
		- des outliers, autrement dit des points en mouvement

Preprocessing:
	- On applique le pre-processing le plus simple possible
	- L’algorithme doit pouvoir comparer les différentes dimensions entre elles
	- Par exemple t doit être comparable à x et y
	- => On normalise les valeurs pour les ramener entre 0 et 1. 
	- Notez que (x,y) représentent les même types de dimensions, et donc doivent être normalisés par les mêmes valeurs.

Choix des paramètres:
	- DBScan a deux paramètres: eps et num_points
	- num_points indique les nombres de points minimum qui peuvent former un cluster
	- choix: 30. 30 points dans le même cluster implique un pause de 3.5 secondes à peu près. En dessous de ce chiffres, il n’est pas raisonnable de considérer le cluster comme un pause.
	- eps: on étudie heuristiquement plusieurs valeurs de eps. Un epsilon trop petit nous donne pas assez de pauses (trop restrictif), alors qu’un choix de eps trop grand à tendance a regrouper les clusters entres eux. On trouve que eps=0.004 fonctionne correctement.

Points à améliorer:
	- considérer l’erreur (en modélisant des distributions de points et non des points fixes par exemple)
	- Mieux rationaliser les choix de eps: toujours difficile avec DBScan, mais peut être possibilité d’utiliser des metrics propres à la trajectoire
	- Meilleure évaluation du modèle. Comment évaluer si le modèle est performant? Un test set sur lequel des pauses auraient étaient annotés?
	- Explorer d’autres algorithms potentiels.
