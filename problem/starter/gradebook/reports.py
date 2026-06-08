"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass

def format_report(records: list[dict])->str:
  total_records=len(records)
  subjects=str(sorted(list(subjects_offered(records))))
  average=average_per_student(records)
  top_name,top_avg=top_scorer(records)
  passed=str(passing_students(records))

  averagetext=""
  for name,avg in sorted(average.items()):
    averagetext+="{name}:{avg}"
  return f"""STUDENT report
total records:{total}
subjects:{subjects}
student_Average:{avg_text}

top_Scorer:{top_name} {top_avg}
 passing_Students:{passed}"""