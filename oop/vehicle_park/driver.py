class Driver:
    def __init__(self, licence_category: str, holidays_starts: object, holidays_ends:object, salary_per_km: float):
        self.licence_category = licence_category
        self.holidays_starts = holidays_starts
        self.holidays_ends = holidays_ends
        self.salary_per_km = salary_per_km

    def can_drive_with_trailer(self):
        if self.licence_category == 'E':
            return "Vairuotojas gali valdyti priekaba"
        return "Vairuotojas negali valdyti priekabos"
