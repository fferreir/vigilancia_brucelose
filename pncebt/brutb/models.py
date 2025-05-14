from django.contrib.gis.db import models
from django.conf import settings
from conta.models import Perfil

class Municipio(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # Brazil's shapefile.
    cd_mun = models.CharField(max_length=7, primary_key=True)
    nm_mun = models.CharField(max_length=100)
    cd_uf = models.CharField(max_length=2)
    nm_uf = models.CharField(max_length=50)
    sigla_uf = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=4674)

    class Meta:
        ordering = ['cd_uf', 'nm_mun']
        indexes = [
            models.Index(fields=['cd_uf', 'nm_mun']),
        ]

    def __str__(self):
        return f'{self.nm_mun}'

class Propriedade(models.Model):
    # Fields corresponding to the attributes in the questionary
    class Exploracao(models.TextChoices):
        NR = '0', 'Não respondeu'
        CORTE = '1', 'Corte'
        LEITE = '2', 'Leite'
        MISTO = '3', 'Misto'

    class Criacao(models.TextChoices):
        NR = '0', 'Não respondeu'
        EXTENSIVO = '1', 'Extensivo'
        SEMICONFINADO = '2', 'Semi-confinado'
        CONFINADO = '3', 'Confinado'

    class Ordenha(models.TextChoices):
        NR = '0', 'Não respondeu'
        ORDENHA_0 = '1', 'Não ordenha'
        ORDENHA_1 = '2', '1 ordenha'
        ORDENHA_2_3 = '3', '2 ou 3 ordenhas'

    class TipoOrdenha(models.TextChoices):
        NR = '0', 'Não respondeu'
        N_OREDENHA = '1', 'Não ordenha'
        SALA = '2', 'Mecânica em sala de ordenha'
        PE = '3', 'Mecânica ao pé'
        MANUAL = '4', 'Manual'

    class Inseminacao(models.TextChoices):
        NR = '0', 'Não respondeu'
        NUSA = '1', 'Não usa'
        IA_TOURO = '2', 'Usa IA e touro'
        IA = '3', 'Só IA'

    class Bovino(models.TextChoices):
        NR = '0', 'Não respondeu'
        ZEBU = '1', 'Zebu'
        EUROPEU_LEITE = '2', 'Europeu de leite'
        EUROPEU_CORTE = '3', 'Europeu de corte'
        MESTICO = '4', 'Mestiço'
        OUTRA = '5', 'Outras raças'
        NTEM = '6', 'Não tem'

    class Bubalino(models.TextChoices):
        NR = '0', 'Não respondeu'
        MURRAH = '1', 'Murrah'
        MEDITERRANEO = '2', 'Mediterrâneo'
        CARABAO = '3', 'Carabao'
        JAFFARABADI = '4', 'JAFFARABADI'
        OUTRA = '5', 'Outras raças'
        NTEM = '6', 'Não tem'

    class Aborto(models.TextChoices):
        NAO = '0', 'Não'
        SIM = '1', 'Sim'
        NAO_SABE = '2', 'Não sabe'
        NR = '3', 'Não respondeu'

    class Feto(models.TextChoices):
        ENTERRA = '0', 'Enterra, joga fossa ou queima'
        ALIMENTA = '1', 'Alimenta porco ou cão'
        NAO_FAZ_NADA = '2', 'Não faz nada'
        NR = '3', 'Não respondeu'

    class SimNao(models.TextChoices):
        NAO = '0', 'Não'
        SIM = '1', 'Sim'
        NR = '3', 'Não respondeu/Não sabe'

    class RegBru(models.TextChoices):
        UMAVEZ = '0', 'Uma vez ao ano'
        DUASVEZES = '1', 'Duas vezes ao ano'
        COMPRA = '2', 'Quando compra'
        ABORTA = '3', 'Quando há aborto na propriedade'
        MOVIMENTACAO = '4', 'Quando exigido para movimentação/crédito'
        NR = '5', 'Não respondeu'

    class RegTB(models.TextChoices):
        UMAVEZ = '0', 'Uma vez ao ano'
        DUASVEZES = '1', 'Duas vezes ao ano'
        COMPRA = '2', 'Quando compra'
        MOVIMENTACAO = '3', 'Quando exigido para movimentação/crédito'
        NR = '4', 'Não respondeu'

    class TipoVacina(models.TextChoices):
        B19 = '0', 'Só com B19'
        B19_RB51 = '1', 'Com B19 ou RB51'
        RB51 = '2', 'Só com RB51'
        NAO_SABE = '3', 'Não sabe a vacina'

    class Classificacao(models.TextChoices):
        RURAL = '0', 'Rural clássica'
        ALDEIA = '1', 'Aldeia indígena'
        ASSENTAMENTO = '2', 'Assentamento'
        PERIFERIA = '3', 'Periferia urbana'

    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    regiao = models.PositiveSmallIntegerField(max_length=2)
    estado = models.CharField(max_length=2)
    proprietario = models.CharField(max_length=200)
    propriedade = models.CharField(max_length=200)
    cod_cadastro_defesa = models.CharField(max_length=40)
    data_inoculacao = models.DateField()
    data_leitura = models.DateField()
    cod_rebanho_estudo = models.PositiveBigIntegerField(min_value=1100015001, max_value=5300108500, unique=True)
    latitude_grau = models.IntegerField(max_value=5, min_value=-33)
    latitude_min = models.IntegerField(max_value=59, min_value=0)
    latitude_seg = models.DecimalField(max_digits=3, decimal_places=1, max_value=59.9, min_value=0.0)
    longitude_grau = models.IntegerField(max_value=-34, min_value=-73)
    longitude_min = models.IntegerField(max_value=59, min_value=0)
    longitude_seg = models.DecimalField(max_digits=3, decimal_places=1, max_value=59.9, min_value=0.0)
    tipo_exploracao = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Exploracao,
        default=Exploracao.NR)
    tipo_criacao = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Criacao,
        default=Criacao.NR
    )
    numero_ordenhas = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Ordenha,
        default=Ordenha.NR
    )
    tipo_ordenha = models.PositiveSmallIntegerField(
        max_length=1,
        choices=TipoOrdenha,
        default=TipoOrdenha.NR
    )
    vacas_lactacao = models.PositiveSmallIntegerField(max_length=6)
    producao_leite = models.PositiveSmallIntegerField(max_length=6)
    usa_inseminacao = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Inseminacao,
        default=Inseminacao.NR
    )
    raca_bovino = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Bovino,
        default=Bovino.NR
    )
    raca_bubalino = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Bubalino,
        default=Bubalino.NR
    )
    bov_macho_castrado = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_macho_0_6 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_macho_7_12 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_macho_13_24 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_macho_25_mais = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_femea_0_6 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_femea_7_12 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_femea_13_24 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bov_femea_25_mais = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_macho_castrado = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_macho_0_6 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_macho_7_12 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_macho_13_24 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_macho_25_mais = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_femea_0_6 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_femea_7_12 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_femea_13_24 = models.PositiveSmallIntegerField(max_length=6, default=0)
    bub_femea_25_mais = models.PositiveSmallIntegerField(max_length=6, default=0)
    ovi_capri = models.BooleanField(default=False)
    equideos = models.BooleanField(default=False)
    suinos = models.BooleanField(default=False)
    aves = models.BooleanField(default=False)
    cao = models.BooleanField(default=False)
    gato = models.BooleanField(default=False)
    silvestre = models.BooleanField(default=False)
    cervideos = models.BooleanField(default=False)
    capivaras = models.BooleanField(default=False)
    felideos = models.BooleanField(default=False)
    marsupiais = models.BooleanField(default=False)
    macacos = models.BooleanField(default=False)
    outro_silvestre = models.TextField(blank=True, max_length=400)
    aborto_ano = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Aborto,
        default=Aborto.NR
    )
    destino_feto = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Feto,
        default=Feto.NR
    )
    testa_brucelose = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    regularidade_brucelose = models.PositiveSmallIntegerField(
        max_length=1,
        choices=RegBru,
        default=RegBru.NR
    )
    testa_tuberculose = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    regularidade_tuberculose = models.PositiveSmallIntegerField(
        max_length=1,
        choices=RegTB,
        default=RegTB.NR
    )
    introducao_bov_bub = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    introducao_exposicao = models.BooleanField(default=False)
    introducao_leilao = models.BooleanField(default=False)
    introducao_comercio = models.BooleanField(default=False)
    introducao_outra_fazenda = models.BooleanField(default=False)
    introducao_reprodutores = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    reprodutores_exposicao = models.BooleanField(default=False)
    reprodutores_leilao = models.BooleanField(default=False)
    reprodutores_comercio = models.BooleanField(default=False)
    reprodutores_outra_fazenda = models.BooleanField(default=False)
    venda_reprodutores = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    venda_reprodutores_exposicao = models.BooleanField(default=False)
    venda_reprodutores_leilao = models.BooleanField(default=False)
    venda_reprodutores_comercio = models.BooleanField(default=False)
    venda_reprodutores_outra_fazenda = models.BooleanField(default=False)
    vacina_brucelose = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    tipo_vacina_brucelose = models.PositiveSmallIntegerField(
        max_length=1,
        choices=TipoVacina,
        default=TipoVacina.NAO_SABE
    )
    abate = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    abate_fazenda = models.BooleanField(default=False)
    abate_sem_inspecao = models.BooleanField(default=False)
    abate_com_inspecao = models.BooleanField(default=False)

    aluga_pastos = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    pasto_comum = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    compartilha_itens = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    compartilha_insumos =  models.BooleanField(default=False)
    compartilha_equipamentos = models.BooleanField(default=False)
    compartilha_funcionarios = models.BooleanField(default=False)
    acesso_areas_alagadas = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    gado_concentrado = models.PositiveSmallIntegerField(
        max_length=1,
        choices=SimNao,
    )
    palafita = models.BooleanField(default=False)
    concentrado_outra = models.BooleanField(default=False)
    concentrado_outra_qual = models.TextField(blank=True, max_length=400)
    piquete_parto = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    entrega_leite = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    entrega_cooperativa = models.BooleanField(default=False)
    entrega_laticinio = models.BooleanField(default=False)
    entrega_consumidor = models.BooleanField(default=False)
    resfria_leite = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    resfria_tanque_proprio = models.BooleanField(default=False)
    resfria_tanque_coletivo = models.BooleanField(default=False)
    entrega_leite_granel = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    produz_queijo_manteiga = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    queijo_manteiga_consumo_proprio = models.BooleanField(default=False)
    queijo_manteiga_venda = models.BooleanField(default=False)
    consome_leite_cru = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    assistencia_veterinaria = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
    )
    veterinario_cooperativa = models.BooleanField(default=False)
    veterinario_privado = models.BooleanField(default=False)
    alimenta_soro_leite = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    bov_bub_comprados_12meses = models.PositiveSmallIntegerField(max_length=6)
    num_faz_comprados_12meses = models.PositiveSmallIntegerField(max_length=6)
    bov_bub_vendidos_12meses = models.PositiveSmallIntegerField(max_length=6)
    num_faz_vendidos_12meses = models.PositiveSmallIntegerField(max_length=6)
    compartilha_aguada = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    pouso_boiada_transito = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    vacina_brucelose_adeq_conservada = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    vacina_brucelose_adeq_aplicada = models.SmallIntegerField(
        max_length=1,
        choices=SimNao,
        default=SimNao.NR
    )
    classificacao_propriedade = models.PositiveSmallIntegerField(
        max_length=1,
        choices=Classificacao,
        default=Classificacao.NR
    )
    veterinario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='registros_propriedades'
    )
    codigo_rebanho = models.CharField(max_length=10, primary_key=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    #class Meta:
    #    ordering = ['municipio']
    #    indexes = [
    #        models.Index(fields=['municipio']),
    #    ]

    def __str__(self):
        return self.codigo_rebanho

