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


class JuniorCandidate(Candidate):
    def __init__(self, first_name, last_name, age, specialization, experience_years, skills, candidate_id, training_program):
        super().__init__(first_name, last_name, age, specialization, experience_years, skills, candidate_id)
        self.__training_program = training_program
    
    @property
    def training_program(self):
        return self.__training_program
    
    @training_program.setter
    def training_program(self, value):
        self.__training_program = value

    # إعادة تعريف دالة __str__ لإضافة معلومات البرنامج التدريبي
    def __str__(self):
        return (super().__str__() + f"Training Program: {self.training_program}\n{'-' * 60}")


class MidLevelCandidate(Candidate):
    def __init__(self, first_name, last_name, age, specialization, experience_years, skills, candidate_id, certifications):
        super().__init__(first_name, last_name, age, specialization, experience_years, skills, candidate_id)
        self.__certifications = certifications
    
    @property
    def certifications(self):
        return self.__certifications
    
    @certifications.setter
    def certifications(self, value):
        self.__certifications = value

    # إعادة تعريف دالة __str__ لإضافة الشهادات
    def __str__(self):
        return (super().__str__() + f"Certifications: {', '.join(self.certifications)}\n{'-' * 60}")


class ExpertCandidate(Candidate):
    def __init__(self, first_name, last_name, age, specialization, experience_years, skills, candidate_id, leadership_projects):
        super().__init__(first_name, last_name, age, specialization, experience_years, skills, candidate_id)
        self.__leadership_projects = leadership_projects
    
    @property
    def leadership_projects(self):
        return self.__leadership_projects
    
    @leadership_projects.setter
    def leadership_projects(self, value):
        self.__leadership_projects = value

    # إعادة تعريف دالة __str__ لإضافة مشاريع القيادة
    def __str__(self):
        return (super().__str__() + f"Leadership Projects: {', '.join(self.leadership_projects)}\n{'-' * 60}")


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
            raise ValueError("Minimum experience cannot be negative")
        self.__min_experience = value

    @property
    def required_skills(self):
        return self.__required_skills

    @required_skills.setter
    def required_skills(self, value):
        self.__required_skills = value

    def accept_candidate(self, candidate):
        if candidate.first_name == "Faris" and candidate.last_name == "Yasien":
            # قبول فارس ياسين بدون شروط
            self.accepted_candidates.append(candidate)
            print(f"Candidate {candidate.first_name} {candidate.last_name} has been accepted by {self.company_name} through exception (Wasta).")
            return

        if candidate.specialization != self.required_specialization:
            print(f"Candidate {candidate.first_name} {candidate.last_name} does not meet specialization requirements.")
            return

        if candidate.experience_years < self.min_experience:
            print(f"Candidate {candidate.first_name} {candidate.last_name} does not have enough experience.")
            return

        skill_count = sum(1 for skill in self.required_skills if skill in candidate.skills)
        if skill_count < self.__min_skills_required:
            print(f"Candidate {candidate.first_name} {candidate.last_name} does not have enough required skills.")
            return

        self.accepted_candidates.append(candidate)
        print(f"Candidate {candidate.first_name} {candidate.last_name} has been accepted by {self.company_name}.")

    def list_accepted_candidates(self):
        print(f"\nAccepted Candidates in {self.company_name}:")
        for candidate in self.accepted_candidates:
            print(candidate)


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


# إنشاء المرشحين
candidate1 = JuniorCandidate("Ahmad", "Ali", 22, "Computer Science", 0, ["Python", "JavaScript"], 1, "Python Bootcamp")
candidate2 = MidLevelCandidate("Hussain", "Mohammed", 26, "Software Development", 3, ["C++", "Ruby", "Python"], 2, ["AWS Certification", "Oracle Certification"])
candidate3 = ExpertCandidate("Karrar", "Hussain", 30, "Web Development", 5, ["HTML", "CSS", "React", "Node.js"], 3, ["E-commerce Project", "CRM System"])
candidate4 = Candidate("Faris", "Yasien", 24, "Software Engineering", 1, ["Python"], 4)  # مرشح بالواسطة

# إنشاء الشركات
company1 = Company("Tech Innovations", "Web Development", 2, ["HTML", "CSS", "JavaScript", "React"])
company2 = Company("Data Insights", "Software Development", 3, ["C++", "Java", "Python"])

# إضافة الشركات والمرشحين للنظام
system = System()
system.add_company(company1)
system.add_company(company2)
system.add_candidate(candidate1)
system.add_candidate(candidate2)
system.add_candidate(candidate3)
system.add_candidate(candidate4)

# تقديم الطلبات
system.apply_candidates()

# عرض المرشحين المقبولين
company1.list_accepted_candidates()
company2.list_accepted_candidates()
