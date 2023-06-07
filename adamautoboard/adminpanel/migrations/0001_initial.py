# Generated by Django 4.2.2 on 2023-06-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Brand')),
                ('model', models.CharField(max_length=50, verbose_name='Model')),
                ('year', models.CharField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025)], max_length=20, verbose_name='Anul producerii')),
                ('hp', models.CharField(max_length=50, null=True, verbose_name='Putere (cp)')),
                ('kw', models.CharField(max_length=50, null=True, verbose_name='Putere (kw))')),
                ('fuel', models.CharField(choices=[('Diesel', 'Diesel'), ('Benzina', 'Benzina'), ('GPL', 'GPL'), ('Hybrid', 'Hybrid'), ('Benzina + GPL', 'Benzina + GPL')], max_length=20, verbose_name='Combustibil')),
                ('gearbox', models.CharField(choices=[('Manual', 'Manual'), ('Automat', 'Automat')], max_length=10, verbose_name='Cutie')),
                ('transmission', models.CharField(choices=[('Fata', 'Fata'), ('Spate', 'Spate'), ('4x4', '4x4')], max_length=20, verbose_name='Transmisie')),
                ('color', models.CharField(max_length=20, verbose_name='Culoare')),
                ('body', models.CharField(max_length=20, verbose_name='Caroserie')),
                ('seats', models.CharField(max_length=50, verbose_name='Locuri')),
                ('urban_comsumption', models.CharField(max_length=50, null=True, verbose_name='Consum oras')),
                ('extra_urban_comsumption', models.CharField(max_length=50, null=True, verbose_name='Consum exterior')),
                ('mixed_comsumption', models.CharField(max_length=50, null=True, verbose_name='Consum mixt')),
            ],
        ),
    ]
