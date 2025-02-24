# Project Recommendation App

## 🔹 Overview
This is a web app that allows users to **submit projects**, **browse & filter projects**, and **get personalized recommendations** based on their skills.

## 🔹 Features
### 1️⃣ User Management
- User **signup/login/logout**.
- User **profile page** with skills & saved projects.

### 2️⃣ Project Contribution
- Users can **submit projects** with:
  - Title
  - Description
  - GitHub Link
  - Star Rating (out of 5)
  - Date Posted
  - Author

### 3️⃣ Recommendation System
- Users **enter their skills** → App **suggests projects** using **cosine similarity**.
- Recommendation **API returns ranked projects**.

### 4️⃣ Browse & Filter Projects
- View all **projects with filtering & sorting**:
  - Sort by **date, popularity, relevance**.
  - Filter by **tech stack, difficulty level**.

### 5️⃣ Save & Track Projects
- Users can **save projects to their profile**.
- Dashboard shows **top contributors**.

## 🔹 Tech Stack
- **Backend:** Django + Django REST Framework (DRF)
- **Frontend:** Django Templates + AJAX (Room for React in the future)
- **Database:** PostgreSQL / SQLite
- **Recommendation Algorithm:** Cosine Similarity (TF-IDF)

## 🔹 Future Enhancements
- Resume Parsing for Auto-Skill Detection
- Collaboration Requests on Projects
- React Frontend Integration


✔ User login/signup
✔ User profile page
✔ Project contribution
✔ Recommendation API
✔ Browse & filter projects
✔ Save projects to profile
✔ Dashboard with top contributors
✔ Track project views (popularity metric)
✔ User ratings for projects (1-5 stars)
✔ Predefined skill options instead of free-text entry

User Authentication			
POST	/api/auth/signup/	Register a new user	❌ No
POST	/api/auth/login/	User login	❌ No
POST	/api/auth/logout/	User logout	✅ Yes
GET	/api/user/profile/	Get logged-in user's profile	✅ Yes
PUT	/api/user/profile/update/	Update user profile	✅ Yes
Projects			
GET	/api/projects/	List all projects	❌ No
POST	/api/projects/add/	Add a new project	✅ Yes
GET	/api/projects/<id>/	Get details of a specific project	❌ No
PUT	/api/projects/<id>/update/	Update a project (only by author)	✅ Yes
DELETE	/api/projects/<id>/delete/	Delete a project (only by author)	✅ Yes
Project Recommendations			
GET	/api/recommendations/?skills=python,react	Get recommended projects based on skills	❌ No
Ratings			
POST	/api/projects/<id>/rate/	Submit a rating for a project	✅ Yes
GET	/api/projects/<id>/ratings/	Get ratings for a project	❌ No
Skills			
GET	/api/skills/	Get all available skill options	❌ No
Saved Projects			
POST	/api/projects/<id>/save/	Save a project to user profile	✅ Yes
GET	/api/user/saved_projects/	Get all saved projects of logged-in user	✅ Yes
DELETE	/api/projects/<id>/unsave/	Remove a project from saved list	✅ Yes
Dashboard			
GET	/api/dashboard/	Get top contributors and project stats	❌ No