
<center>
<img src="./img/logo.png" width="200"/>
</center>

# NOCROISSANT 🥐

> **Croissantage** : Art subtil consistant à s'inviter à déjeuner aux frais d'un collègue qui a eu le malheur de ne pas verrouiller sa session.

---

## C'est quoi ?

NOCROISSANT est un gardien anti-croissantage discret qui surveille votre clavier en arrière-plan.

Dès qu'une touche est pressée sur votre machine non surveillée, il :

1. **Prend une photo** avec la caméra frontale
2. **Enregistre la preuve** localement
3. **Verrouille la session** immédiatement

Résultat : vous avez une photo du coupable, et c'est lui qui ramènera les croissants.

> 💡 **Astuce** : Partagez la photo à vos collègues pour désigner publiquement le prochain fournisseur officiel de viennoiseries.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Utilisation

### Sous Windows

Double-cliquez sur `nocroissant.pyw` — aucune fenêtre de terminal n'apparaît, le programme tourne silencieusement.

### En ligne de commande

```bash
python ./nocroissant.py
```

---

## Arrêt

Appuyez sur **`ÉCHAP`** pour quitter proprement.

> ⚠️ Les signaux `KILL` sont interceptés — inutile d'essayer de contourner le système par ce biais.
