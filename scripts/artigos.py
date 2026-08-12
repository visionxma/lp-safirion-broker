# -*- coding: utf-8 -*-
"""
Conteudo do blog.

Cada artigo mira um termo de cauda longa — busca com menos volume, mas com
intencao clara e concorrencia menor, que e onde um dominio novo tem chance real
de aparecer. O texto e informativo primeiro: quem chega procurando entender
spread nao quer um anuncio.

Financas e YMYL para o Google: os artigos evitam promessa de retorno, citam a
fonte de cada numero da Safirion e fecham com aviso de risco.
"""

AVISO = (
    'Operar produtos alavancados envolve risco significativo de perda e pode não ser '
    'adequado a todos os investidores. Rentabilidade passada não é garantia de resultado '
    'futuro. Opere apenas com capital que você pode se permitir perder.'
)

ARTIGOS = [
    # ------------------------------------------------------------------ 1
    {
        'slug': 'como-funciona-saque-corretora',
        'titulo': 'Como funciona o saque em uma corretora (e o que costuma travar o seu)',
        'resumo': 'Prazos, taxas, limites e os quatro motivos reais pelos quais um pedido de '
                  'saque fica parado. Como avaliar a política de retirada antes de depositar.',
        'seo_titulo': 'Como funciona o saque em corretora: prazos, taxas e o que trava',
        'seo_desc': 'Entenda o processo de saque em corretoras: prazos reais, taxas, limites '
                    'diários e os quatro motivos que mais travam um pedido. Como avaliar a '
                    'política antes de depositar.',
        'data': '2026-08-12',
        'minutos': 7,
        'tag': 'Operação',
        'corpo': [
            ('p', 'Saque travado é a reclamação número um contra corretoras. E quase sempre o '
                  'problema não aparece na hora de sacar — ele foi criado lá atrás, no momento '
                  'do cadastro, quando ninguém leu a política de retirada.'),
            ('h2', 'O caminho que o dinheiro percorre'),
            ('p', 'Quando você solicita um saque, o pedido passa por três etapas. Primeiro a '
                  'validação interna: a corretora confere se a conta está verificada, se não há '
                  'posições abertas travando margem e se o valor respeita o mínimo. Depois vem a '
                  'aprovação, que pode ser automática ou manual. Só então o dinheiro entra na '
                  'fila do provedor de pagamento — banco, carteira eletrônica ou rede blockchain.'),
            ('p', 'O prazo que a corretora anuncia normalmente cobre só a segunda etapa. O tempo '
                  'do provedor é separado, e é ele que costuma dominar a espera em transferências '
                  'bancárias internacionais.'),
            ('h2', 'Os quatro motivos que mais travam um saque'),
            ('h3', '1. Verificação incompleta'),
            ('p', 'A regulamentação de prevenção à lavagem de dinheiro (AML) e conheça seu '
                  'cliente (KYC) obriga a corretora a confirmar identidade e endereço antes de '
                  'liberar retirada. Se você depositou sem concluir a verificação, o dinheiro '
                  'entra — mas não sai. Resolva isso no primeiro dia, não no dia do saque.'),
            ('h3', '2. Método diferente do depósito'),
            ('p', 'A maioria das corretoras exige que o saque volte pelo mesmo caminho do '
                  'depósito, até o valor depositado. É regra antifraude, não má vontade. Se você '
                  'depositou por cartão, espere que a devolução vá para o cartão.'),
            ('h3', '3. Margem presa em posição aberta'),
            ('p', 'O saldo que aparece na tela nem sempre é o saldo disponível. Posições abertas '
                  'reservam margem, e o valor livre para saque é o que sobra. Confira o campo de '
                  'margem livre antes de pedir.'),
            ('h3', '4. Limite diário'),
            ('p', 'Muitas corretoras aplicam teto por dia — algo em torno de US$ 5.000 é comum. '
                  'Quem opera volume alto descobre isso no pior momento. Vale verificar se existe '
                  'limite e qual é antes de escolher onde deixar seu capital.'),
            ('h2', 'O que perguntar antes de depositar'),
            ('ul', [
                'Qual o valor mínimo de saque, por método?',
                'Existe limite diário ou mensal?',
                'A corretora cobra taxa própria, além da taxa do provedor?',
                'Qual o prazo médio real — e onde ele está publicado?',
                'A verificação precisa estar concluída antes do primeiro depósito?',
            ]),
            ('h2', 'Como é na Safirion'),
            ('p', 'Na Safirion o saque mínimo é de US$ 2 por carteira eletrônica e US$ 25 para '
                  'outros métodos de transferência, sem limite diário. Segundo os dados da '
                  'corretora, 100% dos saques dos últimos 6 meses foram processados em menos de '
                  '24 horas. As condições completas estão na Política de Saque, publicada no '
                  'rodapé do site.'),
            ('cta', 'Ver a política de saque da Safirion'),
        ],
    },

    # ------------------------------------------------------------------ 2
    {
        'slug': 'o-que-e-spread-fixo',
        'titulo': 'O que é spread fixo e por que ele muda o seu resultado',
        'resumo': 'A diferença entre spread fixo e variável, quanto cada um custa na prática e '
                  'por que a conta muda justamente nos dias em que você mais opera.',
        'seo_titulo': 'O que é spread fixo: diferença para o variável e quanto custa',
        'seo_desc': 'Spread fixo ou variável? Entenda como cada modelo é cobrado, quanto pesa no '
                    'custo por operação e por que o variável encarece exatamente nos momentos de '
                    'maior volatilidade.',
        'data': '2026-08-12',
        'minutos': 6,
        'tag': 'Custos',
        'corpo': [
            ('p', 'Spread é a diferença entre o preço de compra e o de venda de um ativo. É o '
                  'custo que você paga para entrar em uma operação — e, em muitas corretoras, é '
                  'a principal fonte de receita delas.'),
            ('h2', 'Como o spread aparece na tela'),
            ('p', 'Todo ativo tem dois preços simultâneos. O <em>bid</em> é quanto o mercado paga '
                  'para comprar de você; o <em>ask</em> é quanto cobra para vender a você. Se o '
                  'EUR/USD mostra bid 1,14646 e ask 1,14647, o spread é de 0,00001 — um pip.'),
            ('p', 'Na prática isso significa que, no instante em que você abre uma posição, ela '
                  'já nasce no negativo pelo valor do spread. O preço precisa andar a seu favor '
                  'esse tanto só para você empatar.'),
            ('h2', 'Fixo contra variável'),
            ('p', 'No <strong>spread variável</strong>, o valor acompanha a liquidez do mercado. '
                  'Em horário calmo ele pode ficar baixo, o que parece ótimo. O problema é o '
                  'outro lado: em notícia de impacto, abertura de mercado ou evento de '
                  'volatilidade, ele abre. Um par que custava 0,8 pip pode ir a 4 ou 5 pips em '
                  'segundos.'),
            ('p', 'No <strong>spread fixo</strong>, o valor é definido em contrato e não muda com '
                  'a condição do mercado. Em dia calmo você às vezes paga um pouco mais que '
                  'pagaria no variável. Em dia de volatilidade, paga muito menos.'),
            ('h2', 'Por que a diferença aparece justamente quando importa'),
            ('p', 'A armadilha do spread variável é estatística. Os momentos de maior volatilidade '
                  'são exatamente os que atraem mais operações — divulgação de dados econômicos, '
                  'decisão de juros, abertura de sessão. É quando o volume de trades concentra e '
                  'é quando o spread variável está no pico.'),
            ('p', 'Ou seja: você paga o spread barato nas horas em que opera pouco e o spread '
                  'caro nas horas em que opera muito. A média ponderada do custo real fica bem '
                  'acima da média simples anunciada.'),
            ('h2', 'Fazendo a conta'),
            ('p', 'Em um lote padrão de EUR/USD, cada pip vale cerca de US$ 10. A diferença entre '
                  'um spread de 1 pip e um de 4 pips é de US$ 30 por operação. Para quem faz 10 '
                  'operações por dia, são US$ 300 diários — US$ 6.000 em um mês de 20 pregões.'),
            ('p', 'O custo do spread não aparece como taxa na fatura. Ele é descontado do '
                  'resultado, o que o torna fácil de ignorar e caro de carregar.'),
            ('h2', 'O que verificar na sua corretora'),
            ('ul', [
                'O spread anunciado é fixo ou é uma média?',
                'Se é fixo, está garantido por contrato ou é "tipicamente"?',
                'Existe alargamento em horários específicos, como a virada do dia?',
                'Há comissão cobrada por fora, além do spread?',
            ]),
            ('h2', 'Como é na Safirion'),
            ('p', 'A Safirion trabalha com spread fixo garantido por contrato, a partir de 0,1 '
                  'pip em Forex, sem alargamento em momentos de volatilidade. As condições por '
                  'ativo estão no documento de Taxas Gerais, no rodapé do site.'),
            ('cta', 'Ver as taxas da Safirion'),
        ],
    },

    # ------------------------------------------------------------------ 3
    {
        'slug': 'corretora-regulamentada-seychelles',
        'titulo': 'Corretora regulamentada em Seychelles é segura? O que a licença cobre',
        'resumo': 'O que significa a regulamentação em Seychelles, qual proteção ela oferece de '
                  'fato e quais sinais verificar além da licença.',
        'seo_titulo': 'Corretora regulamentada em Seychelles é segura? O que verificar',
        'seo_desc': 'O que a licença de Seychelles cobre, qual proteção oferece ao seu capital e '
                    'quais sinais checar além do registro: contas segregadas, saldo negativo e '
                    'auditoria externa.',
        'data': '2026-08-12',
        'minutos': 7,
        'tag': 'Segurança',
        'corpo': [
            ('p', 'Seychelles aparece no rodapé de muitas corretoras que atendem o Brasil, e a '
                  'pergunta é sempre a mesma: isso protege meu dinheiro? A resposta honesta é '
                  '"em parte, e depende do que mais a corretora oferece".'),
            ('h2', 'O que é a regulamentação de Seychelles'),
            ('p', 'A autoridade financeira de Seychelles licencia corretoras que operam '
                  'internacionalmente. Para manter a licença, a empresa precisa cumprir '
                  'requisitos de capital mínimo, apresentar demonstrações auditadas, seguir '
                  'regras de prevenção à lavagem de dinheiro e manter o dinheiro dos clientes '
                  'separado do caixa da própria empresa.'),
            ('p', 'É um regime real, com obrigações verificáveis. Mas é mais leve que o de '
                  'jurisdições como Reino Unido ou Austrália, e isso é o principal ponto a '
                  'entender.'),
            ('h2', 'O que a licença cobre — e o que não cobre'),
            ('p', 'A licença <strong>cobre</strong>: exigência de contas segregadas, auditoria '
                  'periódica, obrigação de identificar clientes e um canal formal para reclamação.'),
            ('p', 'A licença <strong>não cobre</strong>: fundo de compensação em caso de falência '
                  'da corretora, como existe no Reino Unido. Se a empresa quebrar, a recuperação '
                  'depende da segregação ter sido cumprida e do processo judicial local.'),
            ('h2', 'Os quatro sinais que valem mais que a licença'),
            ('h3', 'Contas segregadas'),
            ('p', 'O dinheiro do cliente fica em conta separada, em banco de primeiro nível, sem '
                  'se misturar ao caixa operacional da corretora. É a proteção mais concreta que '
                  'existe: se a empresa tem problema financeiro, o seu capital não faz parte da '
                  'massa.'),
            ('h3', 'Proteção contra saldo negativo'),
            ('p', 'Em movimento violento, uma posição alavancada pode fechar abaixo de zero — e '
                  'sem essa proteção você fica devendo à corretora. Com ela, sua perda máxima é o '
                  'que você depositou.'),
            ('h3', 'Auditoria externa'),
            ('p', 'Verificação por auditor independente, em periodicidade definida. É o que '
                  'transforma a promessa de segregação em fato conferível por terceiro.'),
            ('h3', 'Documentação pública'),
            ('p', 'Termos, política de execução, política de saque e divulgação de risco '
                  'publicados e acessíveis. Corretora que esconde o contrato está dizendo algo '
                  'sobre o contrato.'),
            ('h2', 'Como verificar por conta própria'),
            ('ul', [
                'Procure o número de registro no rodapé e confirme na autoridade licenciadora.',
                'Confira se a razão social do registro é a mesma que aparece no contrato.',
                'Leia a divulgação de risco: ela deve falar de perda, não de ganho.',
                'Teste o suporte antes de depositar valor relevante.',
                'Faça um saque pequeno logo no início, para conhecer o processo.',
            ]),
            ('h2', 'Como é na Safirion'),
            ('p', 'A Safirion opera com regulamentação internacional em Seychelles, mantém o '
                  'capital dos clientes em contas segregadas em bancos de primeiro nível, oferece '
                  'proteção contra saldo negativo e passa por auditoria externa trimestral. Os '
                  'documentos societários e as políticas completas estão no rodapé do site.'),
            ('cta', 'Ver os documentos da Safirion'),
        ],
    },

    # ------------------------------------------------------------------ 4
    {
        'slug': 'quanto-preciso-para-comecar-a-operar',
        'titulo': 'Quanto preciso para começar a operar Forex?',
        'resumo': 'O depósito mínimo é a menor parte da conta. Como calcular o capital que faz '
                  'sentido a partir do risco por operação, e por que começar pequeno é técnico, '
                  'não tímido.',
        'seo_titulo': 'Quanto preciso para começar a operar Forex? O cálculo real',
        'seo_desc': 'Depósito mínimo, custo por operação e risco por trade: como calcular o '
                    'capital inicial que faz sentido para operar Forex sem se expor além do que '
                    'pode perder.',
        'data': '2026-08-12',
        'minutos': 6,
        'tag': 'Primeiros passos',
        'corpo': [
            ('p', 'A resposta que se encontra em qualquer site é o depósito mínimo da corretora — '
                  'US$ 10, US$ 100, US$ 250. É a informação menos útil possível, porque o mínimo '
                  'para <em>abrir</em> a conta não tem relação com o mínimo para <em>operar</em> '
                  'de forma sustentável.'),
            ('h2', 'Comece pelo risco, não pelo saldo'),
            ('p', 'A conta que importa é feita ao contrário. Primeiro você define quanto aceita '
                  'perder em uma única operação. A referência mais usada entre operadores é 1% do '
                  'capital por trade — alguns usam 2%, poucos passam disso com consistência.'),
            ('p', 'Com o risco por operação definido, o tamanho da posição vira consequência da '
                  'distância até o seu stop. E o capital necessário vira consequência do menor '
                  'tamanho de posição que a corretora permite.'),
            ('h2', 'Um exemplo com números'),
            ('p', 'Suponha que você opere EUR/USD com stop de 20 pips. No microlote (0,01), cada '
                  'pip vale cerca de US$ 0,10 — então o risco da operação é de US$ 2.'),
            ('p', 'Se US$ 2 devem representar 1% do seu capital, você precisa de US$ 200 para '
                  'operar no menor tamanho possível respeitando a regra. Com US$ 50, aquela mesma '
                  'operação arrisca 4% da conta, e uma sequência de cinco perdas — que acontece — '
                  'leva 20% do capital.'),
            ('h2', 'O custo por operação também entra'),
            ('p', 'Com spread de 1 pip em microlote, cada entrada custa cerca de US$ 0,10. Parece '
                  'irrelevante, mas em 20 operações por dia são US$ 2 diários. Sobre um capital '
                  'de US$ 200, o custo consome 1% ao dia só em spread — antes de qualquer '
                  'resultado.'),
            ('p', 'É por isso que capital muito baixo não é apenas arriscado: ele torna a '
                  'matemática desfavorável, porque o custo fixo pesa proporcionalmente demais.'),
            ('h2', 'Por que começar pequeno mesmo assim'),
            ('p', 'Nada disso é argumento para depositar muito no início. Os primeiros meses '
                  'servem para conhecer a plataforma, testar o processo de saque e descobrir como '
                  'você reage a uma perda real — coisas que a conta demo não ensina.'),
            ('p', 'Depositar o mínimo, operar no menor tamanho e fazer um saque pequeno nas '
                  'primeiras semanas é um teste barato da corretora. Aumente o capital depois que '
                  'o processo tiver funcionado, não antes.'),
            ('h2', 'Resumo prático'),
            ('ul', [
                'Defina o risco por operação primeiro — 1% do capital é a referência comum.',
                'Calcule o capital a partir do menor lote que a corretora aceita.',
                'Considere o spread: ele consome capital pequeno com rapidez.',
                'Use os primeiros meses para testar a corretora, não para buscar retorno.',
                'Só opere com dinheiro que não faz falta no seu orçamento.',
            ]),
            ('h2', 'Como é na Safirion'),
            ('p', 'O depósito mínimo na Safirion é de US$ 10, com abertura de conta em cerca de 2 '
                  'minutos. Vale repetir o que está acima: o mínimo serve para conhecer a '
                  'plataforma, não como base de uma operação regular.'),
            ('cta', 'Abrir conta na Safirion'),
        ],
    },
]
