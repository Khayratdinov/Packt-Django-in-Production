# Chapter 2: Exploring Django ORM, Models, and Migrations


---

## 📂 Related Files

### README
- [**README на русском языке**](./README-ru.md): Основная информация о проекте.
- [**README in English**](./README.md): Main information about the project.

### Review Questions
- [**На русском языке**](./docs/ReviewQuestions-ru.md): Контрольные вопросы для проверки понимания.
- [**In English**](./docs/ReviewQuestions-en.md): Review questions for understanding key concepts.

---


## 🛠 Chapter Summary

This chapter provides a detailed overview of how Django works with databases and explains how to use Django ORM functionality to create and manage models. It begins with configuring PostgreSQL and connecting it to a Django project (replacing the default SQLite). The chapter then explores how to design and use models, handle different types of relationships (ForeignKey, ManyToMany, OneToOne), and apply normalization principles. Special attention is given to migration mechanisms (`makemigrations`, `migrate`), potential pitfalls in collaborative development, and handling reverse migrations. The author also provides recommendations for performance optimization and the use of tools like `select_related` and `prefetch_related`. The chapter concludes with an overview of the asynchronous ORM introduced in Django 4.1.

---

### 📚 Key Topics:

1. **Setting up PostgreSQL and Integrating it with Django**  
   - Preparing to work with a remote PostgreSQL server (e.g., ElephantSQL) or a local installation.  
   - Configuring `settings.py` (ENGINE, HOST, NAME, USER, PORT, PASSWORD).  
   - Installing the `psycopg2-binary` library and testing the connection by running the server.

2. **Working with Models and Django ORM**  
   - Creating models (e.g., `Author`, `Blog`) and linking them to database tables.  
   - Key fields (e.g., `CharField`, `EmailField`, `TextField`) and their parameters (`null`, `blank`, `default`).  
   - Using `auto_now` and `auto_now_add` for timestamps.  
   - Avoiding raw SQL queries and leveraging query expressions, `F` methods, `aggregate`, etc.  
   - Principles of reverse access (`blog_set` for `ForeignKey`) and using `related_name`.

3. **Normalization and Relationship Types in Django**  
   - `OneToOneField`, `ForeignKey`, `ManyToManyField`: key patterns and when to use them.  
   - `on_delete` options (`CASCADE`, `PROTECT`, `RESTRICT`, etc.) and their impact on data integrity.  
   - Types of model inheritance: abstract classes (`abstract = True`), multi-table inheritance, and proxy models.

4. **Django Migrations: Mechanics and Nuances**  
   - How `makemigrations` and `migrate` work, storing migrations, and the `django_migrations` table.  
   - Reverse migrations and fake migrations for syncing manually applied changes.  
   - Practical advice: when to avoid data migrations, why system checks for duplicates are important, and how to correctly add new fields.

5. **Best Practices for Working with ORM**  
   - Organizing base abstract models (e.g., `TimeStampedBaseModel`).  
   - Proper handling of `timezone.now()` and avoiding circular dependencies using string references to models.  
   - Always defining the `__str__` method for better object representation.  
   - Using model methods and model managers, and choosing the right primary key type (Integer ID vs. UUID).  
   - Applying transactions (`transaction.atomic`) for safe bulk updates.  
   - Caution when using `GenericForeignKey`.

6. **Performance Optimization**  
   - Analyzing and planning queries with `explain` and `analyze`.  
   - Using indexes (`Meta.indexes`) where appropriate, while considering the trade-offs with write speed.  
   - Leveraging `select_related` for `ForeignKey` and `OneToOneField` and `prefetch_related` for `ManyToMany` and reverse lookups.  
   - Working with `bulk_create`, `bulk_update`, `get_or_create`, and `update_or_create`.  
   - Connection settings (`CONN_MAX_AGE`, `statement_timeout`) for improved efficiency and stability.

7. **Asynchronous ORM in Django 4.1**  
   - A brief overview of the new async capabilities in Django ORM.  
   - Comparison of the classic synchronous approach with the async/await approach (`aget` vs. `get`).  
   - Current limitations (e.g., not all transactions are supported in async) and the gradual development of this functionality.

---

## 🎯 Chapter Goal

The main goal of this chapter is to help developers gain a deeper understanding of how to use Django ORM and databases in real-world production scenarios. The author demonstrates how to establish proper relationships between models, effectively manage migrations, and avoid common pitfalls when working with data. Additionally, the chapter emphasizes the importance of query optimization, understanding performance, and leveraging the new asynchronous ORM features for building more scalable applications.