class Candidate:
    number_of_Candidates = 0

    def __init__(self, first_name, last_name, age, specialization, experience_years, skills, candidate_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__specialization = specialization
        self.__experience_years = experience_years
        self.__skills = skills
        self.__candidate_id = candidate_id
        Candidate.number_of_Candidates += 1
    
    @classmethod
    def candidate_count(cls):
        print(f"The number of candidates is: {cls.number_of_Candidates}")

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        self.__age = value

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        self.__specialization = value

    @property
    def experience_years(self):
        return self.__experience_years

    @experience_years.setter
    def experience_years(self, value):
        if value < 0:
            raise ValueError("Experience years cannot be negative")
        self.__experience_years = value

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, value):
        self.__skills = value

    @property
    def candidate_id(self):
        return self.__candidate_id

    @candidate_id.setter
    def candidate_id(self, value):
        self.__candidate_id = value

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Candidate ID: {self.candidate_id}\n"
                f"Specialization: {self.specialization}, Experience years: {self.experience_years}\n"
                f"Skills: {', '.join(self.skills)}\n{'-' * 60}")


class Employee(Candidate):
    def __init__(self, first_name, last_name, age, specialization, experience_years, skills, candidate_id, salary, hire_date):
        super().__init__(first_name, last_name, age, specialization, experience_years, skills, candidate_id)
        self.salary = salary
        self.hire_date = hire_date
        self.performance_rating = None

    def set_performance_rating(self, rating):
        self.performance_rating = rating

    def __str__(self):
        return (super().__str__() +
                f", Salary: {self.salary}, Hire Date: {self.hire_date}, Performance Rating: {self.performance_rating or 'N/A'}")


class Company:
    def __init__(self, company_name, required_specialization, min_experience, required_skills, min_skills_required=2):
        self.__company_name = company_name
        self.__required_specialization = required_specialization
        self.__min_experience = min_experience
        self.__required_skills = required_skills
        self.__min_skills_required = min_skills_required
        self.accepted_candidates = []

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        self.__company_name = value

    @property
    def required_specialization(self):
        return self.__required_specialization

    @required_specialization.setter
    def required_specialization(self, value):
        self.__required_specialization = value

    @property
    def min_experience(self):
        return self.__min_experience

    @min_experience.setter
    def min_experience(self, value):
        if value < 0:
            return ValueError("Minimum experience cannot be negative")
        self.__min_experience = value

    @property
    def required_skills(self):
        return self.__required_skills

    @required_skills.setter
    def required_skills(self, value):
        self.__required_skills = value

    def accept_candidate(self, candidate):
        if candidate.first_name == "Faris" and candidate.last_name == "Yasien":
            self.accepted_candidates.append(candidate)
            print("-" * 85)
            print(f"Candidate {candidate.first_name} {candidate.last_name} has been accepted by {self.company_name} through exception (Wasta) by al-haji.")
            print("-" * 85)
            return

        if candidate.specialization != self.required_specialization:
            print(f"Candidate {candidate.first_name} {candidate.last_name} does not meet specialization requirements for {self.company_name}.")
            return

        if candidate.experience_years < self.min_experience:
            print(f"Candidate {candidate.first_name} {candidate.last_name} does not have enough experience for {self.company_name}.")
            return

        skill_count = sum(1 for skill in self.required_skills if skill in candidate.skills)
        if skill_count < self.__min_skills_required:
            print(f"Candidate {candidate.first_name} {candidate.last_name} does not have enough required skills (at least {self.__min_skills_required} required) for {self.company_name}.")
            return

        self.accepted_candidates.append(candidate)
        print(f"Candidate {candidate.first_name} {candidate.last_name} has been accepted by {self.company_name}.")

    def list_accepted_candidates(self):
        print(f"\nAccepted Candidates in {self.company_name}:")
        for candidate in self.accepted_candidates:
            print(candidate)

    def accepted_count(self):
        return len(self.accepted_candidates)


class System:
    def __init__(self):
        self.companies = []
        self.candidates = []

    def add_company(self, company):
        self.companies.append(company)

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def apply_candidates(self):
        for candidate in self.candidates:
            for company in self.companies:
                company.accept_candidate(candidate)


candidate1 = Candidate("Ahmad", "Ali", 28, "Computer Science", 4, ["Python", "JavaScript", "C"], 1)
candidate2 = Candidate("Hussain", "Mohammed", 26, "Software Development", 3, ["C++", "Ruby", "Python"], 2)
candidate3 = Candidate("Karrar", "Hussain", 30, "Web Development", 5, ["HTML", "CSS", "React", "Node.js"], 3)
candidate4 = Candidate("Faris", "Yasien", 24, "Software Engineering", 1, ["Python"], 9)

employee = Employee("Ahmad", "Ali", 28, "Computer Science", 4, ["Python", "JavaScript", "C"], 1, 5000, "2024-01-01")
employee.set_performance_rating("Excellent")

company1 = Company("Tech Innovations", "Web Development", 2, ["HTML", "CSS", "JavaScript", "React"])
company2 = Company("Data Insights", "Software Development", 3, ["Python", "C++", "Machine Learning", "SQL"])

recruitment_system = System()

recruitment_system.add_company(company1)
recruitment_system.add_company(company2)
recruitment_system.add_candidate(candidate1)
recruitment_system.add_candidate(candidate2)
recruitment_system.add_candidate(candidate3)
recruitment_system.add_candidate(candidate4)
recruitment_system.add_candidate(employee)

recruitment_system.apply_candidates()

company1.list_accepted_candidates()
company2.list_accepted_candidates()

print(f"\nNumber of accepted candidates in {company1.company_name}: {company1.accepted_count()}")
print(f"Number of accepted candidates in {company2.company_name}: {company2.accepted_count()}")

Candidate.candidate_count()
