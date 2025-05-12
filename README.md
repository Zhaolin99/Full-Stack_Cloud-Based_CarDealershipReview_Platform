# SmartDealerships: Full-Stack Cloud-Based Car Dealership Review Platform

## 📌 Overview

SmartDealerships is a full-stack web application developed as the capstone project for the IBM Full Stack Cloud Developer Professional Certificate. The platform enables users to browse car dealerships, read and write reviews, and manage dealership information. It leverages modern web technologies and cloud services to provide a scalable and responsive user experience.

## 🚀 Features

- **User Authentication:** Secure login and registration system for users.
- **Dealership Listings:** Browse and search for car dealerships with detailed information.
- **Review System:** Users can submit and read reviews for dealerships.
- **Admin Panel:** Administrative interface for managing dealerships and reviews.
- **Responsive Design:** Mobile-friendly interface built with React.js and Bootstrap.
- **Cloud Deployment:** Application deployed on IBM Cloud using Docker containers.

## 🛠️ Technologies Used

- **Frontend:** React.js, Bootstrap, HTML5, CSS3
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** Django's built-in authentication system
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud Platform:** IBM Cloud

## 📂 Project Structure
xrwvm-fullstack_developer_capstone/
├── client/ # React frontend
│ ├── public/
│ └── src/
│ ├── components/
│ ├── App.js
│ └── index.js
├── server/ # Django backend
│ ├── manage.py
│ ├── server/
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── dealership/
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── serializers.py
│ │ └── urls.py
├── Dockerfile
├── docker-compose.yml
└── README.md



## ⚙️ Installation and Setup

1. **Clone the repository:**
   ```bash
     git clone https://github.com/Zhaolin99/xrwvm-fullstack_developer_capstone.git
     cd xrwvm-fullstack_developer_capstone

2. ** Backend Setup
   ```bash
    cd server
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
   
3. ** Frontend Setup
   ```bash
    cd ../client
    npm install
    npm start

4. ** Access the Application
   ```bash
   http://localhost:3000

5. ** Docker Deployment
   ```bash
   docker-compose up --build
   http://localhost:8000
6. ** Running Test
   ```bash
    cd server
    python manage.py test
  
    cd client
    npm test



## 📄 License  
This project is licensed under the **MIT License**. You are free to use, modify, and distribute the code under the terms specified in the LICENSE file.  

## 🙌 Acknowledgements  
- [IBM Full Stack Cloud Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer)  
- [Django Documentation](https://docs.djangoproject.com/)  
- [React Documentation](https://reactjs.org/docs/getting-started.html)  
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)  
- [Docker Documentation](https://docs.docker.com/)  
- [GitHub Actions Documentation](https://docs.github.com/en/actions)  


