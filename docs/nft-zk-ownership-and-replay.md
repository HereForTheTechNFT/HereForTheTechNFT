# NFT et preuves ZK : propriété et anti-rejeu

Une preuve ZK peut démontrer qu'un utilisateur satisfait une condition sans révéler tout son état. Pour un NFT, la condition peut porter sur la possession d'un token, un attribut ou une appartenance à une collection.

Le circuit doit lier explicitement la preuve au contrat, à la collection, à l'identifiant du token et au contexte réseau. Sans ce domaine de liaison, une preuve valide peut être réutilisée dans une autre application.

Un nonce, un identifiant de demande ou une racine d'état consommée empêchent le rejeu. La révocation et les changements de propriété exigent également une source d'état fraîche.

La preuve d'une propriété passée n'est donc pas nécessairement une preuve de propriété actuelle : cette distinction doit apparaître dans l'interface et dans la politique du protocole.
