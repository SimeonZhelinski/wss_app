## SoftUni Django Advanced Project

This is my project for SoftUni Django Advanced Module.

The project is deployed in PythonAnywhere and you can access it from the following link:


# Water Supply & Sewerage Project Manager
/WSS Project Manager/ or WSS for short.

 WSS is a web application developed with Django. The main goal of the application is for clients to create various types of projects, with the data allowing for the calculation of dimensional and parameter details for water supply and sewage systems. For one of the projects, an approximate cost for project execution is calculated based on current prices for materials and labor.


### Tech Description:

##### Models (7):
- WssUser
- Profile
- BuildingWithoutExistingInfrastructure
- BuildingWithExistingInfrastructure
- InfrastructureProject
- ContactMessage
- Review

##### Views (29):
- Six views are Function Based Views and the other twenty three are Class Based Views.

##### Templates (26):
- Django Template Language is used with some additional help of Bootstrap.

##### Forms (7):
- Seven main forms are used for the project.


#### The project is developed using the following technologies:
- **Back-end:** Python, Django Framework
- **Front-end:** Custom HTML, CSS and additional components built with Bootstrap.
- **Database:** PostgreSQL


#### Screenshots from the web application:

- Home page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/index.png)

- Sign up page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/sign%20up.png)

- Log in page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/log%20in.png)

- Authenticated user home page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/user_page.png)

- Profile Details page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/profile_details.png)

- Project type creation page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/project_creation.png)

- Project with existing infrastructure creation page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/poject_with_infr.png)

- Project with existing infrastructure details page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/poject_with_infr_details.png)

- Project without existing infrastructure page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/project_without_inf.png)

- Project without existing infrastructure details page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/project_without_inf_details.png)

- Project for new infrastructure creation page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/project_infrastr.png)

- Project for new infrastructure details page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/project_infrastr_details.png)

- User Projects page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/user_projects.png)

- User Reviews page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/user_reviews.png)

- User Contact page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/profile_contact.png)

- Superuser admin page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/super_user_admin.png)

- Staff admin page:

![](https://github.com/SimeonZhelinski/wss_app/blob/main/app_screenshots/staff_admin.png)

##### Regulations:
- The number of fire hydrants calculations are made based on Regulation No. Iз-1971 of October 29, 2009, for construction-technical rules and norms for ensuring safety in case of fire.
- All calculations are made based on Regulation No. 4 of June 17, 2005, for the design, construction, and operation of building water supply and sewerage installations.
- The prices are approximate averages for the market and depend on various factors such as the materials used, as well as the manufacturing costs of the contracting company chosen for the project.
