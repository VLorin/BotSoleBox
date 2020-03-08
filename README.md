# BotSolebox
Small bot for solebox.com, it can create an account, log in and add shoes to his basket !

## How to use
1. In `main_bot.py` edit the account details
2. Choose either `create_account()` or `login()` as creating an accounting log you in.
3. Execute
4. You can log in yourself to see if the item is in your basket !

## Démarche utilisée pour effectuer ce bot
### Reconnaissance
Après avoir exécuter l'exemple et analysé le code de `requet.py`, j'ai essayé de capturer les requêtes http avec wireshark pour regarder les en-têtes, mais comme je l'avais prédit on se retrouve très rapidement avec de l'https, ce qui rend Wireshark inutile.
Après quelques recherches je découvre l'analyseur réseau intégré dans chrome qui est l'outils parfait pour visualiser les requêtes http et https !
### Création des requêtes 
J'ai tout d'abord créé un compte manuellement pour regarder la requête https que j'emets, et là je découvre dans cette requête POST un élément nommé "stoken", surement pour session token, et qui est surement dynamique (c'est le cas). Je cherche donc un moyen de recupérer ce "stoken", après quelques recherche je tombe sur une video de "Indian Pythonista" sur youtube (merci à lui), dans laquelle il utilise la fonction BeautifulSoup pour recupérer un token similaire. J'ai ensuite eu quelques difficultés pour trouver où ce trouve l'html des réponses, j'ai mis une dizaine minutes à trouver qu'il suffisait de faire ".response" à notre objet pour avoir l'html...
J'ai maintenant (presque) tout en main pour créer la requête qui créer un compte, au début je recevais des réponses "200 OK", mais pourtant le compte ne se créait pas... Je recevais même des réponses "403 Forbidden" à force de faire trop de test. En cherchant dans les RFC 7230 & 7231 je vois qu'il me manquait l'en-tête Content-Length dans ma requête. J'intègre cet en-tête en calculant sa valeur et enfin ça marche ! Je reçois une réponse "302 Found" et effectivement je peux me connecter sur le compte.
Les requêtes pour se connecter et ajouter une paire de chaussures au panier se font sans trop de problèmes en suivant la même méthode.
### Optimsation
En gardant le strict minimum, j'émets 4 requêtes https :
- GET : Acceder une première fois à https://www.solebox.com/en/my-account/ pour récuperer "mon stoken"
- POST : Pour créer ou se connecter au compte
- POST : Ajouter les chaussures au panier
- GET : Ajouter les chaussures au panier ( je ne suis pas trop sûr, mais sans cette requête les chaussures se sont pas dans le panier)

### Piste d'amélioration 
* Pour l'instant pour choisir une paire de chaussures, il faut aller sur le site et l'ajouter manuellement et copier la requête https. Pour être plus facile à utiliser, on pourrait faire une fonction qui à partir de l'URL et de la pointure trouve toute seule les informations pour faire la requête. 
* Augmenter la vitesse sans se faire bloquer par le site
