from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class WorkoutRequest(BaseModel):
    goal: str
    level: str
    days_per_week: int


class FeedbackRequest(BaseModel):
    name: str
    rating: int
    message: str


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.post("/workout")
def generate_workout(request: WorkoutRequest):

    if request.goal.lower() == "weight loss":
        workout = [
            "Day 1: Full Body Cardio + Squats",
            "Day 2: Upper Body + Walking",
            "Day 3: Rest",
            "Day 4: Lower Body + Core",
            "Day 5: Full Body Workout",
            "Day 6: Light Cardio",
            "Day 7: Rest"
        ]

    elif request.goal.lower() == "muscle gain":
        workout = [
            "Day 1: Chest + Triceps",
            "Day 2: Back + Biceps",
            "Day 3: Rest",
            "Day 4: Legs",
            "Day 5: Shoulders + Core",
            "Day 6: Light Cardio",
            "Day 7: Rest"
        ]

    else:
        workout = [
            "Day 1: Full Body Workout",
            "Day 2: Cardio",
            "Day 3: Rest",
            "Day 4: Full Body Workout",
            "Day 5: Core Workout",
            "Day 6: Light Cardio",
            "Day 7: Rest"
        ]

    return {
        "message": "Workout plan generated successfully",
        "goal": request.goal,
        "level": request.level,
        "days_per_week": request.days_per_week,
        "workout_plan": workout
    }


@router.get("/tip")
def get_tip():
    return {
        "tip": "Stay hydrated and maintain proper form during exercise."
    }


@router.get("/nutrition")
def nutrition_tips():
    return {
        "tips": [
            "Drink enough water throughout the day.",
            "Include fruits and vegetables in your meals.",
            "Choose protein-rich foods such as eggs, beans and lentils.",
            "Prefer whole grains when possible.",
            "Maintain regular meal timings."
        ]
    }


@router.post("/feedback")
def submit_feedback(request: FeedbackRequest):
    return {
        "message": "Thank you for your feedback!",
        "name": request.name,
        "rating": request.rating,
        "feedback": request.message
    }