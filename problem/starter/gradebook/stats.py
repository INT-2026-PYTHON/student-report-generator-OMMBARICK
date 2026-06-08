"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass

def average_per_student(records:list[dict])-> dict[str,float]:
    for record in records:
        name=record["name"]
        score=record["score"]
        if name not in student_data:
            student_data[name]={"total":0,"count":0}
        student_data[name]["total"]+=score
        student_data[name]["count"]+=1

    averages={}
    for name,data in student_data.items():

        averages[name]=round(data["total"]/data["count"],2)
    return averages 

def subjects_offered(records:list[dict])-> set[str]:
    return {record["subject"] for record in records}

def top_scorer(records:list[dict])-> tuple[str,float]:
    averages=average_per_student(records)
    top_student=max(averages,key=averages.get)
    return top_student,averages[top_student]

def passing_students(records:list[dict],threshold:float=60.0)-> list[str]:
    averages=average_per_student(records)
    passed=[name for name,avg>=threshold]
    return sorted(passed)
