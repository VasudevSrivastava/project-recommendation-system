
from .models import Project,Rating
from skills.models import Skill
from django.db.models import Avg
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#from django.contrib.auth.models import User



def get_project_recommendations(user):
    user_skills = user.profile.skills.all()
    
    if not user_skills:
        return []
    
    user_skill_names = set(skill.name for skill in user_skills)

    relevant_projects = Project.objects.filter(skill__name__in=user_skill_names).distinct()
    
    if not relevant_projects:
        return []
    
    project_skill_texts = [ " ".join(skill.name for skill in project.skill.all()) for project in relevant_projects]
    user_skill_text = " ".join(user_skill_names)

    vectorizer = TfidfVectorizer()
    skill_vectors = vectorizer.fit_transform([user_skill_text] +project_skill_texts)
    similirity_scores = cosine_similarity(skill_vectors[0],skill_vectors[1:]).flatten()

    project_ratings = {
        project.id : Project.objects.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0

        for project in relevant_projects
    }

    ranked_projects = []

    for project,score in zip(relevant_projects,similirity_scores):
        rating = project_ratings.get(project.id,0)
        final_score = (0.7 * score ) + (0.3 * rating)
        ranked_projects.append((project,final_score))

    ranked_projects.sort(key = lambda x: x[1], reverse=True)
    return ranked_projects
    #return [project for project,_ in ranked_projects]




