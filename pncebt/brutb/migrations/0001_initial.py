# Generated by Django 5.1.5 on 2025-05-15 11:12

import django.contrib.gis.db.models.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('cd_mun', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nm_mun', models.CharField(max_length=100)),
                ('cd_uf', models.CharField(max_length=2)),
                ('nm_uf', models.CharField(max_length=50)),
                ('sigla_uf', models.CharField(max_length=2)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674)),
            ],
            options={
                'ordering': ['cd_uf', 'nm_mun'],
                'indexes': [models.Index(fields=['cd_uf', 'nm_mun'], name='brutb_munic_cd_uf_bd41fa_idx')],
            },
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('regiao', models.PositiveSmallIntegerField()),
                ('estado', models.CharField(max_length=2)),
                ('proprietario', models.CharField(max_length=200)),
                ('propriedade', models.CharField(max_length=200)),
                ('cod_cadastro_defesa', models.CharField(max_length=40)),
                ('data_inoculacao', models.DateField()),
                ('data_leitura', models.DateField()),
                ('cod_rebanho_estudo', models.PositiveBigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1100015001), django.core.validators.MaxValueValidator(5300108500)])),
                ('latitude_grau', models.IntegerField(validators=[django.core.validators.MinValueValidator(-33), django.core.validators.MaxValueValidator(5)])),
                ('latitude_min', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)])),
                ('latitude_seg', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(59.9)])),
                ('longitude_grau', models.IntegerField(validators=[django.core.validators.MinValueValidator(-73), django.core.validators.MaxValueValidator(-34)])),
                ('longitude_min', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)])),
                ('longitude_seg', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(59.9)])),
                ('tipo_exploracao', models.PositiveSmallIntegerField(choices=[('0', 'Não respondeu'), ('1', 'Corte'), ('2', 'Leite'), ('3', 'Misto')], default='0')),
                ('tipo_criacao', models.PositiveSmallIntegerField(choices=[('0', 'Não respondeu'), ('1', 'Extensivo'), ('2', 'Semi-confinado'), ('3', 'Confinado')], default='0')),
                ('numero_ordenhas', models.PositiveSmallIntegerField(choices=[('0', 'Não respondeu'), ('1', 'Não ordenha'), ('2', '1 ordenha'), ('3', '2 ou 3 ordenhas')], default='0')),
                ('tipo_ordenha', models.PositiveSmallIntegerField(choices=[('0', 'Não respondeu'), ('1', 'Não ordenha'), ('2', 'Mecânica em sala de ordenha'), ('3', 'Mecânica ao pé'), ('4', 'Manual')], default='0')),
                ('vacas_lactacao', models.PositiveSmallIntegerField()),
                ('producao_leite', models.PositiveSmallIntegerField()),
                ('usa_inseminacao', models.PositiveSmallIntegerField(choices=[('0', 'Não respondeu'), ('1', 'Não usa'), ('2', 'Usa IA e touro'), ('3', 'Só IA')], default='0')),
                ('raca_bovino', models.PositiveSmallIntegerField(choices=[('0', 'Não respondeu'), ('1', 'Zebu'), ('2', 'Europeu de leite'), ('3', 'Europeu de corte'), ('4', 'Mestiço'), ('5', 'Outras raças'), ('6', 'Não tem')], default='0')),
                ('raca_bubalino', models.PositiveSmallIntegerField(choices=[('0', 'Não respondeu'), ('1', 'Murrah'), ('2', 'Mediterrâneo'), ('3', 'Carabao'), ('4', 'JAFFARABADI'), ('5', 'Outras raças'), ('6', 'Não tem')], default='0')),
                ('bov_macho_castrado', models.PositiveSmallIntegerField(default=0)),
                ('bov_macho_0_6', models.PositiveSmallIntegerField(default=0)),
                ('bov_macho_7_12', models.PositiveSmallIntegerField(default=0)),
                ('bov_macho_13_24', models.PositiveSmallIntegerField(default=0)),
                ('bov_macho_25_mais', models.PositiveSmallIntegerField(default=0)),
                ('bov_femea_0_6', models.PositiveSmallIntegerField(default=0)),
                ('bov_femea_7_12', models.PositiveSmallIntegerField(default=0)),
                ('bov_femea_13_24', models.PositiveSmallIntegerField(default=0)),
                ('bov_femea_25_mais', models.PositiveSmallIntegerField(default=0)),
                ('bub_macho_castrado', models.PositiveSmallIntegerField(default=0)),
                ('bub_macho_0_6', models.PositiveSmallIntegerField(default=0)),
                ('bub_macho_7_12', models.PositiveSmallIntegerField(default=0)),
                ('bub_macho_13_24', models.PositiveSmallIntegerField(default=0)),
                ('bub_macho_25_mais', models.PositiveSmallIntegerField(default=0)),
                ('bub_femea_0_6', models.PositiveSmallIntegerField(default=0)),
                ('bub_femea_7_12', models.PositiveSmallIntegerField(default=0)),
                ('bub_femea_13_24', models.PositiveSmallIntegerField(default=0)),
                ('bub_femea_25_mais', models.PositiveSmallIntegerField(default=0)),
                ('ovi_capri', models.BooleanField(default=False)),
                ('equideos', models.BooleanField(default=False)),
                ('suinos', models.BooleanField(default=False)),
                ('aves', models.BooleanField(default=False)),
                ('cao', models.BooleanField(default=False)),
                ('gato', models.BooleanField(default=False)),
                ('silvestre', models.BooleanField(default=False)),
                ('cervideos', models.BooleanField(default=False)),
                ('capivaras', models.BooleanField(default=False)),
                ('felideos', models.BooleanField(default=False)),
                ('marsupiais', models.BooleanField(default=False)),
                ('macacos', models.BooleanField(default=False)),
                ('outro_silvestre', models.TextField(blank=True, max_length=400)),
                ('aborto_ano', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('2', 'Não sabe'), ('3', 'Não respondeu')], default='3')),
                ('destino_feto', models.PositiveSmallIntegerField(choices=[('0', 'Enterra, joga fossa ou queima'), ('1', 'Alimenta porco ou cão'), ('2', 'Não faz nada'), ('3', 'Não respondeu')], default='3')),
                ('testa_brucelose', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('regularidade_brucelose', models.PositiveSmallIntegerField(choices=[('0', 'Uma vez ao ano'), ('1', 'Duas vezes ao ano'), ('2', 'Quando compra'), ('3', 'Quando há aborto na propriedade'), ('4', 'Quando exigido para movimentação/crédito'), ('5', 'Não respondeu')], default='5')),
                ('testa_tuberculose', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('regularidade_tuberculose', models.PositiveSmallIntegerField(choices=[('0', 'Uma vez ao ano'), ('1', 'Duas vezes ao ano'), ('2', 'Quando compra'), ('3', 'Quando exigido para movimentação/crédito'), ('4', 'Não respondeu')], default='4')),
                ('introducao_bov_bub', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('introducao_exposicao', models.BooleanField(default=False)),
                ('introducao_leilao', models.BooleanField(default=False)),
                ('introducao_comercio', models.BooleanField(default=False)),
                ('introducao_outra_fazenda', models.BooleanField(default=False)),
                ('introducao_reprodutores', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('reprodutores_exposicao', models.BooleanField(default=False)),
                ('reprodutores_leilao', models.BooleanField(default=False)),
                ('reprodutores_comercio', models.BooleanField(default=False)),
                ('reprodutores_outra_fazenda', models.BooleanField(default=False)),
                ('venda_reprodutores', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('venda_reprodutores_exposicao', models.BooleanField(default=False)),
                ('venda_reprodutores_leilao', models.BooleanField(default=False)),
                ('venda_reprodutores_comercio', models.BooleanField(default=False)),
                ('venda_reprodutores_outra_fazenda', models.BooleanField(default=False)),
                ('vacina_brucelose', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('tipo_vacina_brucelose', models.PositiveSmallIntegerField(choices=[('0', 'Só com B19'), ('1', 'Com B19 ou RB51'), ('2', 'Só com RB51'), ('3', 'Não sabe a vacina')], default='3')),
                ('abate', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('abate_fazenda', models.BooleanField(default=False)),
                ('abate_sem_inspecao', models.BooleanField(default=False)),
                ('abate_com_inspecao', models.BooleanField(default=False)),
                ('aluga_pastos', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('pasto_comum', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('compartilha_itens', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('compartilha_insumos', models.BooleanField(default=False)),
                ('compartilha_equipamentos', models.BooleanField(default=False)),
                ('compartilha_funcionarios', models.BooleanField(default=False)),
                ('acesso_areas_alagadas', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('gado_concentrado', models.PositiveSmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')])),
                ('palafita', models.BooleanField(default=False)),
                ('concentrado_outra', models.BooleanField(default=False)),
                ('concentrado_outra_qual', models.TextField(blank=True, max_length=400)),
                ('piquete_parto', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('entrega_leite', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('entrega_cooperativa', models.BooleanField(default=False)),
                ('entrega_laticinio', models.BooleanField(default=False)),
                ('entrega_consumidor', models.BooleanField(default=False)),
                ('resfria_leite', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('resfria_tanque_proprio', models.BooleanField(default=False)),
                ('resfria_tanque_coletivo', models.BooleanField(default=False)),
                ('entrega_leite_granel', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('produz_queijo_manteiga', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('queijo_manteiga_consumo_proprio', models.BooleanField(default=False)),
                ('queijo_manteiga_venda', models.BooleanField(default=False)),
                ('consome_leite_cru', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('assistencia_veterinaria', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')])),
                ('veterinario_cooperativa', models.BooleanField(default=False)),
                ('veterinario_privado', models.BooleanField(default=False)),
                ('alimenta_soro_leite', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('bov_bub_comprados_12meses', models.PositiveSmallIntegerField()),
                ('num_faz_comprados_12meses', models.PositiveSmallIntegerField()),
                ('bov_bub_vendidos_12meses', models.PositiveSmallIntegerField()),
                ('num_faz_vendidos_12meses', models.PositiveSmallIntegerField()),
                ('compartilha_aguada', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('pouso_boiada_transito', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('vacina_brucelose_adeq_conservada', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('vacina_brucelose_adeq_aplicada', models.SmallIntegerField(choices=[('0', 'Não'), ('1', 'Sim'), ('3', 'Não respondeu/Não sabe')], default='3')),
                ('classificacao_propriedade', models.PositiveSmallIntegerField(choices=[('0', 'Rural clássica'), ('1', 'Aldeia indígena'), ('2', 'Assentamento'), ('3', 'Periferia urbana'), ('4', 'Não respondeu')], default='4')),
                ('codigo_rebanho', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='brutb.municipio')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registros_propriedades', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
