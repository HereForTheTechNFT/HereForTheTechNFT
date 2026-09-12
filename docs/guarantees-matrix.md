# Matrice des garanties cryptographiques

Ce document sépare trois niveaux souvent confondus : la garantie mathématique de la preuve, les hypothèses cryptographiques et la politique applicative.

| Élément | Garantie | Hypothèse / limite |
|---|---|---|
| Trace et AIR | Les transitions décrites sont vérifiables | L'AIR doit représenter le calcul réel |
| Engagement polynomial | Une trace engagée peut être ouverte avec cohérence | La résistance dépend du hash et du domaine |
| FRI | Réduction probabiliste du degré revendiqué | Paramètres et nombre de requêtes déterminants |
| Vérificateur | Rejette une preuve incohérente | Ne garantit pas la disponibilité des données |
| Application NFT | Peut lier une preuve à un token et un sujet | Anti-rejeu, identité et révocation restent applicatifs |

La règle pratique est de documenter séparément ce qui est prouvé, ce qui est supposé et ce qui est décidé par l'application.
