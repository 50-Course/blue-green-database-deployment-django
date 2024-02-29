Blue Green Deployment is a simple project to explore managing database state in production such as the `Blue-Green-Deployment` techique.


## Blue-Green-Deployment

Django provides a special migration function, `migrations.SeperateDatabaseAndState`, to separate the database schema and the data. This is useful for managing database state in production such as the `Blue-Green-Deployment` techique.
Underneath, it alters the database schema and the data separately. It is useful for managing database state in production such as the `Blue-Green-Deployment` techique.

### Usage

```python
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    "CREATE TABLE myapp_mymodel (id int, name varchar(30))",
                    "DROP TABLE myapp_mymodel"
                ),
            ],
            state_operations=[
                migrations.CreateModel(
                    name='MyModel',
                    fields=[
                        ('id', models.AutoField(primary_key=True)),
                        ('name', models.CharField(max_length=30)),
                    ],
                ),
            ],
        ),
    ]
```

