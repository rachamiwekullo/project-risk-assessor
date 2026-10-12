"""Simple rule-based examples for construction and livestock risk."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Project:
    project_id: str
    crew_size: int
    days_remaining: int
    tasks_left: int


def predict_delivery_risk(crew_size: int, days_remaining: int, tasks_left: int) -> str:
    if crew_size <= 0 or days_remaining <= 0 or tasks_left < 0:
        raise ValueError("Crew and days must be positive; remaining tasks cannot be negative.")
    tasks_per_worker_day = tasks_left / (crew_size * days_remaining)
    if tasks_per_worker_day > 1.5:
        return "High"
    if tasks_per_worker_day > 0.8:
        return "Medium"
    return "Low"


def assess_goat_health(weight_loss_kg: float, feed_drop_pct: float, age_years: float) -> str:
    if min(weight_loss_kg, feed_drop_pct, age_years) < 0:
        raise ValueError("Livestock measurements cannot be negative.")
    risk_score = 0
    risk_score += 2 if weight_loss_kg > 3 else 1 if weight_loss_kg > 1.5 else 0
    risk_score += 2 if feed_drop_pct > 30 else 1 if feed_drop_pct > 15 else 0
    risk_score += 1 if age_years > 8 else 0
    if risk_score >= 4:
        return "High"
    if risk_score >= 2:
        return "Medium"
    return "Low"


def main() -> None:
    projects = [
        Project("project-A", 3, 5, 25),
        Project("project-B", 4, 10, 18),
        Project("project-C", 2, 3, 12),
    ]
    print("Construction schedule risk (rule-based demo):")
    for project in projects:
        risk = predict_delivery_risk(
            project.crew_size, project.days_remaining, project.tasks_left
        )
        print(f"  {project.project_id}: {risk}")

    print("\nLivestock health flags (rule-based demo):")
    sample_animals = [("animal-01", 4.2, 35, 3), ("animal-02", 0.5, 8, 2)]
    for animal_id, weight_loss, feed_drop, age in sample_animals:
        risk = assess_goat_health(weight_loss, feed_drop, age)
        print(f"  {animal_id}: {risk}")


if __name__ == "__main__":
    main()
