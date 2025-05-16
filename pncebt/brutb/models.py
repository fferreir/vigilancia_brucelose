from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from conta.models import Perfil
from django.urls import reverse

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
    class Exploracao(models.IntegerChoices):
        NR = 0, 'Não respondeu'
        CORTE = 1, 'Corte'
        LEITE = 2, 'Leite'
        MISTO = 3, 'Misto'

    class Criacao(models.IntegerChoices):
        NR = 0, 'Não respondeu'
        EXTENSIVO = 1, 'Extensivo'
        SEMICONFINADO = 2, 'Semi-confinado'
        CONFINADO = 3, 'Confinado'

    class Ordenha(models.IntegerChoices):
        NR = 0, 'Não respondeu'
        ORDENHA_0 = 1, 'Não ordenha'
        ORDENHA_1 = 2, '1 ordenha'
        ORDENHA_2_3 = 3, '2 ou 3 ordenhas'

    class TipoOrdenha(models.IntegerChoices):
        NR = 0, 'Não respondeu'
        N_OREDENHA = 1, 'Não ordenha'
        SALA = 2, 'Mecânica em sala de ordenha'
        PE = 3, 'Mecânica ao pé'
        MANUAL = 4, 'Manual'

    class Inseminacao(models.IntegerChoices):
        NR = 0, 'Não respondeu'
        NUSA = 1, 'Não usa'
        IA_TOURO = 2, 'Usa IA e touro'
        IA = 3, 'Só IA'

    class Bovino(models.IntegerChoices):
        NR = 0, 'Não respondeu'
        ZEBU = 1, 'Zebu'
        EUROPEU_LEITE = 2, 'Europeu de leite'
        EUROPEU_CORTE = 3, 'Europeu de corte'
        MESTICO = 4, 'Mestiço'
        OUTRA = 5, 'Outras raças'
        NTEM = 6, 'Não tem'

    class Bubalino(models.IntegerChoices):
        NR = 0, 'Não respondeu'
        MURRAH = 1, 'Murrah'
        MEDITERRANEO = 2, 'Mediterrâneo'
        CARABAO = 3, 'Carabao'
        JAFFARABADI = 4, 'JAFFARABADI'
        OUTRA = 5, 'Outras raças'
        NTEM = 6, 'Não tem'

    class Aborto(models.IntegerChoices):
        NAO = 0, 'Não'
        SIM = 1, 'Sim'
        NAO_SABE = 2, 'Não sabe'
        NR = 3, 'Não respondeu'

    class Feto(models.IntegerChoices):
        ENTERRA = 0, 'Enterra, joga fossa ou queima'
        ALIMENTA = 1, 'Alimenta porco ou cão'
        NAO_FAZ_NADA = 2, 'Não faz nada'
        NR = 3, 'Não respondeu'

    class SimNao(models.IntegerChoices):
        NAO = 0, 'Não'
        SIM = 1, 'Sim'
        NR = 2, 'Não respondeu/Não sabe'

    class RegBru(models.IntegerChoices):
        UMAVEZ = 0, 'Uma vez ao ano'
        DUASVEZES = 1, 'Duas vezes ao ano'
        COMPRA = 2, 'Quando compra'
        ABORTA = 3, 'Quando há aborto na propriedade'
        MOVIMENTACAO = 4, 'Quando exigido para movimentação/crédito'
        NR = 5, 'Não respondeu'

    class RegTB(models.IntegerChoices):
        UMAVEZ = 0, 'Uma vez ao ano'
        DUASVEZES = 1, 'Duas vezes ao ano'
        COMPRA = 2, 'Quando compra'
        MOVIMENTACAO = 3, 'Quando exigido para movimentação/crédito'
        NR = 4, 'Não respondeu'

    class TipoVacina(models.IntegerChoices):
        B19 = 0, 'Só com B19'
        B19_RB51 = 1, 'Com B19 ou RB51'
        RB51 = 2, 'Só com RB51'
        NAO_SABE = 3, 'Não sabe a vacina'

    class Classificacao(models.IntegerChoices):
        RURAL = 0, 'Rural clássica'
        ALDEIA = 1, 'Aldeia indígena'
        ASSENTAMENTO = 2, 'Assentamento'
        PERIFERIA = 3, 'Periferia urbana'
        NR = 4, 'Não respondeu'

    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    regiao = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=2)
    proprietario = models.CharField(max_length=200)
    propriedade = models.CharField(max_length=200)
    cod_cadastro_defesa = models.CharField(max_length=40)
    data_inoculacao = models.DateField()
    data_leitura = models.DateField()
    cod_rebanho_estudo = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1100015001), MaxValueValidator(5300108500)], unique=True, primary_key=True
    )
    latitude_grau = models.IntegerField(validators=[MinValueValidator(-33), MaxValueValidator(5)])
    latitude_min = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    latitude_seg = models.DecimalField(validators=[MinValueValidator(0.0), MaxValueValidator(59.9)], max_digits=3, decimal_places=1)
    longitude_grau = models.IntegerField(validators=[MinValueValidator(-73), MaxValueValidator(-34)])
    longitude_min = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    longitude_seg = models.DecimalField(validators=[MinValueValidator(0.0), MaxValueValidator(59.9)], max_digits=3, decimal_places=1)
    tipo_exploracao = models.PositiveSmallIntegerField(
        choices=Exploracao,
        default=Exploracao.NR)
    tipo_criacao = models.PositiveSmallIntegerField(
        choices=Criacao,
        default=Criacao.NR
    )
    numero_ordenhas = models.PositiveSmallIntegerField(
        choices=Ordenha,
        default=Ordenha.NR
    )
    tipo_ordenha = models.PositiveSmallIntegerField(
        choices=TipoOrdenha,
        default=TipoOrdenha.NR
    )
    vacas_lactacao = models.PositiveSmallIntegerField()
    producao_leite = models.PositiveSmallIntegerField()
    usa_inseminacao = models.PositiveSmallIntegerField(
        choices=Inseminacao,
        default=Inseminacao.NR
    )
    raca_bovino = models.PositiveSmallIntegerField(
        choices=Bovino,
        default=Bovino.NR
    )
    raca_bubalino = models.PositiveSmallIntegerField(
        choices=Bubalino,
        default=Bubalino.NR
    )
    bov_macho_castrado = models.PositiveSmallIntegerField(default=0)
    bov_macho_0_6 = models.PositiveSmallIntegerField(default=0)
    bov_macho_7_12 = models.PositiveSmallIntegerField(default=0)
    bov_macho_13_24 = models.PositiveSmallIntegerField( default=0)
    bov_macho_25_mais = models.PositiveSmallIntegerField(default=0)
    bov_femea_0_6 = models.PositiveSmallIntegerField(default=0)
    bov_femea_7_12 = models.PositiveSmallIntegerField(default=0)
    bov_femea_13_24 = models.PositiveSmallIntegerField(default=0)
    bov_femea_25_mais = models.PositiveSmallIntegerField(default=0)
    bub_macho_castrado = models.PositiveSmallIntegerField(default=0)
    bub_macho_0_6 = models.PositiveSmallIntegerField(default=0)
    bub_macho_7_12 = models.PositiveSmallIntegerField(default=0)
    bub_macho_13_24 = models.PositiveSmallIntegerField(default=0)
    bub_macho_25_mais = models.PositiveSmallIntegerField(default=0)
    bub_femea_0_6 = models.PositiveSmallIntegerField(default=0)
    bub_femea_7_12 = models.PositiveSmallIntegerField(default=0)
    bub_femea_13_24 = models.PositiveSmallIntegerField(default=0)
    bub_femea_25_mais = models.PositiveSmallIntegerField(default=0)
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
        choices=Aborto,
        default=Aborto.NR
    )
    destino_feto = models.PositiveSmallIntegerField(
        choices=Feto,
        default=Feto.NR
    )
    testa_brucelose = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    regularidade_brucelose = models.PositiveSmallIntegerField(
        choices=RegBru,
        default=RegBru.NR
    )
    testa_tuberculose = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    regularidade_tuberculose = models.PositiveSmallIntegerField(
        choices=RegTB,
        default=RegTB.NR
    )
    introducao_bov_bub = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    introducao_exposicao = models.BooleanField(default=False)
    introducao_leilao = models.BooleanField(default=False)
    introducao_comercio = models.BooleanField(default=False)
    introducao_outra_fazenda = models.BooleanField(default=False)
    introducao_reprodutores = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    reprodutores_exposicao = models.BooleanField(default=False)
    reprodutores_leilao = models.BooleanField(default=False)
    reprodutores_comercio = models.BooleanField(default=False)
    reprodutores_outra_fazenda = models.BooleanField(default=False)
    venda_reprodutores = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    venda_reprodutores_exposicao = models.BooleanField(default=False)
    venda_reprodutores_leilao = models.BooleanField(default=False)
    venda_reprodutores_comercio = models.BooleanField(default=False)
    venda_reprodutores_outra_fazenda = models.BooleanField(default=False)
    vacina_brucelose = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    tipo_vacina_brucelose = models.PositiveSmallIntegerField(
        choices=TipoVacina,
        default=TipoVacina.NAO_SABE
    )
    abate = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    abate_fazenda = models.BooleanField(default=False)
    abate_sem_inspecao = models.BooleanField(default=False)
    abate_com_inspecao = models.BooleanField(default=False)

    aluga_pastos = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    pasto_comum = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    compartilha_itens = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    compartilha_insumos =  models.BooleanField(default=False)
    compartilha_equipamentos = models.BooleanField(default=False)
    compartilha_funcionarios = models.BooleanField(default=False)
    acesso_areas_alagadas = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    gado_concentrado = models.PositiveSmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    palafita = models.BooleanField(default=False)
    concentrado_outra = models.BooleanField(default=False)
    concentrado_outra_qual = models.TextField(blank=True, max_length=400)
    piquete_parto = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    entrega_leite = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    entrega_cooperativa = models.BooleanField(default=False)
    entrega_laticinio = models.BooleanField(default=False)
    entrega_consumidor = models.BooleanField(default=False)
    resfria_leite = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    resfria_tanque_proprio = models.BooleanField(default=False)
    resfria_tanque_coletivo = models.BooleanField(default=False)
    entrega_leite_granel = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    produz_queijo_manteiga = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    queijo_manteiga_consumo_proprio = models.BooleanField(default=False)
    queijo_manteiga_venda = models.BooleanField(default=False)
    consome_leite_cru = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    assistencia_veterinaria = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    veterinario_cooperativa = models.BooleanField(default=False)
    veterinario_privado = models.BooleanField(default=False)
    alimenta_soro_leite = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    bov_bub_comprados_12meses = models.PositiveSmallIntegerField()
    num_faz_comprados_12meses = models.PositiveSmallIntegerField()
    bov_bub_vendidos_12meses = models.PositiveSmallIntegerField()
    num_faz_vendidos_12meses = models.PositiveSmallIntegerField()
    compartilha_aguada = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    pouso_boiada_transito = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    vacina_brucelose_adeq_conservada = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    vacina_brucelose_adeq_aplicada = models.SmallIntegerField(
        choices=SimNao,
        default=SimNao.NR
    )
    classificacao_propriedade = models.PositiveSmallIntegerField(
        choices=Classificacao,
        default=Classificacao.NR
    )
    veterinario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='registros_propriedades'
    )
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    #class Meta:
    #    ordering = ['municipio']
    #    indexes = [
    #        models.Index(fields=['municipio']),
    #    ]

    def get_absolute_url(self):
        return reverse(
            'brutb:propriedade_detalhe',
            args=[self.cod_rebanho_estudo]
        )

    def __int__(self):
        return self.cod_rebanho_estudo

