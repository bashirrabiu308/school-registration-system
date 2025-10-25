def generate_code(name):
    """Generate code by taking initials of words, excluding 'of' and 'and'."""
    exclude = {"of", "and"}
    words = name.lower().split()
    initials = [w[0] for w in words if w not in exclude]
    return ''.join(initials)

def generate_reg_number(faculty, department, year, serial):
    faculty_code = generate_code(faculty)
    dept_code = generate_code(department)
    return f"{faculty_code}/{dept_code}/{year[-2:]}/{serial:04d}"
