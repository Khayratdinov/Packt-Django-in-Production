## Developing Web Applications with Django: A Learning Guide

### Review Questions

**1. What is the core principle of Django's MVT framework?**  
**2. Why is Django relevant in modern web development, especially in a mobile-first world?**  
**3. How do you create a new Django app and register it in a project?**  
**4. How do you link app views to the project's `urls.py` file?**  
**5. What are the advantages of using DRF for building APIs?**  
**6. What are the best practices for defining RESTful APIs?**  
**7. List API versioning methods and explain how to implement URL path-based versioning with DRF.**  
**8. What is the difference between functional and class-based views in DRF?**  
**9. Why are Generic Views important in DRF?**  
**10. What role do API development tools like Postman play in the development process?**

### Answers to Review Questions

1. **MVT (Model-View-Template)** is a framework where the **Model** handles data, the **View** manages logic, and the **Template** presents data to users.
2. Django is relevant because it integrates seamlessly with DRF, enabling the creation of **API-first** applications ideal for mobile platforms.
3. Create an app using `python manage.py startapp app_name` and register it by adding it to the `INSTALLED_APPS` list in `settings.py`.
4. Create a `urls.py` file in the app to define routes and associate them with views. Then, include the app's `urls.py` in the project's main `urls.py`.
5. DRF simplifies RESTful API development by providing serialization, versioning tools, and a user-friendly interface for managing API requests and responses.
6. Use nouns in endpoint paths, apply correct HTTP methods, maintain a nested structure, implement versioning, use proper status codes, and ensure JSON formatting.
7. Methods include Accept header, URL path, query parameters, and host name. For URL path-based versioning, configure `DEFAULT_VERSIONING_CLASS` in `settings.py` and add a `version` parameter to URL paths.
8. Functional views are simple functions, while class-based views are classes that extend APIView or Generic Views for more structured logic.
9. Generic Views streamline CRUD operations by providing predefined methods and structures, reducing boilerplate code.
10. Tools like Postman improve efficiency by enabling API testing, mock server creation, documentation, and automated testing.

### Essay Topics

1. **Compare MVC and MVT in web development, and explain how Django implements the MVT pattern.**  
2. **Discuss the pros and cons of Django for modern web applications, and give examples of projects where Django is an optimal choice.**  
3. **Analyze the importance of API versioning in the development and maintenance of web applications. Explain different versioning approaches and their advantages.**  
4. **Compare functional and class-based views in DRF. When is each approach preferable?**  
5. **Describe how API development tools like Postman enhance the development process and improve API quality.**

### Glossary

- **Django:** A high-level Python framework for web development.  
- **DRF (Django Rest Framework):** A toolkit for building RESTful APIs with Django.  
- **MVT (Model-View-Template):** An architectural pattern used in Django.  
- **REST API:** An architectural style for web service development.  
- **API-first:** A development approach focusing on APIs as the core component.  
- **Virtualenv:** A tool for creating isolated Python environments.  
- **HTTP Methods:** GET, POST, PUT, PATCH, DELETE - methods for resource interaction over HTTP.  
- **HTTP Status Codes:** Codes indicating the result of HTTP requests.  
- **JSON (JavaScript Object Notation):** A lightweight data-interchange format.  
- **Functional Views:** Functions that handle HTTP requests.  
- **Class-based Views:** Classes that structure and handle HTTP requests.  
- **Generic Views:** Prebuilt classes for CRUD operations.  
- **Postman:** A tool for testing and developing APIs.  
- **Mock Server:** A server that simulates a real API for testing purposes.