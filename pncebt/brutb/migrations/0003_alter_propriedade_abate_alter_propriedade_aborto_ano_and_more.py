# Generated by Django 5.1.5 on 2025-05-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brutb", "0002_remove_propriedade_codigo_rebanho_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="propriedade",
            name="abate",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="aborto_ano",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não sabe"), (3, "Não respondeu")],
                default=3,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="acesso_areas_alagadas",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="alimenta_soro_leite",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="aluga_pastos",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="assistencia_veterinaria",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="classificacao_propriedade",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Rural clássica"),
                    (1, "Aldeia indígena"),
                    (2, "Assentamento"),
                    (3, "Periferia urbana"),
                    (4, "Não respondeu"),
                ],
                default=4,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="compartilha_aguada",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="compartilha_itens",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="consome_leite_cru",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="destino_feto",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Enterra, joga fossa ou queima"),
                    (1, "Alimenta porco ou cão"),
                    (2, "Não faz nada"),
                    (3, "Não respondeu"),
                ],
                default=3,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="entrega_leite",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="entrega_leite_granel",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="gado_concentrado",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="introducao_bov_bub",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="introducao_reprodutores",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="numero_ordenhas",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Não respondeu"),
                    (1, "Não ordenha"),
                    (2, "1 ordenha"),
                    (3, "2 ou 3 ordenhas"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="pasto_comum",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="piquete_parto",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="pouso_boiada_transito",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="produz_queijo_manteiga",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="raca_bovino",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Não respondeu"),
                    (1, "Zebu"),
                    (2, "Europeu de leite"),
                    (3, "Europeu de corte"),
                    (4, "Mestiço"),
                    (5, "Outras raças"),
                    (6, "Não tem"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="raca_bubalino",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Não respondeu"),
                    (1, "Murrah"),
                    (2, "Mediterrâneo"),
                    (3, "Carabao"),
                    (4, "JAFFARABADI"),
                    (5, "Outras raças"),
                    (6, "Não tem"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="regularidade_brucelose",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Uma vez ao ano"),
                    (1, "Duas vezes ao ano"),
                    (2, "Quando compra"),
                    (3, "Quando há aborto na propriedade"),
                    (4, "Quando exigido para movimentação/crédito"),
                    (5, "Não respondeu"),
                ],
                default=5,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="regularidade_tuberculose",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Uma vez ao ano"),
                    (1, "Duas vezes ao ano"),
                    (2, "Quando compra"),
                    (3, "Quando exigido para movimentação/crédito"),
                    (4, "Não respondeu"),
                ],
                default=4,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="resfria_leite",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="testa_brucelose",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="testa_tuberculose",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="tipo_criacao",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Não respondeu"),
                    (1, "Extensivo"),
                    (2, "Semi-confinado"),
                    (3, "Confinado"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="tipo_exploracao",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Não respondeu"),
                    (1, "Corte"),
                    (2, "Leite"),
                    (3, "Misto"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="tipo_ordenha",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Não respondeu"),
                    (1, "Não ordenha"),
                    (2, "Mecânica em sala de ordenha"),
                    (3, "Mecânica ao pé"),
                    (4, "Manual"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="tipo_vacina_brucelose",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Só com B19"),
                    (1, "Com B19 ou RB51"),
                    (2, "Só com RB51"),
                    (3, "Não sabe a vacina"),
                ],
                default=3,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="usa_inseminacao",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Não respondeu"),
                    (1, "Não usa"),
                    (2, "Usa IA e touro"),
                    (3, "Só IA"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="vacina_brucelose",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="vacina_brucelose_adeq_aplicada",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="vacina_brucelose_adeq_conservada",
            field=models.SmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
        migrations.AlterField(
            model_name="propriedade",
            name="venda_reprodutores",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Não"), (1, "Sim"), (2, "Não respondeu/Não sabe")],
                default=2,
            ),
        ),
    ]
