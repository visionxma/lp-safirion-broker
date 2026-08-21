# -*- coding: utf-8 -*-
"""
Catalogo de traducoes da LP da Safirion.

Fonte: pt-BR (o index.html da raiz). Cada entrada mapeia a string em portugues
para en / es / fr. Strings ausentes daqui ficam como estao — e o caso de nomes
proprios (Safirion, Bitcoin, Tesla), codigos de ativos (EUR/USD) e dos enderecos
societarios, que nao se traduzem.

Formato numerico segue a convencao de cada idioma:
  pt/es/fr -> 0,12s  99,98%   |  en -> 0.12s  99.98%
  pt/es    -> 12.500 | fr -> 12 500 | en -> 12,500
"""

T = {
    # ------------------------------------------------- nomes de ativos
    # Tickers e marcas (EUR/USD, Bitcoin, Tesla, NVIDIA) ficam como estao;
    # so os nomes comuns se traduzem.
    'Ouro':     {'en': 'Gold',    'es': 'Oro',      'fr': 'Or'},
    'Petróleo': {'en': 'Oil',     'es': 'Petróleo', 'fr': 'Pétrole'},
    'Índices':  {'en': 'Indices', 'es': 'Índices',  'fr': 'Indices'},

    # ---------------------------------------------------------------- menu
    'Sobre':        {'en': 'About',       'es': 'Acerca de',   'fr': 'À propos'},
    'Velocidade':   {'en': 'Speed',       'es': 'Velocidad',   'fr': 'Vitesse'},
    'Plataforma':   {'en': 'Platform',    'es': 'Plataforma',  'fr': 'Plateforme'},
    'Ao vivo':      {'en': 'Live',        'es': 'En vivo',     'fr': 'En direct'},
    'Mercados':     {'en': 'Markets',     'es': 'Mercados',    'fr': 'Marchés'},
    'Comparativo':  {'en': 'Comparison',  'es': 'Comparativa', 'fr': 'Comparatif'},
    'Por que a Safirion': {
        'en': 'Why Safirion', 'es': 'Por qué Safirion', 'fr': 'Pourquoi Safirion'},
    'O que a Safirion faz diferente': {
        'en': "What Safirion does differently",
        'es': "Lo que Safirion hace diferente",
        'fr': "Ce que Safirion fait différemment"},
    'A Safirion foi construída para quem já perdeu entrada por travamento e saque por burocracia. Execução em 0,12s e spread fixo garantido por contrato — inclusive nos dias de maior volatilidade.': {
        'en': "Safirion was built for traders who have lost an entry to a frozen platform and a withdrawal to red tape. Execution in 0.12s and a fixed spread guaranteed by contract — even on the most volatile days.",
        'es': "Safirion fue construida para quien ya perdio una entrada por bloqueo y un retiro por burocracia. Ejecucion en 0,12s y spread fijo garantizado por contrato, incluso en los dias de mayor volatilidad.",
        'fr': "Safirion a ete construite pour ceux qui ont deja perdu une entree a cause d'un blocage et un retrait a cause de la paperasse. Execution en 0,12s et spread fixe garanti par contrat, meme les jours les plus volatils."},
    'Com tecnologia de última geração e uma operação totalmente automatizada, oferecemos um ambiente onde agilidade e proteção caminham juntas. Aqui, o usuário encontra suporte eficiente, interface simples de usar e transações realizadas com total transparência.': {
        'en': 'With cutting-edge technology and a fully automated operation, we offer an environment where speed and protection go hand in hand. Here you find efficient support, an interface that is simple to use and transactions carried out with complete transparency.',
        'es': 'Con tecnología de última generación y una operación totalmente automatizada, ofrecemos un entorno donde agilidad y protección caminan juntas. Aquí el usuario encuentra soporte eficiente, una interfaz simple de usar y transacciones realizadas con total transparencia.',
        'fr': "Avec une technologie de dernière génération et une opération entièrement automatisée, nous offrons un environnement où rapidité et protection avancent ensemble. L'utilisateur y trouve un support efficace, une interface simple à utiliser et des transactions réalisées en toute transparence."},
    'Sem limite diário de saque e sem pedido parado em análise: 100% das retiradas dos últimos seis meses saíram em menos de 24 horas.': {
        'en': "No daily withdrawal cap and no request stuck in review: 100% of withdrawals in the last six months cleared in under 24 hours.",
        'es': "Sin limite diario de retiro y sin solicitudes detenidas en revision: el 100% de los retiros de los ultimos seis meses salio en menos de 24 horas.",
        'fr': "Aucun plafond quotidien de retrait et aucune demande bloquee en revision : 100 % des retraits des six derniers mois ont ete traites en moins de 24 heures."},
    'Mais de 130 ativos entre Forex, ações, índices, commodities e cripto na mesma tela — você amplia a operação sem trocar de corretora.': {
        'en': "More than 130 assets across Forex, stocks, indices, commodities and crypto on one screen — you scale up without changing brokers.",
        'es': "Mas de 130 activos entre Forex, acciones, indices, materias primas y cripto en una sola pantalla: creces sin cambiar de broker.",
        'fr': "Plus de 130 actifs en Forex, actions, indices, matieres premieres et crypto sur un seul ecran : vous montez en puissance sans changer de courtier."},
    'Segurança':    {'en': 'Security',    'es': 'Seguridad',   'fr': 'Sécurité'},
    'Entrar':       {'en': 'Log in',      'es': 'Iniciar sesión', 'fr': 'Connexion'},
    'Comece Agora': {'en': 'Get Started', 'es': 'Empezar Ahora',  'fr': 'Commencer'},

    # ---------------------------------------------------------------- hero
    'Corretora global · Forex · Cripto · Ações': {
        'en': 'Global broker · Forex · Crypto · Stocks',
        'es': 'Bróker global · Forex · Cripto · Acciones',
        'fr': 'Courtier mondial · Forex · Crypto · Actions'},
    'Safirion Broker: o novo padrão global em experiência profissional de trading': {
        'en': 'Safirion Broker: the new global standard in professional trading',
        'es': 'Safirion Broker: el nuevo estándar global en experiencia profesional de trading',
        'fr': 'Safirion Broker : la nouvelle référence mondiale du trading professionnel'},
    'Opere com a corretora que já executou +17 milhões de ordens sem travamentos e garante seu saque em poucos minutos, sem burocracia e com a segurança que você precisa para proteger seu capital.': {
        'en': 'Trade with the broker that has already executed 17M+ orders without freezing and guarantees your withdrawal in minutes, with no red tape and the security you need to protect your capital.',
        'es': 'Opera con el bróker que ya ejecutó +17 millones de órdenes sin bloqueos y garantiza tu retiro en pocos minutos, sin burocracia y con la seguridad que necesitas para proteger tu capital.',
        'fr': "Tradez avec le courtier qui a déjà exécuté plus de 17 millions d'ordres sans blocage et garantit votre retrait en quelques minutes, sans paperasse et avec la sécurité nécessaire pour protéger votre capital."},
    'Abrir minha conta na Safirion': {
        'en': 'Open my Safirion account',
        'es': 'Abrir mi cuenta en Safirion',
        'fr': 'Ouvrir mon compte Safirion'},

    # ------------------------------------------------------ velocidade
    'Onde seu clique acontece exatamente quando deve acontecer': {
        'en': 'Where your click lands exactly when it should',
        'es': 'Donde tu clic ocurre exactamente cuando debe ocurrir',
        'fr': 'Où votre clic arrive exactement au bon moment'},
    'Nossa plataforma manteve 99,98% de uptime nos últimos 12 meses, mesmo durante os eventos de maior volatilidade do mercado.&nbsp;Tempo médio de resposta na execução de ordens: 70 ms, contra 240 ms das corretoras tradicionais — 3,4× mais rápida que a média do mercado.': {
        'en': 'Our platform held 99.98% uptime over the last 12 months, even through the market&rsquo;s most volatile events.&nbsp;Average order execution response time: 70 ms, against 240 ms at traditional brokers — 3.4× faster than the market average.',
        'es': 'Nuestra plataforma mantuvo un 99,98% de uptime en los últimos 12 meses, incluso durante los eventos de mayor volatilidad del mercado.&nbsp;Tiempo medio de respuesta en la ejecución de órdenes: 70 ms, frente a 240 ms de los brókers tradicionales — 3,4× más rápida que la media del mercado.',
        'fr': "Notre plateforme a maintenu 99,98 % de disponibilité sur les 12 derniers mois, y compris lors des épisodes les plus volatils du marché.&nbsp;Temps de réponse moyen à l'exécution des ordres : 70 ms, contre 240 ms chez les courtiers traditionnels — 3,4× plus rapide que la moyenne du marché."},
    'Velocidade e estabilidade': {
        'en': 'Speed and stability', 'es': 'Velocidad y estabilidad', 'fr': 'Vitesse et stabilité'},
    'A estrutura global que você precisa para operar com liberdade': {
        'en': 'The global infrastructure you need to trade freely',
        'es': 'La estructura global que necesitas para operar con libertad',
        'fr': "L'infrastructure mondiale dont vous avez besoin pour trader librement"},

    'Sem atrasos': {'en': 'No delays', 'es': 'Sin retrasos', 'fr': 'Sans latence'},
    'Clique e entre na taxa certa. Execução em 0,12s, sem slippage causado por fila — o preço que você viu na tela é o preço em que sua ordem entra.': {
        'en': 'Click and enter at the right rate. 0.12s execution, no queue-driven slippage — the price you saw on screen is the price your order gets.',
        'es': 'Haz clic y entra al precio correcto. Ejecución en 0,12s, sin slippage por cola — el precio que viste en pantalla es el precio al que entra tu orden.',
        'fr': "Cliquez et entrez au bon cours. Exécution en 0,12s, sans slippage dû à la file d'attente — le prix affiché est le prix auquel votre ordre passe."},

    'Spread fixo por contrato': {
        'en': 'Fixed spread by contract', 'es': 'Spread fijo por contrato', 'fr': 'Spread fixe par contrat'},
    'Nada de spread que aumenta no pior momento. O seu custo por operação é fixo e garantido por contrato, mesmo nos dias de maior volatilidade do mercado.': {
        'en': 'No spread widening at the worst possible moment. Your cost per trade is fixed and guaranteed by contract, even on the market&rsquo;s most volatile days.',
        'es': 'Nada de spreads que se amplían en el peor momento. Tu coste por operación es fijo y garantizado por contrato, incluso en los días de mayor volatilidad.',
        'fr': "Pas de spread qui s'élargit au pire moment. Votre coût par opération est fixe et garanti par contrat, même les jours les plus volatils."},

    '12.500 ordens por segundo': {
        'en': '12,500 orders per second', 'es': '12.500 órdenes por segundo', 'fr': '12 500 ordres par seconde'},
    'Capacidade de processamento sem degradação de performance. 99,98% de uptime nos últimos 12 meses, inclusive nos dias de crash do mercado.': {
        'en': 'Processing capacity with no performance degradation. 99.98% uptime over the last 12 months, including market crash days.',
        'es': 'Capacidad de procesamiento sin degradación del rendimiento. 99,98% de uptime en los últimos 12 meses, incluso en días de desplome del mercado.',
        'fr': 'Capacité de traitement sans dégradation des performances. 99,98 % de disponibilité sur les 12 derniers mois, y compris les jours de krach.'},

    'Saque em poucos minutos': {
        'en': 'Withdrawals in minutes', 'es': 'Retiro en pocos minutos', 'fr': 'Retrait en quelques minutes'},
    'Sem limite diário e sem burocracia. 100% dos saques dos últimos 6 meses saíram em menos de 24h, com suporte técnico disponível 24/7 pra acompanhar.': {
        'en': 'No daily cap and no red tape. 100% of withdrawals in the last 6 months cleared in under 24h, with technical support available 24/7 to follow up.',
        'es': 'Sin límite diario y sin burocracia. El 100% de los retiros de los últimos 6 meses salieron en menos de 24h, con soporte técnico disponible 24/7.',
        'fr': "Sans plafond quotidien ni paperasse. 100 % des retraits des 6 derniers mois ont été traités en moins de 24 h, avec un support technique disponible 24/7."},

    # ------------------------------------------------------ mercado ao vivo
    'Acompanhe o movimento real do mercado': {
        'en': 'Follow the market as it really moves',
        'es': 'Sigue el movimiento real del mercado',
        'fr': 'Suivez le marché en temps réel'},
    'Mais de 130 ativos em uma só tela, com execução em 0,12s e spread fixo — acompanhe cada ordem executada direto no seu celular, sem atraso entre o que você vê e o preço em que entra.': {
        'en': 'Over 130 assets on a single screen, with 0.12s execution and fixed spread — follow every filled order straight from your phone, with no gap between what you see and the price you get.',
        'es': 'Más de 130 activos en una sola pantalla, con ejecución en 0,12s y spread fijo — sigue cada orden ejecutada desde tu móvil, sin desfase entre lo que ves y el precio al que entras.',
        'fr': "Plus de 130 actifs sur un seul écran, avec une exécution en 0,12s et un spread fixe — suivez chaque ordre exécuté depuis votre mobile, sans décalage entre ce que vous voyez et le prix obtenu."},
    'Sem atraso entre o que você vê e o preço em que entra.': {
        'en': 'No gap between what you see and the price you get.',
        'es': 'Sin desfase entre lo que ves y el precio al que entras.',
        'fr': 'Aucun décalage entre ce que vous voyez et le prix obtenu.'},

    # ------------------------------------------------------------ mercados
    'Todos os mercados': {'en': 'All markets', 'es': 'Todos los mercados', 'fr': 'Tous les marchés'},
    'Opere em todos os': {'en': 'Trade every', 'es': 'Opera en todos los', 'fr': 'Tradez sur tous les'},
    'mercados': {'en': 'global', 'es': 'mercados', 'fr': 'marchés'},
    'globais': {'en': 'market', 'es': 'globales', 'fr': 'mondiaux'},
    'Forex, ações, índices, commodities e criptomoedas em uma única plataforma. Abra posições de compra ou venda em mercados globais, com spread fixo garantido por contrato e execução em 0,12s.': {
        'en': 'Forex, stocks, indices, commodities and crypto on a single platform. Open buy or sell positions across global markets, with a fixed spread guaranteed by contract and 0.12s execution.',
        'es': 'Forex, acciones, índices, materias primas y criptomonedas en una única plataforma. Abre posiciones de compra o venta en mercados globales, con spread fijo garantizado por contrato y ejecución en 0,12s.',
        'fr': "Forex, actions, indices, matières premières et cryptomonnaies sur une seule plateforme. Ouvrez des positions à l'achat ou à la vente sur les marchés mondiaux, avec un spread fixe garanti par contrat et une exécution en 0,12s."},
    'Spread a partir de 0,1 pip em Forex': {
        'en': 'Spread from 0.1 pip on Forex', 'es': 'Spread desde 0,1 pip en Forex', 'fr': 'Spread dès 0,1 pip sur le Forex'},
    'Comissão zero em +3.000 ações globais': {
        'en': 'Zero commission on 3,000+ global stocks',
        'es': 'Comisión cero en +3.000 acciones globales',
        'fr': 'Zéro commission sur plus de 3 000 actions mondiales'},
    'Alavancagem de até 1:500 em commodities': {
        'en': 'Leverage up to 1:500 on commodities',
        'es': 'Apalancamiento de hasta 1:500 en materias primas',
        'fr': "Effet de levier jusqu'à 1:500 sur les matières premières"},
    '+80 pares · spread a partir de 0,1 pip': {
        'en': '80+ pairs · spread from 0.1 pip',
        'es': '+80 pares · spread desde 0,1 pip',
        'fr': '+80 paires · spread dès 0,1 pip'},
    # o selo "Disponivel" virou CTA; a traducao antiga fica para o caso de voltar
    'Disponível': {'en': 'Available', 'es': 'Disponible', 'fr': 'Disponible'},
    'Operar agora': {'en': 'Trade now', 'es': 'Operar ahora', 'fr': 'Trader maintenant'},
    'Ações globais': {'en': 'Global stocks', 'es': 'Acciones globales', 'fr': 'Actions mondiales'},
    '+3.000 ações · comissão zero': {
        'en': '3,000+ stocks · zero commission',
        'es': '+3.000 acciones · comisión cero',
        'fr': '+3 000 actions · zéro commission'},
    'Criptomoedas': {'en': 'Cryptocurrencies', 'es': 'Criptomonedas', 'fr': 'Cryptomonnaies'},
    '50 criptos · operação 24/7': {
        'en': '50 cryptos · trading 24/7', 'es': '50 criptos · operación 24/7', 'fr': '50 cryptos · trading 24/7'},
    '+130 ativos entre Forex, ações, índices, commodities e cripto': {
        'en': '130+ assets across Forex, stocks, indices, commodities and crypto',
        'es': '+130 activos entre Forex, acciones, índices, materias primas y cripto',
        'fr': '+130 actifs entre Forex, actions, indices, matières premières et crypto'},
    'Forex': {'en': 'Forex', 'es': 'Forex', 'fr': 'Forex'},

    # --------------------------------------------------------- comparativo
    'A Safirion': {'en': 'Safirion', 'es': 'Safirion', 'fr': 'Safirion'},
    'redefine': {'en': 'redefines', 'es': 'redefine', 'fr': 'redéfinit'},
    'o padrão das corretoras': {
        'en': 'the broker standard', 'es': 'el estándar de los brókers', 'fr': 'la norme des courtiers'},
    'Quase todo trader que chega aqui já perdeu dinheiro com saque travado ou clique fora da hora. Veja a diferença lado a lado.': {
        'en': 'Almost every trader who arrives here has already lost money to a stuck withdrawal or a mistimed click. See the difference side by side.',
        'es': 'Casi todo trader que llega aquí ya perdió dinero por un retiro bloqueado o un clic a destiempo. Mira la diferencia lado a lado.',
        'fr': "Presque tous les traders qui arrivent ici ont déjà perdu de l'argent à cause d'un retrait bloqué ou d'un clic hors délai. Voyez la différence côte à côte."},
    'Sem perder entrada por travamento': {
        'en': 'No missed entries from freezing', 'es': 'Sin perder entradas por bloqueos', 'fr': "Plus d'entrée manquée pour cause de blocage"},
    'Sem plataforma fora do ar no pior momento': {
        'en': 'No platform outage at the worst moment', 'es': 'Sin plataforma caída en el peor momento', 'fr': 'Plus de plateforme hors service au pire moment'},
    'Sem pedido de saque travado por burocracia': {
        'en': 'No withdrawal request stuck in red tape', 'es': 'Sin solicitudes de retiro trabadas por burocracia', 'fr': 'Plus de demande de retrait bloquée par la paperasse'},
    'Sem custo surpresa em dia de volatilidade': {
        'en': 'No surprise cost on a volatile day', 'es': 'Sin costes sorpresa en días de volatilidad', 'fr': 'Plus de coût surprise les jours de volatilité'},
    'Abrir minha conta': {'en': 'Open my account', 'es': 'Abrir mi cuenta', 'fr': 'Ouvrir mon compte'},
    'Corretoras comuns': {'en': 'Ordinary brokers', 'es': 'Brókers comunes', 'fr': 'Courtiers ordinaires'},
    'Execução média de 0,45s': {
        'en': 'Average execution of 0.45s', 'es': 'Ejecución media de 0,45s', 'fr': 'Exécution moyenne de 0,45s'},
    'Execução ultrarrápida de': {
        'en': 'Ultra-fast execution of', 'es': 'Ejecución ultrarrápida de', 'fr': 'Exécution ultra-rapide de'},
    '92% de uptime em dias de alta volatilidade': {
        'en': '92% uptime on high-volatility days', 'es': '92% de uptime en días de alta volatilidad', 'fr': '92 % de disponibilité les jours de forte volatilité'},
    '99,98% de uptime': {'en': '99.98% uptime', 'es': '99,98% de uptime', 'fr': '99,98 % de disponibilité'},
    'mesmo em dias de crash': {
        'en': 'even on crash days', 'es': 'incluso en días de desplome', 'fr': 'même les jours de krach'},
    'Limite de saques de $5.000/dia': {
        'en': 'Withdrawal cap of $5,000/day', 'es': 'Límite de retiros de $5.000/día', 'fr': 'Plafond de retrait de 5 000 $/jour'},
    'Saques ilimitados': {'en': 'Unlimited withdrawals', 'es': 'Retiros ilimitados', 'fr': 'Retraits illimités'},
    'em poucos minutos, sem burocracia': {
        'en': 'in minutes, with no red tape', 'es': 'en pocos minutos, sin burocracia', 'fr': 'en quelques minutes, sans paperasse'},
    'Spread variável que aumenta em momentos críticos': {
        'en': 'Variable spread that widens at critical moments', 'es': 'Spread variable que se amplía en momentos críticos', 'fr': "Spread variable qui s'élargit aux moments critiques"},
    'Spread fixo': {'en': 'Fixed spread', 'es': 'Spread fijo', 'fr': 'Spread fixe'},
    'garantido por contrato': {'en': 'guaranteed by contract', 'es': 'garantizado por contrato', 'fr': 'garanti par contrat'},
    'Suporte por e-mail que responde em 48h': {
        'en': 'Email support that replies in 48h', 'es': 'Soporte por e-mail que responde en 48h', 'fr': 'Support e-mail qui répond sous 48 h'},
    'Suporte 24/7': {'en': '24/7 support', 'es': 'Soporte 24/7', 'fr': 'Support 24/7'},
    'via chat, telefone e e-mail': {
        'en': 'via chat, phone and email', 'es': 'vía chat, teléfono y e-mail', 'fr': 'par chat, téléphone et e-mail'},

    # ----------------------------------------------------------- seguranca
    'é prioridade absoluta': {
        'en': 'is the absolute priority', 'es': 'es prioridad absoluta', 'fr': 'est une priorité absolue'},
    'Regulamentação internacional': {
        'en': 'International regulation', 'es': 'Regulación internacional', 'fr': 'Régulation internationale'},
    'SSL 256 bits': {'en': '256-bit SSL', 'es': 'SSL de 256 bits', 'fr': 'SSL 256 bits'},
    'Criptografia de nível bancário': {
        'en': 'Bank-grade encryption', 'es': 'Cifrado de nivel bancario', 'fr': 'Chiffrement de niveau bancaire'},
    'Contas segregadas': {'en': 'Segregated accounts', 'es': 'Cuentas segregadas', 'fr': 'Comptes ségrégués'},
    'Bancos de primeiro nível': {
        'en': 'Tier-one banks', 'es': 'Bancos de primer nivel', 'fr': 'Banques de premier rang'},
    'Auditoria trimestral': {'en': 'Quarterly audit', 'es': 'Auditoría trimestral', 'fr': 'Audit trimestriel'},
    'Verificação externa independente': {
        'en': 'Independent external verification', 'es': 'Verificación externa independiente', 'fr': 'Vérification externe indépendante'},

    # ----------------------------------------------------------------- FAQ
    'Perguntas frequentes sobre a Safirion': {
        'en': 'Frequently asked questions about Safirion',
        'es': 'Preguntas frecuentes sobre Safirion',
        'fr': 'Questions fréquentes sur Safirion'},
    'Tire suas dúvidas antes de abrir a conta.': {
        'en': 'Clear your doubts before opening an account.',
        'es': 'Resuelve tus dudas antes de abrir la cuenta.',
        'fr': "Levez vos doutes avant d'ouvrir un compte."},
    'Qual o saque e depósito mínimo?': {
        'en': 'What is the minimum deposit and withdrawal?',
        'es': '¿Cuál es el retiro y depósito mínimo?',
        'fr': 'Quel est le dépôt et le retrait minimum ?'},
    'Posso tirar dinheiro quando eu quiser?': {
        'en': 'Can I withdraw money whenever I want?',
        'es': '¿Puedo retirar dinero cuando quiera?',
        'fr': "Puis-je retirer de l'argent quand je veux ?"},
    'Posso operar pelo celular?': {
        'en': 'Can I trade from my phone?',
        'es': '¿Puedo operar desde el móvil?',
        'fr': 'Puis-je trader depuis mon mobile ?'},
    'Como abrir um chamado de suporte?': {
        'en': 'How do I open a support ticket?',
        'es': '¿Cómo abrir un ticket de soporte?',
        'fr': "Comment ouvrir un ticket d'assistance ?"},

    # ------------------------------------------------- como se cadastrar
    'Como se cadastrar': {
        'en': 'How to sign up', 'es': 'Cómo registrarse', 'fr': "Comment s'inscrire"},
    'Como se cadastrar na': {
        'en': 'How to sign up with', 'es': 'Cómo registrarse en',
        'fr': "Comment s'inscrire sur"},
    'Abrir conta na Safirion leva cerca de dois minutos e pede seis campos.': {
        'en': "Opening a Safirion account takes about two minutes and asks for six fields.",
        'es': "Abrir una cuenta en Safirion toma unos dos minutos y pide seis campos.",
        'fr': "Ouvrir un compte Safirion prend environ deux minutes et demande six champs."},
    'A verificação de documentos vem depois e não bloqueia o primeiro acesso à plataforma.': {
        'en': "Document verification comes later and does not block your first access to the platform.",
        'es': "La verificacion de documentos viene despues y no bloquea el primer acceso a la plataforma.",
        'fr': "La verification des documents vient ensuite et ne bloque pas le premier acces a la plateforme."},
    'O que a Safirion pede no cadastro': {
        'en': "What Safirion asks for at sign-up",
        'es': "Lo que Safirion pide en el registro",
        'fr': "Ce que Safirion demande a l'inscription"},
    'Acesse a página de cadastro da Safirion Broker': {
        'en': 'Go to the Safirion Broker sign-up page',
        'es': 'Accede a la página de registro de Safirion Broker',
        'fr': "Accédez à la page d'inscription de Safirion Broker"},
    # cita o rotulo exato do botao, que vem do catalogo logo acima
    'Clique em “Abrir minha conta na Safirion”;': {
        'en': 'Click “Open my Safirion account”;',
        'es': 'Haz clic en “Abrir mi cuenta en Safirion”;',
        'fr': 'Cliquez sur « Ouvrir mon compte Safirion » ;'},
    'Informe nome, sobrenome e país de residência;': {
        'en': "Enter your first name, last name and country of residence;",
        'es': "Indica nombre, apellido y pais de residencia;",
        'fr': "Indiquez prenom, nom et pays de residence ;"},
    'Defina a senha e confirme os Termos e Condições;': {
        'en': "Set your password and confirm the Terms and Conditions;",
        'es': "Define la contrasena y confirma los Terminos y Condiciones;",
        'fr': "Definissez le mot de passe et confirmez les Conditions Generales ;"},
    'Valide o e-mail que a Safirion enviar;': {
        'en': "Validate the email Safirion sends you;",
        'es': "Valida el correo que Safirion te envie;",
        'fr': "Validez l'e-mail envoye par Safirion ;"},
    'Entre na conta e conheça a plataforma.': {
        'en': "Log in and get to know the platform.",
        'es': "Inicia sesion y conoce la plataforma.",
        'fr': "Connectez-vous et decouvrez la plateforme."},
    'Feito — a conta está ativa.': {
        'en': "Done — your account is live.",
        'es': "Listo: la cuenta esta activa.",
        'fr': "Termine : le compte est actif."},
    'A partir daí você opera Forex, ações, índices, commodities e cripto na mesma plataforma.': {
        'en': "From there you trade Forex, stocks, indices, commodities and crypto on the same platform.",
        'es': "A partir de ahi operas Forex, acciones, indices, materias primas y cripto en la misma plataforma.",
        'fr': "A partir de la, vous tradez Forex, actions, indices, matieres premieres et crypto sur la meme plateforme."},
    # -------------------------------------------------------------- rodape
    'Safirion é a plataforma de trading profissional que combina velocidade,\n      segurança e tecnologia de ponta.': {
        'en': 'Safirion is the professional trading platform that combines speed,\n      security and cutting-edge technology.',
        'es': 'Safirion es la plataforma de trading profesional que combina velocidad,\n      seguridad y tecnología de punta.',
        'fr': "Safirion est la plateforme de trading professionnelle qui allie rapidité,\n      sécurité et technologie de pointe."},
    'Navegação': {'en': 'Navigation', 'es': 'Navegación', 'fr': 'Navigation'},
    'Início': {'en': 'Home', 'es': 'Inicio', 'fr': 'Accueil'},
    'Suporte': {'en': 'Support', 'es': 'Soporte', 'fr': 'Support'},
    'Afiliados': {'en': 'Affiliates', 'es': 'Afiliados', 'fr': 'Affiliés'},
    'Criar conta de afiliado': {
        'en': 'Create affiliate account', 'es': 'Crear cuenta de afiliado', 'fr': 'Créer un compte affilié'},
    'Login de afiliado': {'en': 'Affiliate login', 'es': 'Acceso de afiliado', 'fr': 'Connexion affilié'},
    'Legal': {'en': 'Legal', 'es': 'Legal', 'fr': 'Mentions légales'},
    'Termos e Condições': {
        'en': 'Terms and Conditions', 'es': 'Términos y Condiciones', 'fr': 'Conditions générales'},
    'Política AML e KYC': {
        'en': 'AML and KYC Policy', 'es': 'Política AML y KYC', 'fr': 'Politique LBC et KYC'},
    'Taxas Gerais': {'en': 'General Fees', 'es': 'Tarifas Generales', 'fr': 'Frais généraux'},
    'Política de Execução': {
        'en': 'Order Execution Policy', 'es': 'Política de Ejecución', 'fr': "Politique d'exécution"},
    'Política de Pagamento': {
        'en': 'Payment Policy', 'es': 'Política de Pago', 'fr': 'Politique de paiement'},
    'Política de Cookies': {
        'en': 'Cookies Policy', 'es': 'Política de Cookies', 'fr': 'Politique de cookies'},
    'Contas Demo': {'en': 'Demo Accounts', 'es': 'Cuentas Demo', 'fr': 'Comptes démo'},
    'Divulgação de Risco': {
        'en': 'Risk Disclosure', 'es': 'Divulgación de Riesgo', 'fr': 'Avertissement sur les risques'},
    'Política de Saque': {
        'en': 'Withdrawal Policy', 'es': 'Política de Retiro', 'fr': 'Politique de retrait'},
    'Margin Trading': {
        'en': 'Margin Trading', 'es': 'Trading con Margen', 'fr': 'Trading sur marge'},
    '© 2026 Safirion. Todos os direitos reservados.': {
        'en': '© 2026 Safirion. All rights reserved.',
        'es': '© 2026 Safirion. Todos los derechos reservados.',
        'fr': '© 2026 Safirion. Tous droits réservés.'},
}

# ---------------------------------------------------------------------------
# Respostas do FAQ (objeto ANS do kv-faq-js e o FAQPage do JSON-LD)
# ---------------------------------------------------------------------------
FAQ = {
    'Quanto preciso para depositar e para sacar?': {
        'pt': "Os valores mínimos mudam conforme o método de pagamento. O valor exato aparece na própria área de depósito, antes de você confirmar a operação.",
        'en': "The minimums depend on the payment method. The exact figure appears in the deposit area itself, before you confirm.",
        'es': "Los minimos dependen del metodo de pago. El importe exacto aparece en la propia area de deposito, antes de confirmar.",
        'fr': "Les montants minimum dependent du moyen de paiement. Le montant exact s'affiche dans l'espace de depot, avant confirmation."},
    'Existe carência ou limite para sacar?': {
        'pt': "Não há carência nem limite diário. O pedido pode ser aberto a qualquer momento dentro da plataforma.",
        'en': "There is no lock-up and no daily cap. You can open a request at any time inside the platform.",
        'es': "No hay periodo de espera ni limite diario. La solicitud puede abrirse en cualquier momento dentro de la plataforma.",
        'fr': "Il n'y a ni delai de blocage ni plafond quotidien. La demande peut etre ouverte a tout moment depuis la plateforme."},
    'A plataforma funciona no celular?': {
        'pt': "Sim. A mesma conta abre no navegador do celular e também no aplicativo.",
        'en': "Yes. The same account opens in your mobile browser and in the app.",
        'es': "Si. La misma cuenta abre en el navegador del movil y tambien en la aplicacion.",
        'fr': "Oui. Le meme compte s'ouvre dans le navigateur mobile et dans l'application."},
    'Como falo com o suporte?': {
        'pt': "Pelo menu de suporte dentro do painel. O atendimento responde por chat, telefone e e-mail.",
        'en': "Through the support menu inside the dashboard. The team answers by chat, phone and email.",
        'es': "Por el menu de soporte dentro del panel. El equipo responde por chat, telefono y correo.",
        'fr': "Par le menu support dans le tableau de bord. L'equipe repond par chat, telephone et e-mail."},
}

# ---------------------------------------------------------------------------
# Meta tags e textos do grafo JSON-LD
# ---------------------------------------------------------------------------
META = {
    'title': {
        'pt': 'Safirion Broker — Corretora de Forex, Cripto e Ações | Saque em Minutos',
        'en': 'Safirion Broker — Forex, Crypto and Stock Broker | Withdrawals in Minutes',
        'es': 'Safirion Broker — Bróker de Forex, Cripto y Acciones | Retiros en Minutos',
        'fr': 'Safirion Broker — Courtier Forex, Crypto et Actions | Retraits en Minutes'},
    'description': {
        'pt': 'Opere Forex, criptomoedas e ações em uma corretora com regulamentação internacional em Seychelles. Execução ultrarrápida, saques processados em poucos minutos e suporte 24/7. Abra sua conta em 2 minutos.',
        'en': 'Trade Forex, crypto and stocks with a broker under international regulation in Seychelles. Ultra-fast execution, withdrawals processed in minutes and 24/7 support. Open your account in 2 minutes.',
        'es': 'Opera Forex, criptomonedas y acciones en un bróker con regulación internacional en Seychelles. Ejecución ultrarrápida, retiros procesados en pocos minutos y soporte 24/7. Abre tu cuenta en 2 minutos.',
        'fr': "Tradez le Forex, les cryptomonnaies et les actions chez un courtier sous régulation internationale aux Seychelles. Exécution ultra-rapide, retraits traités en quelques minutes et support 24/7. Ouvrez votre compte en 2 minutes."},
    'og_title': {
        'pt': 'Safirion Broker — Corretora de Forex, Cripto e Ações | Saque em Minutos',
        'en': 'Safirion Broker — Forex, Crypto and Stock Broker | Withdrawals in Minutes',
        'es': 'Safirion Broker — Bróker de Forex, Cripto y Acciones | Retiros en Minutos',
        'fr': 'Safirion Broker — Courtier Forex, Crypto et Actions | Retraits en Minutes'},
    'twitter_title': {
        'pt': 'Safirion Broker — Corretora de Forex, Cripto e Ações',
        'en': 'Safirion Broker — Forex, Crypto and Stock Broker',
        'es': 'Safirion Broker — Bróker de Forex, Cripto y Acciones',
        'fr': 'Safirion Broker — Courtier Forex, Crypto et Actions'},
    'keywords': {
        'pt': 'safirion, safirion broker, corretora forex, corretora de criptomoedas, plataforma de trading, spread fixo, saque rápido, corretora regulamentada, day trade, o que é a safirion',
        'en': 'safirion, safirion broker, forex broker, crypto broker, trading platform, fixed spread, fast withdrawal, regulated broker, day trading, what is safirion',
        'es': 'safirion, safirion broker, bróker forex, bróker de criptomonedas, plataforma de trading, spread fijo, retiro rápido, bróker regulado, day trading, qué es safirion',
        'fr': 'safirion, safirion broker, courtier forex, courtier crypto, plateforme de trading, spread fixe, retrait rapide, courtier régulé, day trading, quest-ce que safirion'},
    'lang_attr': {'pt': 'pt-BR', 'en': 'en', 'es': 'es', 'fr': 'fr'},
    'og_locale': {'pt': 'pt_BR', 'en': 'en_US', 'es': 'es_ES', 'fr': 'fr_FR'},
}

# ---------------------------------------------------------------------------
# Textos de atributo (alt das imagens) — nao ficam entre > <, entao precisam
# de uma passada propria no gerador.
# ---------------------------------------------------------------------------
ATRIBUTOS = {
    'Painel de operações da Safirion — EUR/USD em tempo real': {
        'en': 'Safirion trading panel — EUR/USD in real time',
        'es': 'Panel de operaciones de Safirion — EUR/USD en tiempo real',
        'fr': 'Panneau de trading Safirion — EUR/USD en temps réel'},
    'Planeta Terra visto do espaco': {
        'en': 'Planet Earth seen from space',
        'es': 'Planeta Tierra visto desde el espacio',
        'fr': 'La Terre vue de l\'espace'},
    'Mapa-mundi indicando alcance global da Safirion': {
        'en': 'World map showing Safirion global reach',
        'es': 'Mapamundi que muestra el alcance global de Safirion',
        'fr': 'Carte du monde illustrant la portée mondiale de Safirion'},
}

IDIOMAS = ['en', 'es', 'fr']
NOMES = {'pt': 'Português', 'en': 'English', 'es': 'Español', 'fr': 'Français'}
CURTO = {'pt': 'PT', 'en': 'EN', 'es': 'ES', 'fr': 'FR'}
# /pt/ e nao / porque o safirion.com ja tem essa URL indexada; trocar
# para a raiz criaria um 404 na pagina que ja tem historico.
CAMINHO = {'pt': '/pt/', 'en': '/en/', 'es': '/es/', 'fr': '/fr/'}
