# Chapter 01: Setting Up Django with Django REST Framework (DRF)

## 📚 Topics Covered

### 1. Basics of Django:
- Understanding the MVT (Model-View-Template) architecture.
- Creating a new Django project and application.
- Configuring the project and registering apps in `settings.py`.
- Working with routing using `urls.py`.

### 2. Django Rest Framework (DRF):
- Installing and configuring DRF.
- Adding `rest_framework` to `INSTALLED_APPS`.
- Creating APIs using `APIView` and `Response`.

### 3. RESTful API:
- Performing CRUD operations using HTTP methods (GET, POST, PUT, DELETE).
- Best practices for designing RESTful APIs:
  - Naming endpoints appropriately.
  - Using proper HTTP status codes.
  - Applying JSON format for data exchange.
- API versioning using URL paths.

---

## 📂 Related Files

### README
- [**README на русском языке**](./README-ru.md): Основная информация о проекте.
- [**README in English**](./README.md): Main information about the project.

### Review Questions
- [**На русском языке**](./docs/ReviewQuestions-ru.md): Контрольные вопросы для проверки понимания.
- [**In English**](./docs/ReviewQuestions-en.md): Review questions for understanding key concepts.

### FAQ
- [**На русском языке**](./docs/FAQ-ru.md): Часто задаваемые вопросы по Django и DRF.
- [**In English**](./docs/FAQ-en.md): Frequently Asked Questions about Django and DRF.


---

## 🛠 Chapter Overview

The first chapter explores the basics of building web applications with Django, project setup, folder structure, and integrating Django Rest Framework (DRF) for developing RESTful APIs.

### Key Topics:

1. **Introduction to Django:**
   - History and advantages of Django.
   - The MVT (Model-View-Template) architecture.
   - Relevance of Django in modern web development.
   - Integration with DRF for creating API-first applications.

2. **Setting up a Django Project:**
   - Creating a Python virtual environment.
   - Installing Django.
   - Creating a project and application.
   - Registering the application in `settings.py`.
   - Linking app views with `urls.py`.

3. **Integrating Django Rest Framework (DRF):**
   - Installing DRF.
   - Adding `rest_framework` to `INSTALLED_APPS`.
   - Using `Response` from DRF in views.

4. **Creating RESTful APIs:**
   - Best practices for naming API endpoints.
   - Using appropriate HTTP methods (GET, POST, PUT, PATCH, DELETE).
   - Nested endpoint structures.
   - API versioning.
   - Using HTTP status codes.
   - JSON data format.

5. **API Versioning with DRF:**
   - Methods of versioning (Accept header, URL path, query parameters, host name).
   - Implementing versioning through URL paths in DRF.
   - Configuring custom versioning classes.
   - Restricting allowed versions.

6. **Working with DRF Views:**
   - Functional views with the `@api_view` decorator.
   - Class-based views: `APIView` and Generic Views.
   - Linking views to `urls.py`.

7. **API Development Tools:**
   - Postman: creating mock servers, API documentation, collections, and tests.

---

## 🎯 Project Goal

To strengthen foundational skills in Django and Django Rest Framework (DRF) while learning how to create RESTful APIs.
