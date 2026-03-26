
![Logo NOCROISSANT](./img/logo.png)


# NOCROISSANT 

> Croissantage : Subtile art de s'inviter à déjeuner durant l'absence d'un collègue qui n'a pas verouillé sa session.


NOCROISSANT est une protection anti-croissantage qui va surveiller les touches du clavier : si une touche est pressée il prend une photo avec la caméra frontale de la machine, l'enregistre, et lock la session. 

Ainsi : 
- Vous avez une preuve que votre collègue a essayé de vous croissanter. 
- Vous n'aurez pas à ramener les croissants. 

Proposition subsidiaire : Envoyez la photo à vos collègues pour spécifier que la personne souhaite ramener les croissants pour tout le monde. 

## Installation 

```bash
pip install -r requirements.txt
```

## Lancement 

Sur windows, avec l'extension .pyw, il suffit de double-cliquer sur nocroissant.pyw. 

Si vous optez pour une execution dans le terminal : 
```
python ./nocroissant.py
```

## Arrêt 

Les signaux KILL sont interceptés pour éviter qu'un malotru essaie de contourner ce formidable système. Il suffit d'appuyer sur ECHAP pour quitter le programme. 