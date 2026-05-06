from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, ValidationError, field_validator
from typing import Literal
from langchain_community.chat_models import ChatOpenAI
import os

# List of doctor categories
DOCTOR_CATEGORIES = [
    "Neurologist", "Oncologist", "Cardiologist", "Endocrinologist", "Dermatologist",
    "Gynecologist", "Psychiatrist", "Gastroenterologist", "Pediatrician", "Radiologist",
    "Geriatrician", "Ophthalmologist", "Nephrologist", "Hematologist", "Pulmonologist",
    "Anesthesiologist", "Orthopedic Surgeon", "General Physician"
]

# Pydantic model for validation
class DoctorCategory(BaseModel):
    category: Literal[
        "Neurologist", "Oncologist", "Cardiologist", "Endocrinologist", "Dermatologist",
        "Gynecologist", "Psychiatrist", "Gastroenterologist", "Pediatrician", "Radiologist",
        "Geriatrician", "Ophthalmologist", "Nephrologist", "Hematologist", "Pulmonologist",
        "Anesthesiologist", "Orthopedic Surgeon", "General Physician"
    ]

    # Field validator for category
    @field_validator('category')
    def check_valid_category(cls, value):
        if value not in DOCTOR_CATEGORIES:
            raise ValueError(f"{value} is not a valid doctor category.")
        return value

# Function to query the AI model
def get_doctor_category(disease_name: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "").strip().lower()
    if not provider:
        provider = "openai" if os.getenv("OPENROUTER_API_KEY") else "groq"

    if provider == "groq" and not os.getenv("GROQ_API_KEY"):
        provider = "openai"
    if provider == "openai" and not os.getenv("OPENROUTER_API_KEY"):
        provider = "groq"

    if provider == "groq":
        model_name = os.getenv("GROQ_MODEL", "groq/llama-3.1-8b-instant")
        chat = ChatOpenAI(
            model=model_name,
            temperature=0.2,
            base_url="https://api.groq.com/openai/v1",
            api_key=os.getenv("GROQ_API_KEY"),
        )
    else:
        model_name = os.getenv("OPENAI_MODEL","deepseek/deepseek-chat-v3-0324")
        chat = ChatOpenAI(
            model=model_name,
            temperature=0.2,
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

    response = chat.invoke([
        {"role": "system", "content": "You are a medical assistant. Only respond with a single doctor category from the list."},
        {"role": "user", "content": f"Which doctor category can diagnose the disease: {disease_name}? Choose from: {', '.join(DOCTOR_CATEGORIES)}. Do not provide explanations or multiple categories, only the category name."}
    ])
    response = response.content.strip()
    
    print('DiseaseName, Response is-------', disease_name, response)
    # Validate the response
    try:
        valid_category = DoctorCategory(category=response.strip())
        return valid_category.category
    except ValidationError as e:
        raise ValueError(f"Invalid response from the AI model: {e}")

# # Example usage
# if __name__ == "__main__":
#     disease = "diabetes"
#     try:
#         doctor_category = get_doctor_category(disease)
#         print(f"The doctor category for '{disease}' is: {doctor_category}")
#     except ValueError as e:
#         print(e)