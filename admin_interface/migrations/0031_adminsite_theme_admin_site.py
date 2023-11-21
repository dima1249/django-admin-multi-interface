from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0030_theme_collapsible_stacked_inlines_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Tapatrip', max_length=50, unique=True, verbose_name='Admin name')),
                ('cache_name', models.CharField(default='tapatrip', max_length=50, unique=True, verbose_name='Cache name')),
            ],
            options={
                'verbose_name': 'Admin Site',
                'verbose_name_plural': 'Admin Sites',
            },
        ),
        migrations.AddField(
            model_name='theme',
            name='admin_site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_interface.adminsite', verbose_name='Admin Name'),
        ),
    ]
