from abc import ABC, abstractmethod


# Abstract base class Person
class Person(ABC):
    @abstractmethod
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

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

    @abstractmethod
    def __str__(self):
        pass


# Candidate class
class Candidate(Person):
    number_of_Candidates = 0

    def __init__(self, first_name, last_name, age, specialization, experience_years, skills, candidate_id):
        super().__init__(first_name, last_name, age)
        self.__specialization = specialization
        self.__experience_years = experience_years
        self.__skills = skills
        self.__candidate_id = candidate_id
        Candidate.number_of_Candidates += 1

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

    def __repr__(self):
        return f"Candidate({self.first_name}, {self.last_name}, ID={self.candidate_id})"

    def __eq__(self, other):
        if isinstance(other, Candidate):
            return self.experience_years == other.experience_years and len(self.skills) == len(other.skills)
        return False

    def __lt__(self, other):
        if isinstance(other, Candidate):
            return self.experience_years < other.experience_years
        raise TypeError(f"Cannot compare Candidate with {type(other)}")

    def __len__(self):
        return len(self.skills)


# Employee class
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


# Company class
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

    @property
    def required_specialization(self):
        return self.__required_specialization

    @property
    def min_experience(self):
        return self.__min_experience

    @property
    def required_skills(self):
        return self.__required_skills

    def accept_candidates(self, candidate):
        if candidate.specialization != self.required_specialization:
            return
        if candidate.experience_years < self.min_experience:
            return
        skill_count = sum(1 for skill in self.required_skills if skill in candidate.skills)
        if skill_count < self.__min_skills_required:
            return
        self.accepted_candidates.append(candidate)

    def __len__(self):
        return len(self.accepted_candidates)

    def __repr__(self):
        return f"Company({self.company_name}, Accepted={len(self)})"


# System class
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
                company.accept_candidates(candidate)



candidate1 = Candidate("Ali", "Mohammed", 32, "Data Science", 5, ["Python", "R", "SQL","HTML", "CSS"], 4)
candidate2 = Candidate("Sara", "Fahad", 25, "Software Development", 3, ["Java", "C#", "SQL"], 5)
candidate3 = Candidate("Omar", "Youssef", 29, "Web Development", 5, ["HTML", "CSS", "JavaScript","Python","C#"], 6)
candidate4 = Candidate("Laila", "Nasir", 27, "Data Science", 4, ["Python", "SQL", "Tableau"], 7)
candidate5 = Candidate("Hassan", "Ali", 33, "Software Development", 6, ["C++", "Java", "Python","HTML", "CSS", "JavaScript"], 8)
candidate6 = Candidate("Rana", "Hussein", 28, "Web Development", 3, ["HTML", "CSS", "Node.js"], 9)

    
employee1 = Employee("Ahmed", "Ali", 30, "Data Science", 6, ["Python", "Machine Learning"], 7, 6000, "2022-02-01")
employee1.set_performance_rating("Excellent")

company1 = Company("Tech Innovations", "Web Development", 2, ["HTML", "CSS", "JavaScript", "React"])
company2 = Company("Data Insights", "Data Science", 3, ["Python", "SQL", "R"])

    
recruitment_system = System()
recruitment_system.add_company(company1)
recruitment_system.add_company(company2)

recruitment_system.add_candidate(candidate1)
recruitment_system.add_candidate(candidate2)
recruitment_system.add_candidate(candidate3)
recruitment_system.add_candidate(candidate4)
recruitment_system.add_candidate(candidate5)
recruitment_system.add_candidate(candidate6)
recruitment_system.add_candidate(employee1)

recruitment_system.apply_candidates()

print("\n Comparing candidates")
print(f"Are {candidate1.first_name} and {candidate2.first_name} equal? {candidate1 == candidate2}")
print(f"Are {candidate1.first_name} and {candidate3.first_name} equal? {candidate1 == candidate3}")
print(f"Are {candidate4.first_name} and {candidate5.first_name} equal? {candidate4 == candidate5}")

   
print("\n Sorting candidates by years of experience ")
sorted_candidates = sorted([candidate1, candidate2, candidate3, candidate4, candidate5, candidate6])
for candidate in sorted_candidates:
    print(candidate)

    
print("\n Counting the number of skills for each candidate ")
print(f"{candidate1.first_name} has {len(candidate1)} skills.")
print(f"{candidate2.first_name} has {len(candidate2)} skills.")
print(f"{candidate3.first_name} has {len(candidate3)} skills.")
print(f"{candidate4.first_name} has {len(candidate4)} skills.")
print(f"{candidate5.first_name} has {len(candidate5)} skills.")
print(f"{candidate6.first_name} has {len(candidate6)} skills.")


print(f"\nNumber of accepted candidates in {company1.company_name}: {len(company1)}")
print(f"Number of accepted candidates in {company2.company_name}: {len(company2)}")
