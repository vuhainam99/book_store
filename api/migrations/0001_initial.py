# Generated by Django 3.1.4 on 2021-11-28 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_authors', models.CharField(max_length=250)),
                ('book_desc', models.CharField(max_length=10000)),
                ('book_edition', models.CharField(max_length=250)),
                ('book_format', models.CharField(max_length=250)),
                ('book_isbn', models.CharField(max_length=250)),
                ('book_pages', models.IntegerField(default=0)),
                ('book_rating', models.FloatField(default=0)),
                ('book_rating_count', models.IntegerField(default=0)),
                ('book_review_count', models.IntegerField(default=0)),
                ('book_title', models.CharField(max_length=250)),
                ('genres', models.CharField(max_length=250)),
                ('image_url', models.CharField(max_length=250)),
                ('book_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres_vi', models.CharField(max_length=100)),
                ('genres_eg', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('ratingCount', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
            ],
        ),
        migrations.CreateModel(
            name='User_To_read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_book', to='api.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_user', to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='User_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_id', to='api.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=30)),
                ('order_info', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sale', to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='Book_Sales_His',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('status', models.SmallIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_sale', to='api.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='api.order')),
            ],
        ),
        migrations.CreateModel(
            name='Book_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_in_stock', models.IntegerField(default=0)),
                ('source', models.CharField(max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_if', to='api.book')),
            ],
        ),
        migrations.CreateModel(
            name='Book_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodreads_book_id', models.IntegerField(default=0)),
                ('best_book_id', models.IntegerField(default=0)),
                ('work_id', models.IntegerField(default=0)),
                ('books_count', models.IntegerField(default=0)),
                ('isbn', models.IntegerField(default=0)),
                ('isbn13', models.CharField(max_length=50)),
                ('authors', models.CharField(max_length=250)),
                ('original_publication_year', models.FloatField(default=0)),
                ('original_title', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=10)),
                ('average_rating', models.FloatField(default=0)),
                ('ratings_count', models.IntegerField(default=0)),
                ('work_ratings_count', models.IntegerField(default=0)),
                ('work_text_reviews_count', models.IntegerField(default=0)),
                ('ratings_1', models.IntegerField(default=0)),
                ('ratings_2', models.IntegerField(default=0)),
                ('ratings_3', models.IntegerField(default=0)),
                ('ratings_4', models.IntegerField(default=0)),
                ('ratings_5', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=100)),
                ('small_image_url', models.CharField(max_length=100)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='api.book')),
            ],
        ),
    ]
